from app import *
from controller import *
from config import *

if __name__ == '__main__':
    if CONTROLLER_REGISTERED:
        # 路由信息
        for item in APP.url_map.iter_rules():
            print(f" * {SERVER_BASE}{item}")
        print()
        # 启动应用
        APP.run(
            host=SERVER_HOST,
            port=SERVER_PORT
        )
