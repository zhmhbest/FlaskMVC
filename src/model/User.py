from app import DB


class UserToken(DB.Model):
    """
    用户 Token
    """
    __tablename__ = 'user_token'

    # Token ID
    id = DB.Column(DB.BIGINT, primary_key=True)

    # （外键）用户ID
    uid = DB.Column(DB.BIGINT, DB.ForeignKey('user_info.uid'))

    # Login IP
    # 255.255.255.255
    login_ip = DB.Column(DB.VARCHAR(20))

    # Token
    token = DB.Column(DB.VARCHAR(128))

    # Expire
    time_add = DB.Column(DB.DateTime)
    time_last_login = DB.Column(DB.DateTime)
    time_expire = DB.Column(DB.DateTime)


class UserPassword(DB.Model):
    """
    用户 密码表
    """
    __tablename__ = 'user_pwd'

    # Pwd ID
    id = DB.Column(DB.BIGINT, primary_key=True)

    # Usr ID（外键）
    uid = DB.Column(DB.BIGINT, DB.ForeignKey('user_info.uid'))

    # 密码
    pwd = DB.Column(DB.VARCHAR(128))

    # 软删除
    is_delete = DB.Column(DB.Boolean, nullable=False, default=False)


class UserInfo(DB.Model):
    """
    用户 信息表
    """
    __tablename__ = 'user_info'

    # User ID
    uid = DB.Column(DB.BIGINT, primary_key=True)

    # 用户名
    account = DB.Column(DB.VARCHAR(32), unique=True)

    # 姓名
    name = DB.Column(DB.VARCHAR(128), unique=False)

    # 软删除
    is_delete = DB.Column(DB.Boolean, nullable=False, default=False)

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # （反映）反向映射外键
    Passwords = DB.relationship(UserPassword)
    Tokens = DB.relationship(UserToken)
