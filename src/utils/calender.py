import time
from datetime import date
from datetime import datetime
from datetime import timedelta
from typing import Union


def calendar_current_datetime() -> datetime:
    """当前时间"""
    return datetime.now()


def calendar_current_date() -> date:
    """当前时间"""
    return date.today()


def calendar_current_ts() -> float:
    """当前时间"""
    return time.time()


def calendar_current_string() -> str:
    """当前时间"""
    # return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


def calendar_dt_to_str(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def calendar_dt_to_ts(dt: datetime) -> float:
    return dt.timestamp()


def calendar_dt_to_da(dt: datetime) -> date:
    return dt.date()


def calendar_da_to_str(da: date) -> str:
    return da.strftime("%Y-%m-%d")


def calendar_da_to_dt(da: date) -> datetime:
    return datetime(da.year, da.month, da.day)


def calendar_da_to_ts(da: date) -> float:
    return calendar_da_to_dt(da).timestamp()


def calendar_str_to_dt(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


def calendar_str_to_da(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def calendar_ts_to_dt(ts: float) -> datetime:
    return datetime.fromtimestamp(ts)


def calendar_ts_to_da(ts: float) -> date:
    return date.fromtimestamp(ts)


def calendar_td_to_sec(td: timedelta) -> int:
    return td.seconds + td.days * 24 * 3600

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


def calendar_count_down_sec(time_point: Union[datetime, str, float]):
    """还有多少秒到达传入的时间"""
    if isinstance(time_point, datetime):
        return calendar_td_to_sec(time_point - datetime.now())
    elif isinstance(time_point, str):
        return calendar_td_to_sec(calendar_str_to_dt(time_point) - datetime.now())
    else:
        return calendar_td_to_sec(calendar_ts_to_dt(time_point) - datetime.now())


def calendar_count_down_day(time_point: Union[date, str, float]):
    """还有多少天到达传入的日期"""
    if isinstance(time_point, date):
        return (time_point - date.today()).days
    elif isinstance(time_point, str):
        return (calendar_str_to_da(time_point) - date.today()).days
    else:
        return (calendar_ts_to_da(time_point) - date.today()).days


def calendar_after(**kwargs) -> datetime:
    """
    当前时间±一段时间后的日期
    :param kwargs:
        weeks
        days
        hours
        minutes
        seconds
        microseconds
    :return:
    """
    return datetime.now() + timedelta(**kwargs)
