from app import the_app
import json
from flask import make_response


def make_json_return(data, code=200, header=None, cookie=None):
    # 响应头
    return_header = {
        'Content-Type': 'text/json; charset=utf-8'
    }
    return_header.update(the_app.config['COMMON_HEAD'])
    if header is not None:
        return_header.update(header)

    if cookie is None:
        return json.dumps(data), code, return_header
    else:
        response = make_response(json.dumps(data), code)
        # response.status = "200"

        for (key, val) in return_header.items():
            response.headers[key] = val

        for (key, val) in cookie.items():
            if isinstance(val, list):
                # val = [value, max_age, path])
                print(key, val)
                response.set_cookie(key, str(val[0]), max_age=val[1], path=val[2])
            else:
                response.set_cookie(key, str(val))
        return response
