import json

def load_config():
    global __config
    try:
        file = open('config.json')
        __config = json.load(file)
        file.close()
    except:
        __config = {'ssid': '', 'password': '', 'server': ''}
    return __config.copy()

def save_config():
    global __config
    file = open('config.json', 'w')
    json.dump(__config, file)
    file.flush()
    file.close()

def get_config():
    return __config.copy()

def set_config(c):
    global __config
    __config = c

__config = load_config()
