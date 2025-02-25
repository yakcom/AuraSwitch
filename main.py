from configparser import *
from keyboard import *
from system import *
from time import *

Config=ConfigParser()
Config.read('config.ini')
vid, pid, iid = (int(Config.get('keyboard', key), 16) for key in ('vid', 'pid', 'iid'))
languages = {lang: [int(x, 16) for x in Config.get('languages', lang).split(',')] for lang in ('ru', 'en')}

kb = Keyboard(vid,pid)

lang = None
while True:
    sleep(0.01)
    if lang==get_lang():continue
    lang = get_lang()
    kb.send(languages[lang], iid)



