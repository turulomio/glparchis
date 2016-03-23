@ECHO ON
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/frmAbout.ui -o ui/Ui_frmAbout.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/frmHelp.ui -o ui/Ui_frmHelp.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/frmInitGame.ui -o ui/Ui_frmInitGame.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/frmMain.ui -o ui/Ui_frmMain.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/frmSettings.ui -o ui/Ui_frmSettings.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/frmShowCasilla.ui -o ui/Ui_frmShowCasilla.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/frmShowFicha.ui -o ui/Ui_frmShowFicha.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/wdgPlayerDado.ui -o ui/Ui_wdgPlayerDado.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/wdgPlayer.ui -o ui/Ui_wdgPlayer.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/wdgUserPanel.ui -o ui/Ui_wdgUserPanel.py
call c:\Python34\Lib\site-packages\PyQt5\pyuic5.bat ui/wdgGame.ui -o ui/Ui_wdgGame.py
call c:\Python34\Lib\site-packages\PyQt5\pyrcc5.exe  images/glparchis.qrc -o images/glparchis_rc.py
call c:\Python34\Lib\site-packages\PyQt5\pylupdate5.exe -noobsolete glparchis.pro
call c:\Python34\Lib\site-packages\PyQt5\lrelease.exe glparchis.pro

