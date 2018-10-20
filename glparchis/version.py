import datetime
import sys

__versiondate__=datetime.date(2018, 10, 20)
__version__ = '20181020'
#__versiondate__=datetime.date(2000, 1, 1)#When developing

def version(platform=None):
    """platform can be win32 or linux"""
    if platform==None:
        platform=sys.platform
    if platform=="win32":
        return "{}.{}.{}".format(__versiondate__.year, __versiondate__.month, __versiondate__.day)
    else:
        print("version",  platform)
        return str(__versiondate__).replace("-", "")
