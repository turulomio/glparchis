#!/usr/bin/python3
import argparse
import datetime
import os
import sys
sys.path.append("ui")
import platform
from subprocess import call, check_call
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from libglparchis import version

def shell(*args):
    print(" ".join(args))
    call(args,shell=True)

def build_dir():
    pyversion="{}.{}".format(sys.version_info[0], sys.version_info[1])
    if sys.platform=="win32":
        so="win"
        if platform.architecture()[0]=="64bit":
            pl="amd64"
        else:
            pl="win32"
            return "build/exe.{}-{}".format(sys.platform, pyversion)
    else:#linux
        so="linux"
        if platform.architecture()[0]=="64bit":
            pl="x86_64"
        else:
            pl="i686"
    return "build/exe.{}-{}-{}".format(so, pl, pyversion)
    
def filename_output():
    if sys.platform=="win32":
        so="windows"
        if platform.architecture()[0]=="64bit":
            pl="amd64"
        else:
            pl="win32"
    else:#linux
        so="linux"
        if platform.architecture()[0]=="64bit":
            pl="x86_64"
        else:
            pl="x86"
    return "glparchis-{}-{}.{}".format(so,  version(), pl)
    


if __name__ == '__main__':
    start=datetime.datetime.now()
    parser=argparse.ArgumentParser(prog='Makefile.py', description='Makefile in python', epilog="Developed by Mariano Muñoz", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--doc', help="Generate docs and i18n",action="store_true",default=False)
    parser.add_argument('--compile', help="App compilation",action="store_true",default=False)
    parser.add_argument('--compile_windows', help="Make a Windows binary compilation", action="store_true",default=False)
    parser.add_argument('--compile_images', help="App images compilation",action="store_true",default=False)
    parser.add_argument('--destdir', help="Directory to install",action="store",default="/")
    parser.add_argument('--uninstall', help="Uninstall",action="store_true",default=False)
    parser.add_argument('--dist_sources', help="Make a sources tar", action="store_true",default=False)
    parser.add_argument('--dist_linux', help="Make a Linux binary distribution", action="store_true",default=False)
    parser.add_argument('--dist_windows', help="Make a Windows binary distribution", action="store_true",default=False)
    parser.add_argument('--python', help="Python path", action="store",default='/usr/bin/python3')
    args=parser.parse_args()

    prefixbin=args.destdir+"/usr/bin"
    prefixlib=args.destdir+"/usr/lib/glparchis"
    prefixshare=args.destdir+"/usr/share/glparchis"
    prefixpixmaps=args.destdir+"/usr/share/pixmaps"
    prefixapplications=args.destdir+"/usr/share/applications"
    prefixman=args.destdir+"/usr/share/man"
    prefixsounds=args.destdir+"/usr/share/glparchis/sounds"

    if ( "--dist_windows" in sys.argv or "--compile_windows" in sys.argv )  and platform.system()!="Windows":
        print("You need to be in Windows to pass this parameters")
        sys.exit(1)
    elif "--dist_windows" not in sys.argv and platform.system=="Windows":#In windows only dist_windows
        print("You need to be in Linux to pass this parameters")
        sys.exit(1)


    if args.doc==True:
        shell("pylupdate5 -noobsolete -verbose glparchis.pro")
        shell("lrelease -qt5 glparchis.pro")
    elif args.uninstall==True:
        shell("rm " + prefixbin + "/glparchis*")
        shell("rm -Rf " + prefixlib)
        shell("rm -Rf " + prefixshare)
        shell("rm -fr " + prefixpixmaps + "/glparchis.png")
        shell("rm -fr " + prefixapplications +"/glparchis.desktop")
    elif args.dist_sources==True:
        shell("{} setup.py sdist".format(args.python))
    elif args.dist_linux==True:
        shell("{} setup.py build_exe".format(args.python))    
        print (build_dir(), filename_output(), os.getcwd())
        pwd=os.getcwd()
        try:
            os.makedirs(build_dir())
        except:
            pass
        os.chdir(build_dir())
        print (build_dir(), filename_output(), os.getcwd())
        os.system("tar cvz -f '{0}/dist/{1}.tar.gz' * -C '{0}/'".format(pwd, filename_output()))#,  build_dir()))
    elif args.compile_windows==True:
        check_call([sys.executable, "setup.py","build exe"])
    elif args.dist_windows==True:
        check_call([sys.executable, "setup.py","bdist_msi"])
    elif args.compile==True:
        futures=[]
        with ProcessPoolExecutor(max_workers=cpu_count()+1) as executor:
            futures.append(executor.submit(shell, "pyuic5 ui/frmAbout.ui -o ui/Ui_frmAbout.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/frmHelp.ui -o ui/Ui_frmHelp.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/frmInitGame.ui -o ui/Ui_frmInitGame.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/frmMain.ui -o ui/Ui_frmMain.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/frmSettings.ui -o ui/Ui_frmSettings.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/frmShowCasilla.ui -o ui/Ui_frmShowCasilla.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/frmShowFicha.ui -o ui/Ui_frmShowFicha.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/wdgPlayerDado.ui -o ui/Ui_wdgPlayerDado.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/wdgPlayer.ui -o ui/Ui_wdgPlayer.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/wdgUserPanel.ui -o ui/Ui_wdgUserPanel.py"))
            futures.append(executor.submit(shell, "pyuic5 ui/wdgGame.ui -o ui/Ui_wdgGame.py"))
    elif args.compile_images==True:
            shell("pyrcc5 images/glparchis.qrc -o images/glparchis_rc.py")
    else:
        shell("install -o root -d "+ prefixbin)
        shell("install -o root -d "+ prefixlib)
        shell("install -o root -d "+ prefixshare)
        shell("install -o root -d "+ prefixpixmaps)
        shell("install -o root -d "+ prefixapplications)
        shell("install -o root -d "+ prefixsounds)
        shell("install -o root -d "+ prefixman+"/man1")
        shell("install -o root -d "+ prefixman+"/es/man1")
        shell("install -o root -d "+ prefixman+"/fr/man1")
        shell("install -o root -d "+ prefixman+"/ro/man1")
        shell("install -o root -d "+ prefixman+"/ru/man1")

        shell("install -m 755 -o root glparchis.py "+ prefixbin+"/glparchis")
        shell("install -m 644 -o root ui/*.py libglparchis.py images/*.py "+ prefixlib)
        shell("install -m 644 -o root i18n/*.qm " + prefixlib)
        shell("install -m 644 -o root glparchis.desktop "+ prefixapplications)
        shell("install -m 644 -o root images/ficharoja.png "+ prefixshare)
        shell("install -m 644 -o root sounds/* "+ prefixsounds)
        shell("install -m 644 -o root images/ficharoja.png "+ prefixpixmaps + "/glparchis.png")
        shell("install -m 644 -o root GPL-3.txt AUTHORS-EN.txt AUTHORS-ES.txt CHANGELOG-EN.txt CHANGELOG-ES.txt INSTALL-EN.txt INSTALL-ES.txt RELEASES.txt "+ prefixshare)
    print ("*** Process took {} using {} processors ***".format(datetime.datetime.now()-start , cpu_count()))

