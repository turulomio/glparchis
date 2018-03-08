from cx_Freeze import setup, Executable
import sys
sys.path.append('ui')
sys.path.append('images')
from libglparchis import version

print ("Building for", sys.platform, version())
name="glparchis"

#Add files
include_files=['sounds/','images/ficharoja.ico', 'GPL-3.txt']
include_files.append(("i18n/glparchis_es.qm", "i18n/glparchis_es.qm"))
include_files.append(("i18n/glparchis_en.qm", "i18n/glparchis_en.qm"))
include_files.append(("i18n/glparchis_fr.qm", "i18n/glparchis_fr.qm"))
include_files.append(("i18n/glparchis_ro.qm", "i18n/glparchis_ro.qm"))
include_files.append(("i18n/glparchis_ru.qm", "i18n/glparchis_ru.qm"))

#Build options
if sys.platform=='win32':
      base = 'Win32GUI'
      #base="Console"
      import PyQt5
      include_files.append((PyQt5.__path__[0] + "/Qt/plugins/audio/qtaudio_windows.dll","audio/qtaudio_windows.dll"))
      include_files.append((PyQt5.__path__[0] + "/Qt/bin/QtWebEngineProcess.exe","QtWebEngineProcess.exe"))
      include_files.append((PyQt5.__path__[0] + "/Qt/resources/icudtl.dat","icudtl.dat"))
      include_files.append((PyQt5.__path__[0] + "/Qt/resources/qtwebengine_resources.pak","qtwebengine_resources.pak"))
      include_files.append((PyQt5.__path__[0] + "/Qt/resources/qtwebengine_resources_100p.pak","qtwebengine_resources_100p.pak"))
      include_files.append((PyQt5.__path__[0] + "/Qt/resources/qtwebengine_resources_200p.pak","qtwebengine_resources_200p.pak"))
      include_files.append((PyQt5.__path__[0] + "/Qt/translations/qtwebengine_locales/es.pak","qtwebengine_locales/es.pak"))

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
           "TARGETDIR"               # WkDir
           ),
          ("ProgramMenuShortcut",        # Shortcut
           "ProgramMenuFolder",          # Directory_
           "glParchis",     # Name
           "TARGETDIR",              # Component_
           "[TARGETDIR]glparchis.exe",   # Target
           None,                     # Arguments
           None,                     # Description
           None,                     # Hotkey
           None,                     # Icon
           None,                     # IconIndex
           None,                     # ShowCmd
           "TARGETDIR"               # WkDir
           ),
      ]

      msi_data = {"Shortcut": shortcut_table}  # This will be part of the 'data' option of bdist_msi
      build_msi_options = {
           'upgrade_code': '{3849730B-2375-4F76-B4A5-A6677A23AB9B}',
           'add_to_path': False,
           'initial_target_dir': r'[ProgramFilesFolder]\glparchis',
           'data': msi_data
            }
      build_exe_options = dict(
           includes = ['OpenGL','OpenGL.platform.win32','OpenGL.arrays','OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.lists','OpenGL.converters','OpenGL.GLU','OpenGL.GLU.glustruct','PyQt5.QtNetwork','PyQt5.QtWebEngineCore','PyQt5.QtWebChannel','PyQt5.QtPrintSupport', 'PyQt5.QtMultimedia','PyQt5.QtWebEngineWidgets'],
           excludes=[],
           zip_include_packages=["*"],
           zip_exclude_packages=[],
           include_files=include_files,
           )

      options={'bdist_msi': build_msi_options, 'build_exe': build_exe_options}

else:#linux
      base="Console"
      build_options = dict(
           includes = ['OpenGL','OpenGL.platform.glx','OpenGL.arrays','OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.lists','OpenGL.converters','PyQt5.QtNetwork','PyQt5.QtPrintSupport', 'OpenGL.GLU.glustruct'],
           excludes = [], 
           include_files=include_files
           )
      options=dict(build_exe = build_options)

executables = [
      Executable('glparchis.py', base=base, icon='images/ficharoja.ico')
]

setup(name=name,
      version = version(),
      author = 'Mariano Muñoz',
      author_email="turulomio@yahoo.es", 
      description = 'GPL Parchessi',
      options = options,
      url="https://sourceforge.net/projects/glparchis/", 
      executables = executables)
