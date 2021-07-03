from sys import _getframe as __frame__


def __current__():
    return __frame__().f_back


def __line__() -> int:
    """
    所在位置行号
    """
    return __current__().f_lineno


def __fun__() -> str:
    """
    所在位置函数名
    """
    return __current__().f_code.co_name


def __filename__() -> str:
    """
    所在位置文件名
    """
    return __current__().f_code.co_filename
