import hashlib


# VARCHAR(32)
def md5(content, encoding='UTF-8'):
    return hashlib.md5(content.encode(encoding=encoding)).hexdigest()


# VARCHAR(64)
def sha256(content, encoding='UTF-8'):
    return hashlib.sha256(content.encode(encoding=encoding)).hexdigest()

