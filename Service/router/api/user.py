"""
    用户接口
"""
from ..prefix import *              # 固定内容
# --------------------------------
from common.flask_base.Token import TokenHelper
from model import ModelUser, ModelPassword
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
    :request: <request.cookies> {}
    :response: <json> {
        code: 0=登录成功, else=登录失败
        msg: 说明信息
        name:
        uid:
        token:
    }
    :response: <cookie> {
        uid:
        token:
    }
    """
    if not check_must_keys(['account', 'password'], request.form):
        return make_json_return({'code': 1, 'msg': "缺少必要参数"})

    # 检查用户存在性
    usr_items = ModelUser.query.filter_by(id=request.form['account'], is_delete=False)
    if 0 == usr_items.count():
        return make_json_return({'code': 1, 'msg': "不存在的用户"})

    # 密码是否存在
    usr_item = usr_items[0]
    pwd_items = ModelPassword.query.filter_by(uid=usr_item.id, is_delete=False)
    if 0 == pwd_items.count():
        return make_json_return({'code': 1, 'msg': "权限认证失败1"})

    # 密码是否正确
    pwd_item = pwd_items[0]
    if request.form['password'] != pwd_item.pwd:
        return make_json_return({'code': 1, 'msg': "权限认证失败2"})

    # 登录成功
    token = TokenHelper.make(
        request.form['account'],
        request.form['password'],
        request.remote_addr
    )
    TokenHelper.set(usr_item.id, token, request.remote_addr)
    expire_time = the_app.config['TOKEN_EXPIRE_TIME']
    print(expire_time)
    return make_json_return({
        'code': 0,
        'name': usr_item.name,
        'uid': usr_item.id,
        'token': token,
        'msg': "登录成功"
    }, cookie={
        'uid': [usr_item.id, expire_time, '/'],
        'token': [token, expire_time, '/']
    })


@the_app.route(URL_PREFIX + '/authority', methods=['POST'])
def api_user_authority():
    """
    用户登录接口
    :request: <request.cookies> {
        uid:
        token:
    }
    :response: <json> {
        code: 0=登录成功, else=登录失败
        msg: 说明信息
        authority:
    }
    """
    if not check_must_keys(['uid', 'token'], request.cookies):
        return make_json_return({'code': 1, 'msg': "权限认证失败"})

    # 检查Token是否有效
    if not TokenHelper.check(request.cookies, request.remote_addr):
        return make_json_return({'code': 1, 'msg': "无效的Token"})

    # 获取用户
    items = ModelUser.query.filter_by(id=request.cookies['uid'], is_delete=False)
    if 0 == items.count():
        return make_json_return({'code': 1, 'msg': "无效用户ID"})

    # 获取身份权限
    item = items[0]
    # 略

    # 根据权限返回信息
    return make_json_return({
        'code': 0,
        'msg': "获取成功",
        'authority': None
    })
