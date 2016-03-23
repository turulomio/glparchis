call Makefile.bat
c:/python34/python.exe setup.py build_exe
###### binaries windows
#DIR=build/exe.win32-$PYTHONVERSION
#mkdir -p $DIR
copy glparchis.iss $DIR
cd $DIR
c:/Program\ Files\ \(x86\)/Inno\ Setup\ 5/ISCC.exe /o$CWD/dist /DVERSION_NAME=$VERSION glparchis.iss
