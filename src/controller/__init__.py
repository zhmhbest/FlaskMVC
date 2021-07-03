"""
    在此处注册要使用的控制器
"""
from app import add_router

from controller.hello import hello
from controller.user import personal
add_router([
    hello,
    personal
])

CONTROLLER_REGISTERED = True
