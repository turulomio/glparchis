## @namespace glparchis.shortcuts 
## @brief Creates windows shortcuts

import os
import pythoncom #Viene en pywin32
import pkg_resources
from win32com.shell import shell, shellcon

##Creates a shortcut in the Windows Desktop
def create():
    shortcut = pythoncom.CoCreateInstance (
      shell.CLSID_ShellLink,
      None,
      pythoncom.CLSCTX_INPROC_SERVER,
      shell.IID_IShellLink
    )

    icon=pkg_resources.resource_filename("glparchis","images/glparchis.ico")
    shortcut.SetPath (r'glparchis.exe')
    shortcut.SetDescription ("Parchís game")
    shortcut.SetIconLocation (icon, 0)
     
    desktop_path = shell.SHGetFolderPath (0, shellcon.CSIDL_DESKTOP, 0, 0)
    persist_file = shortcut.QueryInterface (pythoncom.IID_IPersistFile)
    persist_file.Save (os.path.join (desktop_path, "glParchis.lnk"), 0)
    
    print("A shortcut have been placed in your desktop ;)")

##Removes the shortcut from the Windows Desktop
def remove():
    desktop_path = shell.SHGetFolderPath (0, shellcon.CSIDL_DESKTOP, 0, 0)
    os.remove(os.path.join (desktop_path, "glParchis.lnk"))

