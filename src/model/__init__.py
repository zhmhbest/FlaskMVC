"""
    在此处注册要使用的模型
"""
from model.User import UserInfo
from model.User import UserPassword
from model.User import UserToken


if __name__ == '__main__':
    from app import APP, DB

    """初始化数据"""
    def init_db_data():
        # 默认用户
        DB.session.add(UserInfo(account="admin", name="管理员"))
        DB.session.commit()

        user = UserInfo.query.first()
        DB.session.add(UserPassword(uid=user.uid, pwd='admin'))
        DB.session.commit()

    """初始化表"""
    # 打开SQL语句打印
    # APP.config['SQLALCHEMY_ECHO'] = True
    with APP.app_context():
        # 清除数据库所有内容
        DB.drop_all()

        # 根据模型创建数据库表
        DB.create_all()

        # 创建基础数据
        init_db_data()
    print(APP.config['SQLALCHEMY_DATABASE_URI'])
