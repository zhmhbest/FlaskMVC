from model.db import the_db as db


class ModelPassword(db.Model):
    """
    用户 密码表
    """
    __tablename__ = 'tbl_pwd'

    # Pwd ID
    id = db.Column(db.BIGINT, primary_key=True)

    # Usr ID（外键）
    uid = db.Column(db.BIGINT, db.ForeignKey('tbl_usr.id'))

    # 密码
    pwd = db.Column(db.VARCHAR(128))

    # 软删除
    is_delete = db.Column(db.Boolean, nullable=False, default=False)
