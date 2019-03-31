import os
from pathlib import Path, PurePosixPath, PureWindowsPath

class convertpath:

    def __init__(self, path=os.environ['HOME']):
        self.path = path

    def win2linux(self, path=None):
        rawpath = path or self.path
        rst = convertpath_win2linux(rawpath)
        return rst


def convertpath_win2linux(path):
    r"""
    Convert a directory path from windows path to linux path

    >>> convertpath_win2linux(r"C:\Users\user")
    '/C/Users/user'
    """
    rst = PurePosixPath(Path(path).absolute())
    rst = str(rst).replace('C:\\', '/C').replace('c:\\', '/c')
    return rst

