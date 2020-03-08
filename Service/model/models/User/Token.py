from model.db import the_db as db


class ModelToken(db.Model):
    """
    用户 Token
    """
    __tablename__ = 'tbl_token'

    # Token ID
    id = db.Column(db.BIGINT, primary_key=True)

    # （外键）用户ID
    uid = db.Column(db.BIGINT, db.ForeignKey('tbl_usr.id'))

    # Login IP
    # 255.255.255.255
    login_ip = db.Column(db.VARCHAR(20))

    # Token
    token = db.Column(db.VARCHAR(128))

    # Expire
    time_add = db.Column(db.DateTime)
    time_last_login = db.Column(db.DateTime)
    time_expire = db.Column(db.DateTime)
