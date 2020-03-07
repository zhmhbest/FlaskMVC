from ..Time import DateTimeHelper
from ..Hash import md5


class TokenHelper:
    @staticmethod
    def make_user_token(account, password, ip):
        """
        生成User Token
        :param account: 用户帐号
        :param password: 用户密码
        :param ip: 登录IP（防止Token异地使用）
        :return:
        """
        return md5(str(account) + str(password) + str(ip) + str(DateTimeHelper.get_current_time_float()))
