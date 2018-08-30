import os
import json


def load_json_file(file_dir):
    if os.path.exists(file_dir):
        with open(file_dir) as f:
                return json.load(f)
    else:
        return False

def create_json_file(file_dir, payload):
    data = {}
    for key, value in payload.items():
        data[key] = value

    jsonFile = open(file_dir, "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

def update_json_file(file_name, payload):
    jsonFile = open(file_name, "r") # Open the JSON file for reading
    data = json.load(jsonFile) # Read the JSON into the buffer
    jsonFile.close() # Close the JSON file
    for key, value in payload.items():
        data[key] = value
    jsonFile = open(file_name, "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()