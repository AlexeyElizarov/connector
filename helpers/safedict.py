class SafeDict(dict):
    """
    Returns {key} if a key is missing in a dict.
    https://stackoverflow.com/questions/17215400/python-format-string-unused-named-arguments
    """
    def __missing__(self, key):
        return '{' + key + '}'
