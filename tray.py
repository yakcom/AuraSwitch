from pystray import Icon, MenuItem, Menu
from PIL import Image
import os,threading

def exit_app(icon, item):
    icon.stop()
    os._exit(0)

def run_tray():
    menu = Menu(MenuItem('Выход', exit_app))
    tray_icon = Icon("TestIcon", Image.open("main.ico"), menu=menu)
    tray_icon.run()

threading.Thread(target=run_tray, daemon=True).start()