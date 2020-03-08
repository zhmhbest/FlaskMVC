"""
    请勿修改本文件
"""
from app import the_app as app


# 导入所有注册的接口
from router import *


if __name__ == '__main__':
    if app.config['DEBUG']:
        for item in app.url_map.iter_rules():
            print(" * Map: http://" + str(app.config['SERVER_HOST']) + ':' + str(app.config['SERVER_PORT']) + str(item))
        print()
    # end if

    app.run(host=app.config['SERVER_HOST'], port=app.config['SERVER_PORT'])
