

def check_must_keys(items, args):
    """
    :param items: [必备参数, ...]
    :param args: request.args | request.form | request.cookies
    :return: {Boolean}
    """
    r = True
    for item in items:
        r = r and (item in args)
    return r
