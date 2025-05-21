import json


def load_data(file_path):
    """
    Loads json file.
    :param file_path:
    :return:
    """
    with open(file_path, "r") as json_file:
        return json.load(json_file)


def print_animals(animals_data):
    """
    Prints the animal data.
    :param animals_data: json formatted animal data.
    :return: None
    """
    for animal in animals_data:
        characteristic_is_there = False # spare one if check later

        if "name" in animal.keys():
            print(f"Name: {animal['name']}")

        if "characteristics" in animal.keys():
            characteristic_is_there = True
            if "diet" in animal["characteristics"]:
                diet = animal["characteristics"]["diet"]
                print(f"Diet: {diet}")

        if "locations" in animal.keys():
            first_location = animal["locations"][0]
            print(f"Locations: {first_location}")

        if characteristic_is_there:
            if "type" in animal["characteristics"]:
                type_of_animal = animal["characteristics"]["type"]
                print(f"Type: {type_of_animal}")
        print()


def get_html():
    """
    Reads the content of the HTML file.
    :return: content of the HTML file.
    """
    with open("animals_template.html", "r") as html_file:
        return html_file.read()



def main():
    animals_data = load_data("animals_data.json")
    print_animals(animals_data)


if __name__ == "__main__":
    main()