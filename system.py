import ctypes
import ctypes
import collections

langs = {68748313: "ru", 67699721: "en"}
buffer_size = 5
lang_buffer = collections.deque(maxlen=buffer_size)


def get_lang():
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    thread = user32.GetWindowThreadProcessId(hwnd, None)
    layout = user32.GetKeyboardLayout(thread)
    lang = langs.get(layout)

    if lang:
        lang_buffer.append(lang)

    if len(lang_buffer) == buffer_size:
        return max(set(lang_buffer), key=lang_buffer.count)
    return lang
