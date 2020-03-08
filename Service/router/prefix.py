from app import the_app
from model.db import the_db
from flask import request
from common.flask_base.JsonReturn import make_json_return
from common.Verify import check_must_keys


def get_prefix(n):
    r = (n[n.find('.'):]).replace('.', '/')
    print(' *', r)
    return r


def get_args_without_method():
    return request.args if 'GET' == request.method else request.form


