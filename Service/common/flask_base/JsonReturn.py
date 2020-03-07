from app import the_app
import json


def make_json_return(data, code=200, header=None):
    # 响应头
    return_header = {
        'Content-Type': 'text/json'
    }
    return_header.update(the_app.config['COMMON_HEAD'])
    if header is not None:
        return_header.update(header)

    return json.dumps(data), code, return_header
