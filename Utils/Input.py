import json

def getData():
    with open('input.json') as json_file:
        json_data = json.load(json_file)
    return json_data
