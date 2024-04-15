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
        name_list.append(person["lastname"] + ", " + person["firstname"])
    return name_list

def find_person_data_by_name():
    suchstring  = "Huber, Julian"

    # Teilt einen String in und speichert die Ergebnisse in einer Liste
    two_names = suchstring.split(", ")
    vorname = two_names[1]
    nachname = two_names[0]

    person_data = load_person_data()

    # Nun können wir vergleichen bis wir einen Treffer finden
    for eintrag in person_data:
        if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
            print(eintrag)
    






