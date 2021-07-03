from typing import List, Type

from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from config import FlaskConfigHolder

APP = Flask(__name__)
API = Api(APP)
DB = SQLAlchemy()

APP.config.from_object(FlaskConfigHolder)
DB.init_app(APP)


@APP.route("/")
def root():
    """配置主页"""
    from flask import redirect
    from config import HOME_PAGE
    return redirect(HOME_PAGE, code=302)


@APP.route("/favicon.ico")
def root_favicon():
    """配置网站图标"""
    from flask import redirect
    from config import SITE_ICON
    return redirect(SITE_ICON, code=302)


def add_router(resources: List[Type[Resource]]):
    """注册控制器"""
    def get_default_path():
        nonlocal resource
        buff = resource.__module__.split('.')[1:]
        buff.append(resource.__name__)
        return f"/{'/'.join(buff)}"
    for resource in resources:
        default_path = get_default_path()
        API.add_resource(resource, default_path)
