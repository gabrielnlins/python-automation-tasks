import json

def get_data():
    with open(r"C:\Users\Gabri\game\src\python-automation-tasks\database.json", 'r') as file:
        return json.load(file)

def set_data(data):
    with open(r"C:\Users\Gabri\game\src\python-automation-tasks\database.json", 'w') as file:
        json.dump(data, file, indent=4)
