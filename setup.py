from cx_Freeze import setup, Executable
import sys
import os 
sys.path.append('ui')
sys.path.append('images')
from libglparchis import version

def winversion():
    versio=version.replace("+","")
    return versio[:-4]+"."+versio[4:-2]+"."+versio[6:]

print ("Building for", sys.platform, version, winversion())
name="glParchis"

#Add files
include_files=['sounds/', 'images/ficharoja.ico', 'GPL-3.txt']
for f in os.listdir('i18n/'):#adding qm
      if f[len(f)-3:]==".qm":
            include_files.append('i18n/'+f)
            print (f)

#Build options
if sys.platform=='win32':
      base = 'Win32GUI'
      version=winversion()
#      build_msi_options = {
#           'upgrade_code': '{3849730B-2375-4F76-B4A5-A6677A23AB9B}',
#           'add_to_path': False,
#           'initial_target_dir': r'[ProgramFilesFolder]\%s' % (name),
#            }

      build_exe_options = dict(
           create_shared_zip=False,
           includes = ['OpenGL','OpenGL.platform.win32','OpenGL.arrays','OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.lists','OpenGL.converters'],
           excludes=[], 
           include_files=include_files
           )

      options={
      #'bdist_msi': build_msi_options,
               'build_exe': build_exe_options
               }
else:#linux
      base="Console"
      build_options = dict(
           includes = ['OpenGL','OpenGL.platform.glx','OpenGL.arrays','OpenGL.arrays.ctypesarrays', 'OpenGL.arrays.lists','OpenGL.converters','PyQt5.QtNetwork'], 
           excludes = [], 
           include_files=include_files
           )
      options=dict(build_exe = build_options)

executables = [
      Executable('glparchis.py', base=base, icon='images/ficharoja.ico', shortcutName= name, shortcutDir='ProgramMenuFolder')
]

setup(name=name,
      version = version,
      author = 'Mariano Muñoz',
      description = 'Parcheesi Game',
      options = options,
      executables = executables)

