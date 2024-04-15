import json


def load_person_data():
    # Opening JSON file
    file = open('person_db.json') # old: 'data/person_db.json"
    # Loading the JSON File in a dictionary
    person_data = json.load(file)
    return person_data


def get_person_list(person_data):
    name_list = []
    for person in person_data:
        name_list.append(person["lastname"] + " " + person["firstname"])
    return name_list







