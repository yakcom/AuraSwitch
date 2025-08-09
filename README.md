# AuraSwitch

**AuraSwitch** — программа для Windows, которая автоматически меняет цвет подсветки клавиатуры в зависимости от текущей раскладки (RU/EN и т.д.).

## Возможности
- Автосмена цвета при смене языка ввода  
- Настройка цветов в файле `config.ini`  
- Работает в фоне, иконка в трее  

## Установка
1. Скачайте последнюю версию в разделе **[Releases](https://github.com/yakcom/AuraSwitch/releases)**.  
2. Запустите `AuraSwitch.exe`.  
3. При первом запуске появится `config.ini` — укажите в нём цвета для раскладок.  

## Запуск из исходников
```bash
git clone https://github.com/yakcom/AuraSwitch.git
cd AuraSwitch
pip install -r requirements.txt
python main.py
```

## Настройка
Пример `config.ini`:
```ini
[Layouts]
en = #00D084
ru = #1E90FF
```

## Требования
- Windows 10/11  
- Python 3.10+ (только для запуска из исходников)  
