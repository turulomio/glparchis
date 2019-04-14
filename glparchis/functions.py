import datetime
import warnings
import functools
import logging
import pkg_resources
import sys

from PyQt5.QtCore import Qt, QCoreApplication, QEventLoop
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from colorama import Style, Fore



def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)
    return new_func

## Swaps a list with tho items
## @param arr List to swap
def swap_list_with_two_items(arr):
    arr.append(arr[0])
    arr.pop(0)

def str2bool(s):
    if s.__class__==bool:#Si ya fuera bool
        return s
    if s.lower()=="true":
        return True
    if s.lower()=="false":
        return False
    print ("I coudn't convert string to boolean '{}'".format(s))
    
def bytes2bool(b):
    return str2bool(b2s(b))

def b2s(b, code='UTF-8'):
    return bytes(b).decode(code)
    
def s2b(s, code='UTF8'):
    if s==None:
        return "".encode(code)
    else:
        return s.encode(code)
        

def c2b(state):
    """QCheckstate to python bool"""
    if state==Qt.Checked:
        return True
    else:
        return False

def delay(miliseconds):
    dieTime= datetime.datetime.now()+datetime.timedelta(microseconds=miliseconds*1000)
    while datetime.datetime.now()< dieTime :
        QCoreApplication.processEvents(QEventLoop.AllEvents, 100);    
    #print ("Delay", miliseconds)
    
    
    
def signal_handler(signal, frame):
        logging.critical(Style.BRIGHT+Fore.RED+QApplication.translate("Core","You pressed 'Ctrl+C', exiting..."))
        sys.exit(1)
        
        
def cargarQTranslator(qtranslator, language):  
    """language es un string"""  

    url=pkg_resources.resource_filename("glparchis","i18n/glparchis_{}.qm".format(language))
    print(url)
    qtranslator.load(url)
    QCoreApplication.installTranslator(qtranslator);

def developing():
    """Funcion que permite avanzar si hay un parametro y da un aviso e interrumpe si no, se debe poner un if en donde se use"""
    if len (sys.argv)==1:
        qmessagebox(QApplication.translate("frmMain", "Esta opcion se esta desarrollando"))
        return False
    return True

def qmessagebox(message, type=QMessageBox.Information):
    m=QMessageBox()
    m.setWindowIcon(QIcon(":glparchis/ficharoja.png"))
    m.setIcon(type)
    m.setText(str(message))
    m.exec_() 
    
## Converts a bytes stream to a tuple of strings (command, [args])
## @param s bytes
## @return (command,args)
def command_split(s):
        s=b2s(s)
        arr=s.split(" ")
        return (arr[0], arr[1:])
