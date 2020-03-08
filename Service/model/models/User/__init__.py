from model.db import the_db as db
from .Password import ModelPassword
from .Token import ModelToken


class ModelUser(db.Model):
    """
    用户 信息表
    """
    __tablename__ = 'tbl_usr'

    # User ID
    id = db.Column(db.BIGINT, primary_key=True)

    # 用户名
    name = db.Column(db.VARCHAR(128), unique=False)

    # 软删除
    is_delete = db.Column(db.Boolean, nullable=False, default=False)

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    # （反映）反向映射外键
    Passwords = db.relationship(ModelPassword, backref='User')
    Tokens = db.relationship(ModelToken, backref='User')
