from datetime import date
from urllib.request import urlopen

__version__ = '20221204'
__versiondate__=date(2022, 12, 4)

## This function expectss __version__= 'VERSION' file
## @return String removeversion or None if it couln't be found
def get_remote(path):
    try:
        web=urlopen(path).read().decode("UTF-8")
    except:
        return None
    if web==None:
        return None
    for line in web.split("\n"):
        if line.find("__version__")!=-1:
            return web.split("'")[1]
    return None
