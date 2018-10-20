import datetime

__version__ = '1.0.0'
__versiondate__=datetime.date(2018, 10, 20)
#dateversion=datetime.date(2000, 1, 1)#When developing


def version(platform=None):
    """platform can be win32 or linux"""
    if platform==None:
        platform=sys.platform
    if platform=="win32":
        return "{}.{}.{}".format(dateversion.year, dateversion.month, dateversion.day)
    else:
        print("version",  platform)
        return  str(dateversion).replace("-", "")
