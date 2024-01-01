import json
def loadData(file):
    with open(file, 'r') as json_file:
        loaded_data = json.load(json_file)
    return loaded_data
def saveData(t_data,filepath):
    with open(filepath, 'w') as json_file:
        json.dump(t_data, json_file, indent=4)
        