from configparser import *
from keyboard import *
from system import *
from time import *
import threading
import tray

threading.Thread(target=tray.start).start()

old = None
while True:
    sleep(0.01)

    lang = get_lang()
    if not lang or lang==old:continue
    old = lang

    Config = ConfigParser()
    Config.read('config.ini')
    vid, pid, iid = (int(Config.get('keyboard', key), 16) for key in ('vid', 'pid', 'iid'))
    languages = {lang: [int(x, 16) for x in Config.get('languages', lang).split(',')] for lang in ('ru', 'en')}

    kb = Keyboard(vid, pid)
    kb.send(languages[lang], iid)



