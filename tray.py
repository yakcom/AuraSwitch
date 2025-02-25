from pystray import Icon, MenuItem, Menu
from PIL import Image
import os,sys

def settings():
    os.startfile('config.ini')

def exit(icon, item):
    icon.stop()
    os._exit(0)

def icon(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)

def start():
    menu = Menu(MenuItem('Настройки', settings),MenuItem('Выход', exit))
    tray_icon = Icon("TestIcon", Image.open(icon("main.ico")), menu=menu)
    tray_icon.run()