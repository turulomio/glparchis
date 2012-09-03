DESTDIR ?= /


PREFIXBIN=$(DESTDIR)/usr/bin
PREFIXLIB=$(DESTDIR)/usr/lib/glparchis
PREFIXSHARE=$(DESTDIR)/usr/share/glparchis 
PREFIXSOUND=$(DESTDIR)/usr/share/glparchis/sounds
PREFIXPIXMAPS=$(DESTDIR)/usr/share/pixmaps
PREFIXAPPLICATIONS=$(DESTDIR)/usr/share/applications

all: compile install
compile:
	pyuic4 ui/frmAbout.ui > ui/Ui_frmAbout.py
	pyuic4 ui/frmInitGame.ui > ui/Ui_frmInitGame.py
	pyuic4 ui/frmMain.ui > ui/Ui_frmMain.py
	pyuic4 ui/frmSettings.ui > ui/Ui_frmSettings.py
	pyuic4 ui/frmShowCasilla.ui > ui/Ui_frmShowCasilla.py
	pyuic4 ui/frmShowFicha.ui > ui/Ui_frmShowFicha.py
	pyuic4 ui/wdgUserPanel.ui > ui/Ui_wdgUserPanel.py
	pyuic4 ui/wdgGame.ui > ui/Ui_wdgGame.py
	pyrcc4 images/glparchis.qrc > images/glparchis_rc.py
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
	install -m 644 -o root doc/glparchis-* $(PREFIXSHARE)
	install -m 644 -o root AUTHORS-EN.txt  AUTHORS-ES.txt  CHANGELOG-EN.txt  CHANGELOG-ES.txt  GPL-3.txt  INSTALL-EN.txt  INSTALL-ES.txt  RELEASES-EN.txt  RELEASES-ES.txt  $(PREFIXSHARE)
	install -m 644 -o root sounds/*.ogg $(PREFIXSOUND)

uninstall:
	rm $(PREFIXBIN)/glparchis
	rm -Rf $(PREFIXLIB)
	rm -Rf $(PREFIXSHARE)
	rm -fr $(PREFIXPIXMAPS)/glparchis.png
	rm -fr $(PREFIXAPPLICATIONS)/glparchis.desktop



