DESTDIR ?= /usr

PREFIXBIN=$(DESTDIR)/bin
PREFIXLIB=$(DESTDIR)/lib/glparchis
PREFIXSHARE=$(DESTDIR)/share/glparchis 
PREFIXSOUND=$(DESTDIR)/share/glparchis/sounds
PREFIXPIXMAPS=$(DESTDIR)/share/pixmaps
PREFIXAPPLICATIONS=$(DESTDIR)/share/applications

compile:
	pyuic4 ui/frmAbout.ui > ui/Ui_frmAbout.py
	pyuic4 ui/frmHelp.ui > ui/Ui_frmHelp.py
	pyuic4 ui/frmInitGame.ui > ui/Ui_frmInitGame.py
	pyuic4 ui/frmMain.ui > ui/Ui_frmMain.py
	pyuic4 ui/frmSettings.ui > ui/Ui_frmSettings.py
	pyuic4 ui/frmShowCasilla.ui > ui/Ui_frmShowCasilla.py
	pyuic4 ui/frmShowFicha.ui > ui/Ui_frmShowFicha.py
	pyuic4 ui/wdgPlayerDado.ui > ui/Ui_wdgPlayerDado.py
	pyuic4 ui/wdgPlayer.ui > ui/Ui_wdgPlayer.py
	pyuic4 ui/wdgUserPanel.ui > ui/Ui_wdgUserPanel.py
	pyuic4 ui/wdgGame.ui > ui/Ui_wdgGame.py
	pyrcc4 -py3 images/glparchis.qrc > images/glparchis_rc.py
	pylupdate4 -noobsolete glparchis.pro
	lrelease glparchis.pro

install:
	install -o root -d $(PREFIXBIN)
	install -o root -d $(PREFIXLIB)
	install -o root -d $(PREFIXSHARE)
	install -o root -d $(PREFIXSOUND)
	install -o root -d $(PREFIXPIXMAPS)
	install -o root -d $(PREFIXAPPLICATIONS)

	install -m 755 -o root glparchis.py $(PREFIXBIN)/glparchis
	install -m 644 -o root libglparchis.py $(PREFIXLIB)
	install -m 644 -o root ui/*.py $(PREFIXLIB)
	install -m 644 -o root images/*.py $(PREFIXLIB)
	install -m 644 -o root images/ficharoja.png $(PREFIXPIXMAPS)/glparchis.png
	install -m 644 -o root glparchis.desktop $(PREFIXAPPLICATIONS)
	install -m 644 -o root i18n/*.qm $(PREFIXSHARE)
	install -m 644 -o root AUTHORS-EN.txt AUTHORS-ES.txt CHANGELOG-EN.txt CHANGELOG-ES.txt GPL-3.txt INSTALL-EN.txt INSTALL-ES.txt RELEASES.txt $(PREFIXSHARE)
	install -m 644 -o root sounds/* $(PREFIXSOUND)
	install -m 644 -o root images/ficharoja.ico $(PREFIXSHARE)

uninstall:
	rm $(PREFIXBIN)/glparchis
	rm -Rf $(PREFIXLIB)
	rm -Rf $(PREFIXSHARE)
	rm -fr $(PREFIXPIXMAPS)/glparchis.png
	rm -fr $(PREFIXAPPLICATIONS)/glparchis.desktop



