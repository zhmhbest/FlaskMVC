from os import urandom

SERVER_HOST = "localhost"
SERVER_PORT = 5000
SERVER_BASE = f"http://{SERVER_HOST}:{SERVER_PORT}"

HOME_PAGE = "/static/index.html"
SITE_ICON = "/static/favicon.ico"
COMMON_HEAD = {}

DB_HOST = "localhost"
DB_PORT = 3306
DB_USR = "flask"
DB_PWD = "flask"
DB_DBNAME = "flask_mvc"
DB_PARAMS = ""


# Token有效时间（秒） 1d
TOKEN_EXPIRE_TIME = 1 * 24 * 3600
# 小于此时间，自动延长（秒） 3h
TOKEN_EXTEND_EXPIRE_TIME = 3 * 3600


class FlaskConfigHolder:
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USR}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_DBNAME}?{DB_PARAMS}"

    SESSION_TYPE = 'filesystem'
    SECRET_KEY = urandom(24)
