from typing import List


class __CodeMessage:
    def __init__(self, messages: List[str], start: int = 100):
        __code = {}
        for i in range(len(messages)):
            __code[messages[i]] = start + i
        self.__start = start
        self.__messages = messages
        self.__code = __code

    def __getitem__(self, message: str) -> int:
        if message in self.__code:
            return self.__code[message]
        else:
            return -1

    def message(self, code: int) -> str:
        return self.__messages[code - self.__start]


CodeMessage = __CodeMessage([
    "登录成功",
    "登录失败",
    "请求参数错误"
])


if __name__ == '__main__':
    # 通过Code获取失败信息
    print(CodeMessage.message(100))
