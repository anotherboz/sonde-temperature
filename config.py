import json

def load():
    global __config
    try:
        file = open('config.json')
        __config = json.load(file)
        file.close()
    except:
        __config = {'ssid': '', 'password': '', 'server': ''}
    return __config.copy()

def save():
    global __config
    file = open('config.json', 'w')
    json.dump(__config, file)
    file.flush()
    file.close()

def get():
    return __config.copy()

def set(c):
    global __config
    __config = c

__config = load_config()
