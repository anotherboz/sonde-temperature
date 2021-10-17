import json

def loadConfig():
    global config
    try:
        file = open('config.json')
        config = json.load(file)
        file.close()
    except:
        config = {'ssid': '', 'password': '', 'server': ''}

def saveConfig():
    global config
    file = open('config.json', 'w')
    json.dump(config, file)
    file.flush()
    file.close()

def getConfig():
    return config

def setConfig(c):
    global config
    config = c

config = loadConfig()
