"""
    请勿修改本文件
"""
from flask import Flask
from model import the_db


the_app = Flask(__name__)
the_app.config.from_pyfile('config.py')
the_db.init_app(the_app)
