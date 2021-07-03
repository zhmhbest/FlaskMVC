"""
    参数验证、获取及数据返回
"""
import re
import json
from typing import Union, Tuple, Dict

from flask import request, make_response
from flask.wrappers import Response
from werkzeug.datastructures import ImmutableMultiDict
from config import COMMON_HEAD


RESTRICTIVE_RULES = {
    # 基础
    'integer': r"^[0-9]+$",
    'float': r"^([0-9]+\.)?[0-9]+$",
    'words': r"^[0-9a-zA-Z_]+$",
    # 扩展
    'account': r"^[a-zA-Z0-9_]{4,12}$",
    'password': r"^[a-zA-Z0-9_\.]{6,12}$"
}


def get_one_header_params(text: str) -> dict:
    """
    拆解一个请求头的以`;`分割的参数
    :param text:
    :return:
    """
    holder = {}
    items = text.split(";")
    holder[""] = items[0]
    for i in range(1, len(items)):
        k, v = items[i].split("=")
        holder[k.strip().lower()] = v.strip()
    return holder


def get_json_body() -> dict:
    """
    获取请求体中的JSON
    :return:
    """
    # application/json;charset=UTF-8
    content_type = get_one_header_params(request.headers.get('Content-Type'))
    if content_type[""].lower() == "application/json":
        if "charset" in content_type:
            charset = content_type["charset"]
        else:
            charset = "UTF-8"
        body: str = request.data.decode(charset)
        return json.loads(body)
    return {}


def check_params(expect_keys: Dict[str, Tuple[Union[None, str, type], bool]]) -> Tuple[Union[None, str], dict]:
    """
    :param expect_keys:
        {参数名: (None | 正则匹配规则 | int | float, 是否必须)}
    :returns:
        None | 错误原因, 请求参数
    """
    args: ImmutableMultiDict = request.args.to_dict()
    form: ImmutableMultiDict = request.form.to_dict()
    body = get_json_body()
    args.update(form)
    args.update(body)

    for key in expect_keys.keys():
        rules, is_must = expect_keys[key]

        if key in args:
            # 参数存在，是否符合匹配要求
            if isinstance(rules, str):
                if re.match(rules, args[key]) is None:
                    return f"Mismatched `{key}`", args
            elif rules is int:
                if re.match(RESTRICTIVE_RULES['integer'], args[key]) is None:
                    return f"Mismatched `{key}`", args
                args[key] = int(args[key])
            elif rules is float:
                if re.match(RESTRICTIVE_RULES['float'], args[key]) is None:
                    return f"Mismatched `{key}`", args
                args[key] = float(args[key])
        else:
            # 必须参数不存在
            if is_must:
                return f"Undefined `{key}`", args
            args[key] = None
    # 检查通过，返回参数
    return None, args


def return_json(
        data: dict,
        status: int = 200,
        headers=None,
        cookie=None
) -> Union[Tuple[dict, int, dict], Response]:
    """
    返回带Cookie的JSON
    :param data:
    :param status:
    :param headers:
    :param cookie:
    :return:
    """
    # 响应头
    if headers is None:
        headers: dict = {}
    headers.update(COMMON_HEAD)
    headers.update({
        'Content-Type': 'text/json; charset=utf-8'
    })

    if cookie is None:
        return data, status, headers
    else:
        response = make_response(json.dumps(data, ensure_ascii=False), status)
        for (key, val) in headers.items():
            response.headers[key] = val
        for (key, val) in cookie.items():
            if isinstance(val, list) or isinstance(val, tuple):
                # val = [value, max_age, path])
                response.set_cookie(key, str(val[0]), max_age=val[1], path=val[2])
            else:
                response.set_cookie(key, str(val))
        return response


def get_remote_address():
    return request.remote_addr
