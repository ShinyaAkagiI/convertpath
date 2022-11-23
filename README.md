# convertpath module

pathlib support changing '/' to '\\'. This module is finished the role.

https://docs.python.org/ja/3/library/pathlib.html

```
>>> p = PurePath('/etc')
>>> str(p)
'/etc'
>>> p = PureWindowsPath('c:/Program Files')
>>> str(p)
'c:\\Program Files'
```


Simply Path Convertor for converting from windows path ('C:\\hoge') to linux path ('/C/hoge').  


# PYPI

https://pypi.org/project/convertpath/  


# Setup

```
pip install convertpath
```

# Usage 

```
from convertpath import convertpath_win2linux
convertpath_win2linux('C:\\hoge')
# /C/hoge
```
