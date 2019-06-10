import json

def loadSettings():
    with open('settings.json') as config_file:
        data = json.load(config_file)
        return data
