import hashlib
import base64
from urllib.parse import quote, unquote


# VARCHAR(32)
def md5(content: str, encoding: str = 'UTF-8') -> str:
    return hashlib.md5(content.encode(encoding=encoding)).hexdigest()


# VARCHAR(64)
def sha256(content: str, encoding: str = 'UTF-8') -> str:
    return hashlib.sha256(content.encode(encoding=encoding)).hexdigest()


def encode_base64(content: str) -> str:
    return base64.encodebytes(content.encode('UTF-8')).decode('UTF-8').rstrip()


def decode_base64(content: str) -> str:
    return base64.decodebytes(content.encode('UTF-8')).decode('UTF-8')


def encode_url(url: str) -> str:
    return quote(url)


def decode_url(url: str) -> str:
    return unquote(url)


if __name__ == '__main__':
    print(md5("123"))
    print(sha256("123"))

    _b64 = encode_base64("123")
    print(_b64)
    _b64 = decode_base64(_b64)
    print(_b64)

    _url = "https://www.baidu.com/"
    _url = encode_url(_url)
    print(_url)
    _url = decode_url(_url)
    print(_url)
