"""
    请勿修改本文件
"""
from flask import Flask
from model.db import the_db
from config import ConfigHolder


the_app = Flask(__name__)
the_app.config.from_object(ConfigHolder)
the_db.init_app(the_app)
