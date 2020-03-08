from ..Time import DateTimeHelper
from ..Hash import md5
from model import ModelToken
from model.db import the_db as db
from app import the_app


class TokenHelper:
    @staticmethod
    def make(account, password, ip):
        """
        生成User Token
        :param account: 用户帐号
        :param password: 用户密码
        :param ip: 登录IP（防止Token异地使用）
        :return:
        """
        return md5(str(account) + str(password) + str(ip) + str(DateTimeHelper.get_current_time_float()))

    @staticmethod
    def set(uid, token, ip):
        """
        应用UserToken到数据库
        :param uid: 用户id
        :param token: 用户Token
        :param ip: request.remote_addr
        :return: None
        """
        items = ModelToken.query.filter_by(uid=uid)

        # 删除已存在的Token
        if 0 != items.count():
            db.session.delete(items[0])
        # end if

        # 追加Token
        db.session.add(ModelToken(
            uid=uid,
            login_ip=ip,
            token=token,
            time_add=DateTimeHelper.get_current_datetime(),
            # time_last_login=
            time_expire=DateTimeHelper.after_current_datetime(seconds=
                                                              the_app.config['TOKEN_EXPIRE_TIME'])
        ))
        db.session.commit()

    @staticmethod
    def check(cookies, ip):
        """
         检查用户Token，若低于最低要求时间则延时
        :param cookies: request.cookies {
            uid:
            token:
        }
        :param ip: request.remote_addr
        :return: True | False
        """
        items = ModelToken.query.filter_by(uid=cookies['uid'])

        # 没有Token
        if 0 == items.count():
            return False
        # end if

        # 无效Token
        item = items[0]
        if item.token != cookies['token']:
            return False
        # end if

        # 异地Token
        if item.login_ip != ip:
            return False
        # end if

        # 过期Token
        sec_diff = DateTimeHelper.count_down_datetime_seconds(item.time_expire)
        if sec_diff < 0:
            return False
        # end if

        # 延期Token
        minimum_expire_time = the_app.config['TOKEN_MINIMUM_EXPIRE_TIME']
        if sec_diff < minimum_expire_time:
            item.time_expire = DateTimeHelper.after_current_datetime(seconds=minimum_expire_time)
        # end if

        # 验证成功，修改登录时间
        item.time_last_login = DateTimeHelper.get_current_datetime()
        db.session.commit()
        return True
