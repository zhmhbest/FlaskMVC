from flask_restful import Resource
from flask_sqlalchemy import BaseQuery

from model import UserInfo
from utils.EasyFlask import request, return_json, check_params, RESTRICTIVE_RULES
from utils.EasyToken import Token
from utils.Message import CodeMessage
from utils.coder import sha256


# noinspection PyMethodMayBeStatic
class personal(Resource):
    def get(self):
        """
        查看用户登录状态是否有效
        若有效返回用户信息
        [arg_cookies]
            uid
            token
        [return_data]
            是否成功
        """
        return {
            'ok': Token.wise_check(),
            'data': {}
        }

    def post(self):
        """
        用户个人登录 / 注销当前登录

        [arg_params]
            account: 用户名
            password: 密码
        [return_data]
            ok: 是否成功
            code: 状态码
            message: 其它信息
            data: 响应数据
        [return_cookies]
            token: 用户身份码
        """
        # 检查必要信息
        msg, args = check_params({
            'account': (RESTRICTIVE_RULES['words'], True),
            'password': (RESTRICTIVE_RULES['words'], True)
        })
        if msg is not None:
            return return_json({
                'ok': False,
                'code': CodeMessage['请求参数错误'],
                'message': msg
            }, cookie={'uid': ('', 0, '/'), 'token': ('', 0, '/')})

        info_all: BaseQuery = UserInfo.query.filter_by(account=args['account'])
        if info_all.count() > 0:
            info: UserInfo = info_all[0]
            pwd: str = info.Passwords[0].pwd
            if pwd == args['password']:
                # 生成token
                token = Token(
                    info.uid, request.remote_addr,
                    args['account'] + sha256(args['password'])
                )
                token.set_user_token()
                token.load_to_session()

                return return_json({
                    'ok': True,
                    'code': CodeMessage['登录成功'],
                    'data': {
                        'uid': info.uid,
                        'name': info.name
                    }
                }, cookie={'uid': info.uid, 'token': token.get_token()})

        # 检查失败
        return return_json({
            'ok': False,
            'code': CodeMessage['登录失败']
        }, cookie={'uid': ('', 0, '/'), 'token': ('', 0, '/')})
