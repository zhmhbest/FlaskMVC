"""
    请勿修改本文件
"""
from app import the_app, the_db
from model import *


if __name__ == '__main__':
    # 强制打开SQL语句打印
    the_app.config['SQLALCHEMY_ECHO'] = True

    with the_app.app_context():
        # 清除数据库所有内容
        the_db.drop_all()

        # 根据模型创建数据库表
        the_db.create_all()

    print(the_app.config['SQLALCHEMY_DATABASE_URI'])
