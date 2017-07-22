##from cx_Freeze import setup, Executable
##import os
##import shutil
##import subprocess
##import sys
##import platform 
##import PyQt5
##sys.path.append('ui')
##sys.path.append('images')
##from libglparchis import version
##
##def winversion():
##    lastpoint="0"
##    if version.find("+")!=-1:
##        lastpoint="1"
##        
##    versio=version.replace("+","")
##    return versio[:-4]+"."+versio[4:-2]+"."+versio[6:]+"."+lastpoint
##    
##def build_dir():
##    pyversion="{}.{}".format(sys.version_info[0], sys.version_info[1])
##    if sys.platform=="win32":
##        so="win"
##        if platform.architecture()[0]=="64bit":
##            pl="amd64"
##        else:
##            pl="win32"
##            return "build/exe.{}-{}".format(sys.platform, pyversion)
##    else:#linux
##        so="linux"
##        if platform.architecture()[0]=="64bit":
##            pl="x86_64"
##        else:
##            pl="i686"
##    return "build/exe.{}-{}-{}".format(so, pl, pyversion)
##    
##def filename_output():
##    if sys.platform=="win32":
##        so="windows"
##        if platform.architecture()[0]=="64bit":
##            pl="amd64"
##        else:
##            pl="win32"
##    else:#linux
##        so="linux"
##        if platform.architecture()[0]=="64bit":
##            pl="x86_64"
##        else:
##            pl="x86"
##    return "glparchis-{}-{}.{}".format(so,  version, pl)
##
##print ("Building for", sys.platform, version, winversion())
##name="glParchis"
##
###Add files for all platforms
##include_files=['sounds/', 'images/ficharoja.ico', 'GPL-3.txt']
##include_files.append(('i18n', 'i18n')) #include files puede ser tambien una tupla (origen,destino)
##
###Build options
##if sys.platform=='win32':
##        shutil.rmtree("build/", ignore_errors=True)
##        base = 'Win32GUI'     
##        include_files.append((PyQt5.__path__[0]+'/plugins/audio/qtaudio_windows.dll', 'audio/qtaudio_windows.dll' ))#Si no no sonaba en windows solo
##        include_files.append('glparchis.iss')
##        build_exe_options = dict(
##           create_shared_zip=False,
##           includes = ['OpenGL','OpenGL.platform.win32','OpenGL.arrays','OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.lists','OpenGL.converters','PyQt5.QtNetwork','PyQt5.QtWebKit','PyQt5.QtPrintSupport'],
##           excludes=[], 
##           include_files=include_files
##           )
##
##        options={
##      #'bdist_msi': build_msi_options,
##               'build_exe': build_exe_options
##               }
##               
##               
##               
##else:#linux
##        base="Console"
##        build_options = dict(
##           includes = ['OpenGL','OpenGL.platform.glx','OpenGL.arrays','OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.lists','OpenGL.converters','PyQt5.QtNetwork','PyQt5.QtWebKit','PyQt5.QtPrintSupport'],
##           excludes = [], 
##           include_files=include_files
##           )
##        options=dict(build_exe = build_options)
##
##executables = [
##      Executable('glparchis.py', base=base, icon='images/ficharoja.ico', shortcutName= name, shortcutDir='ProgramMenuFolder')
##]
##
##setup(name=name,
##      version = winversion(),
##      author = 'Mariano Muñoz',
##      description = 'Parcheesi Game',
##      options = options,
##      executables = executables)
##
##
###Post setup
##if sys.platform=="win32":
##    os.chdir(build_dir())
##    
##    inno="c:/Program Files (x86)/Inno Setup 5/ISCC.exe"
##    if platform.architecture()[0]=="32bit":
##        inno=inno.replace(" (x86)", "")
##    
##    subprocess.call([inno,  "/o../",  "/DVERSION_NAME={}".format(winversion()), "/DFILENAME={}".format(filename_output()),"glparchis.iss"], stdout=sys.stdout)
##else:   #Linux
##    print (build_dir(), filename_output(), os.getcwd())
##    pwd=os.getcwd()
##    os.chdir(build_dir())
##    print (build_dir(), filename_output(), os.getcwd())
##    os.system("tar cvz -f '{0}/build/{1}.tar.gz' * -C '{0}/{2}/'".format(pwd, filename_output(),  build_dir()))
##    
##    
    
from cx_Freeze import setup, Executable
import sys
sys.path.append('ui')
sys.path.append('images')
from libglparchis import version

print ("Building for", sys.platform, version())
name="glparchis"

#Add files
include_files=[ 'images/ficharoja.ico', 'GPL-3.txt']
include_files.append(("i18n/glparchis_es.qm", "i18n/glparchis_es.qm"))
include_files.append(("i18n/glparchis_fr.qm", "i18n/glparchis_fr.qm"))
include_files.append(("i18n/glparchis_ro.qm", "i18n/glparchis_ro.qm"))
include_files.append(("i18n/glparchis_ru.qm", "i18n/glparchis_ru.qm"))

#Build options
if sys.platform=='win32':
      #base = 'Win32GUI'
      base="Console"
      shortcut_table = [
          ("DesktopShortcut",        # Shortcut
           "DesktopFolder",          # Directory_
           "glParchis",     # Name
           "TARGETDIR",              # Component_
           "[TARGETDIR]glparchis.exe",   # Target
           None,                     # Arguments
           None,                     # Description
           None,                     # Hotkey
           None,                     # Icon
           None,                     # IconIndex
           None,                     # ShowCmd
           'TARGETDIR'               # WkDir
           ),

          ("StartupShortcut",        # Shortcut
           "StartupFolder",          # Directory_
           "glParchis",     # Name
           "TARGETDIR",              # Component_
           "[TARGETDIR]glparchis.exe",   # Target
           None,                     # Arguments
           None,                     # Description
           None,                     # Hotkey
           None,                     # Icon
           None,                     # IconIndex
           None,                     # ShowCmd
           'TARGETDIR'               # WkDir
           ),
      ]

      msi_data = {"Shortcut": shortcut_table}  # This will be part of the 'data' option of bdist_msi
      build_msi_options = {
           'upgrade_code': '{3849730B-2375-4F76-B4A5-A6677A23AB9B}',
           'add_to_path': False,
           'initial_target_dir': r'[ProgramFilesFolder]\%s' % (name),
           'data': msi_data
            }
 
      build_exe_options = dict(includes = [],excludes=[], include_files=include_files)
      options={'bdist_msi': build_msi_options, 'build_exe': build_exe_options}

else:#linux
      base="Console"
      build_options = dict(includes = [], excludes = [], include_files=include_files)
      options=dict(build_exe = build_options)

executables = [
      Executable('glparchis.py', base=base, icon='images/ficharoja.ico', shortcutName= name, shortcutDir='ProgramMenuFolder')
]

setup(name=name,
      version = version(),
      author = 'Mariano Muñoz',
      author_email="turulomio@yahoo.es", 
      description = 'Parchessi game',
      options = options,
      url="https://sourceforge.net/projects/glparchis/", 
      executables = executables)
