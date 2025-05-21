import json

from bs4 import BeautifulSoup


def load_data(file_path):
    """
    Loads json file.
    :param file_path:
    :return:
    """
    with open(file_path, "r") as json_file:
        return json.load(json_file)


def get_string_with_animals(animals_data):
    """
    Gets the single string with predefined animal data.
    :param animals_data: JSON formatted animal data.
    :return: string with predefined animal data.
    """
    output_animals_data = ""

    for animal in animals_data:
        characteristic_is_there = False # spare one if check later

        if "name" in animal.keys():
            output_animals_data += f"Name: {animal['name']}\n"

        if "characteristics" in animal.keys():
            characteristic_is_there = True
            if "diet" in animal["characteristics"]:
                diet = animal["characteristics"]["diet"]
                output_animals_data += f"Diet: {diet}\n"

        if "locations" in animal.keys():
            first_location = animal["locations"][0]
            output_animals_data += f"Locations: {first_location}\n"

        if characteristic_is_there:
            if "type" in animal["characteristics"]:
                type_of_animal = animal["characteristics"]["type"]
                output_animals_data += f"Type: {type_of_animal}\n"

        output_animals_data += "\n"

    return output_animals_data


def get_html():
    """
    Reads the content of the HTML file.
    :return: Content of the HTML file.
    """
    with open("animals_template.html", "r") as html_file:
        return html_file.read()


def main():
    animals_data = load_data("animals_data.json")
    string_with_animals = get_string_with_animals(animals_data)
    html_raw = get_html()
    html_raw.replace("__REPLACE_ANIMALS_INFO__", string_with_animals)


if __name__ == "__main__":
    main()