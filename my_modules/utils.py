#
def to_unicode(str_or_unicode):
    if isinstance(str_or_unicode, str):
        value = str_or_unicode.decode('utf-8')
    else:
        value = str_or_unicode
    return value

def to_str(str_or_unicode):
    if isinstance(str_or_unicode, unicode):
        value = str_or_unicode.encode('utf-8')
    else:
        value = str_or_unicode
    return value