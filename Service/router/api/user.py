"""
    用户接口
"""
from ..prefix import *              # 固定内容
# --------------------------------
from common.flask_base.Token import TokenHelper
# --------------------------------
URL_PREFIX = get_prefix(__name__)   # 固定内容
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


@the_app.route(URL_PREFIX + '/login', methods=['POST'])
def api_user_login():
    """
    用户登录接口
    :request: <request.form> {
        account: 登录帐号（手机号码）
        password: 登录密码
    }
    :request: <request.cookies> None
    :response: <json> {
        code: 0=登录成功, else=登录失败
        uid: 用户ID
        token: 用户Token
        expire: Token有效时间（秒）
        msg: 说明信息
    }
    :response: <cookie> None
    """
    if not check_must_args(['account', 'password']):
        return make_json_return({'code': 1, 'msg': "缺少必要参数"})

    remote_ip = request.remote_addr
    token = TokenHelper.make_user_token(
        request.form['account'],
        request.form['password'],
        remote_ip
    )
    return make_json_return({
        'code': 0,
        'uid': -1,
        'token': token,
        'expire': -1,
        'msg': "登录成功"
    })