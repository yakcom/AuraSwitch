import ctypes

langs = {68748313: "ru", 67699721: "en"}

def get_lang():
    user32 = ctypes.windll.user32
    if not (hwnd := user32.GetForegroundWindow()): return
    thread = user32.GetWindowThreadProcessId(hwnd, None)
    layout = user32.GetKeyboardLayout(thread)
    return langs.get(layout)
