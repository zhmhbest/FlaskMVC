"""
    解决用户持久化登录，Token、Session转换问题
"""
from typing import Union
from flask import session, request

from app import DB
from config import TOKEN_EXPIRE_TIME, TOKEN_EXTEND_EXPIRE_TIME
from model import UserToken
from utils.calender import calendar_current_ts, calendar_current_datetime, calendar_after, calendar_count_down_sec
from utils.coder import sha256


class Token:
    def __init__(self, uid: int, address: str, salt: str = ''):
        self.uid = uid
        self.address = address
        self.salt = salt
        self.user_token = self.get_user_token()

    def make_token(self) -> str:
        """生成 Token"""
        return sha256(str(self.uid) + self.address + self.salt + str(calendar_current_ts()))

    def get_token(self):
        """获取 Token"""
        return None if self.user_token is None else self.user_token.token

    def get_user_token(self) -> Union[UserToken, None]:
        """获取 User Token"""
        items = UserToken.query.filter_by(uid=self.uid)
        if 0 != items.count():
            return items[0]
        return None

    def set_user_token(self):
        """设置 User Token"""
        if self.user_token is None:
            # 增加
            DB.session.add(UserToken(
                uid=self.uid,
                login_ip=self.address,
                token=self.make_token(),
                time_add=calendar_current_datetime(),
                time_last_login=calendar_current_datetime(),
                time_expire=calendar_after(seconds=TOKEN_EXPIRE_TIME)
            ))
            DB.session.commit()
            self.user_token = self.get_user_token()
        else:
            # 更新
            UserToken.query.filter_by(uid=self.uid).update({
                'login_ip': self.address,
                'token': self.make_token(),
                'time_add': calendar_current_datetime(),
                'time_last_login': calendar_current_datetime(),
                'time_expire': calendar_after(seconds=TOKEN_EXPIRE_TIME)
            })
            DB.session.commit()

    def extend_expire(self):
        """延长到期时间"""
        if self.user_token is not None:
            UserToken.query.filter_by(uid=self.uid).update({
                'time_expire': calendar_after(seconds=TOKEN_EXTEND_EXPIRE_TIME)
            })
            DB.session.commit()

    def update_login(self):
        """更新登录时间"""
        if self.user_token is not None:
            UserToken.query.filter_by(uid=self.uid).update({
                'time_last_login': calendar_current_datetime()
            })
            DB.session.commit()

    def check_token(self, token: str) -> bool:
        """检查Token是否有效"""
        if self.user_token is None:
            return False

        # 错误 Token
        if self.user_token.token != token:
            return False

        # 异地 Token
        if self.user_token.login_ip != self.address:
            return False

        # 过期 Token
        sec_diff = calendar_count_down_sec(self.user_token.time_expire)
        if sec_diff < 0:
            return False

        # 延期Token
        if sec_diff < TOKEN_EXTEND_EXPIRE_TIME:
            self.extend_expire()

        # 验证成功，修改登录时间
        self.update_login()
        return True

    def load_to_session(self):
        """登记信息到Session"""
        if self.user_token is not None:
            session['uid'] = self.uid
            session['token'] = self.user_token.token
            session['address'] = self.address

    @staticmethod
    def wise_check() -> bool:
        cookies = request.cookies
        address = request.remote_addr
        # Cookie(uid, token)
        if not ('uid' in cookies and 'token' in cookies):
            return False
        # Session(uid, token, address)
        if 'uid' in session and 'token' in session and 'address' in session:
            # 通过Session快速验证
            if int(cookies['uid']) == int(session['uid']) and \
                    cookies['token'] == session['token'] and \
                    address == session['address']:
                return True
        else:
            # 加载Session
            token = Token(cookies['uid'], address)
            if token.check_token(cookies['token']):
                token.load_to_session()
                return True
        return False
