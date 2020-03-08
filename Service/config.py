import os


class ConfigHolder:
    DEBUG = True

    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 5000

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<帐号>:<密码>@<HOST>:3306/<数据库名称>'
    SQL_CONFIG = {
        'host': 'localhost',
        'port': '3306',
        'user': 'taxfree',
        'password': '1234',
        'database': 'taxfreeshop',
    }
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (
        SQL_CONFIG['user'], SQL_CONFIG['password'],
        SQL_CONFIG['host'], SQL_CONFIG['port'],
        SQL_CONFIG['database']
    )

    # 数据被修改时，修改模型类
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 打印SQL语句
    SQLALCHEMY_ECHO = False

    # Session
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = os.urandom(24)

    #
    COMMON_HEAD = {
        'Access-Control-Allow-Origin': ','.join([
            '*'
        ])
    }

    # Token有效时间（秒） 1天
    TOKEN_EXPIRE_TIME = 1 * 24 * 3600
    TOKEN_MINIMUM_EXPIRE_TIME = 3 * 3600
