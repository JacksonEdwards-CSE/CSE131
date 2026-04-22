import json

def write_data_to_json_file(data, filename):
    '''Write the data contained in data to the json file with the name of filename.
    Catch exceptions if file cannot be found'''
    try:
        with open(filename, 'wt') as filehandle:
            json_data = json.dumps(data)
            filehandle.write(json_data)

    except (FileExistsError, FileNotFoundError):
        print("File not found")

def read_data_from_json_file(filename):
    try:
        with open(filename, 'rt') as filehandle:
            json_data = filehandle.read()

            dictionary_data = json.loads(json_data)

            return dictionary_data

    except (FileExistsError, FileNotFoundError):
        print("File not found")

def get_total_debts(debts):
    total = sum(debts)
    return total

def main():
    my_friends = {
        "Names" : ['bob', 'Betty', 'Jeannie'],
        "Phone Numbers" : [2085551111, 2085551212, 2088675309],
        "Addresses" : ["555 Cherry Lane", "123 Bob Lane", '867 Tuple Lane'],
        "Debts" : [123.45, 435.12, -20]
    }

    filename = "myfriends.json"

    write_data_to_json_file(my_friends, filename)

    my_friends2 = read_data_from_json_file(filename)

    print(my_friends2["Names"])
    print(my_friends2["Phone Numbers"])
    print(my_friends2["Addresses"])
    print(my_friends2["Debts"])

    total_debts = get_total_debts(my_friends2["Debts"])

    print(total_debts)

if __name__ == "__main__":
    main()