from app import the_app
from model import the_db
from flask import request, make_response
from common.flask_base.JsonReturn import make_json_return


def get_prefix(n):
    r = (n[n.find('.'):]).replace('.', '/')
    print(' *', r)
    return r


def check_must_args(args):
    r = True
    for item in args:
        r = r and (item in request.form)
    return r
