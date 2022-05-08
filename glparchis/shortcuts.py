## @namespace glparchis.shortcuts 
## @brief Creates windows shortcuts

from os import path, remove as os_remove
from pythoncom import CoCreateInstance,CLSCTX_INPROC_SERVER, ID_IPersistFile#Viene en pywin32
from pkg_resources import resource_filename
from win32com.shell import shell, shellcon

##Creates a shortcut in the Windows Desktop
def create():
    shortcut = CoCreateInstance (
      shell.CLSID_ShellLink,
      None,
      CLSCTX_INPROC_SERVER,
      shell.IID_IShellLink
    )

    icon=resource_filename("glparchis","images/glparchis.ico")
    shortcut.SetPath (r'glparchis.exe')
    shortcut.SetDescription ("Parchís game")
    shortcut.SetIconLocation (icon, 0)
     
    desktop_path = shell.SHGetFolderPath (0, shellcon.CSIDL_DESKTOP, 0, 0)
    persist_file = shortcut.QueryInterface (ID_IPersistFile)
    persist_file.Save (path.join (desktop_path, "glParchis.lnk"), 0)
    
    print("A shortcut have been placed in your desktop ;)")

##Removes the shortcut from the Windows Desktop
def remove():
    desktop_path = shell.SHGetFolderPath (0, shellcon.CSIDL_DESKTOP, 0, 0)
    os_remove(path.join (desktop_path, "glParchis.lnk"))

