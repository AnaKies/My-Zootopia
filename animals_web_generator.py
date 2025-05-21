import json


def load_data(file_path):
    """
    Loads JSON file.
    :param file_path: path to the JSON file
    :return: JSON data as string
    """
    try:
        # use encoding for correct representation of such special symbols like an apostrophe
        with open(file_path, "r", encoding = "utf-8") as json_file:
            return json.load(json_file)

    except FileNotFoundError as error:
        print(f"Error: File {file_path} is not found.\n{error}")
    except json.JSONDecodeError as error:
        print(f"Error: JSON {file_path} is not valid.\n{error}")
    except Exception as error:
        print(f"Error: Unexpected error at reading {file_path}.\n{error}")
    return None


def serialize_animal(animal_obj):
    """
    Serializes a single animal to HTML
    :param animal_obj: dictionary with animal data
    :return: HTML string with animal data
    """
    output_animal_data = ""

    # spare one if check later
    characteristic_is_there = False

    # append information to each string
    output_animal_data += "<li class='cards__item'>\n"
    output_animal_data += "<div class='card__title'>"

    if "name" in animal_obj.keys():
        output_animal_data += f"{animal_obj['name']}"

    if "taxonomy" in animal_obj.keys():
        if "scientific_name" in animal_obj["taxonomy"].keys():
            scientific_name = animal_obj["taxonomy"]["scientific_name"]
            output_animal_data += f" ({scientific_name})"

    output_animal_data += "</div>\n"

    output_animal_data += "<div class='card__text'><ul class='animal_list'>"
    if "characteristics" in animal_obj.keys():
        characteristic_is_there = True
        if "diet" in animal_obj["characteristics"].keys():
            diet = animal_obj["characteristics"]["diet"]
            output_animal_data += "<li class='animal_properties'><strong>Diet: </strong>"
            output_animal_data += f"{diet}</li>\n"

    if "locations" in animal_obj.keys():
        if animal_obj["locations"]:  # check if the list is not empty
            first_location = animal_obj["locations"][0]
            output_animal_data += "<li class='animal_properties'><strong>Location: </strong>"
            output_animal_data += f"{first_location}</li>\n"

    if characteristic_is_there:
        if "type" in animal_obj["characteristics"]:
            type_of_animal = animal_obj["characteristics"]["type"]
            output_animal_data += "<li class='animal_properties'><strong>Type: </strong>"
            output_animal_data += f"{type_of_animal}</li>\n"

        if "lifespan" in animal_obj["characteristics"]:
            lifespan = animal_obj["characteristics"]["lifespan"]
            output_animal_data += "<li class='animal_properties'><strong>Lifespan: </strong>"
            output_animal_data += f"{lifespan}</li>\n"

    output_animal_data += "</ul></div></li>\n"

    return output_animal_data


def add_animals_to_html(animals_data):
    """
    Add to the given HTML the animal data.
    :param animals_data: JSON formatted animal data.
    :return: String with predefined animal data.
    """
    output_animals_data = ""

    for animal in animals_data:
        output_animals_data += serialize_animal(animal)

    return output_animals_data


def get_html():
    """
    Reads the content of the HTML file.
    :return: Content of the HTML file.
    """
    try:
        file_name = "animals_template.html"
        # use encoding for correct representation of such special symbols like an apostrophe
        with open(file_name, "r", encoding = "utf-8") as html_file:
            return html_file.read()

    except FileNotFoundError as error:
        print(f"Error: File {file_name} is not found.\n{error}")
    except json.JSONDecodeError as error:
        print(f"Error: JSON {file_name} is not valid.\n{error}")
    except Exception as error:
        print(f"Error: Unexpected error at reading {file_name}.\n{error}")
    return None

def write_html(html_content):
    """
    Writes the content of the HTML file to the HTML file.
    :param html_content: HTML content of the HTML file as string.
    :return: None
    """
    try:
        file_name = "animals.html"
        # use encoding for correct representation of such special symbols like an apostrophe
        with open(file_name, "w", encoding = "utf-8") as html_file:
            html_file.write(html_content)

    except FileNotFoundError as error:
        print(f"Error: File {file_name} is not found.\n{error}")
    except json.JSONDecodeError as error:
        print(f"Error: JSON {file_name} is not valid.\n{error}")
    except Exception as error:
        print(f"Error: Unexpected error at writing {file_name}.\n{error}")


def replace_html_with_animals(html_text, string_with_animals):
    """
    Replaces HTML content with animal data.
    :param html_text: The HTML content of the HTML file as string.
    :param string_with_animals: Text to be replaced with the animal data.
    :return: string with replaced HTML content.
    """
    if "__REPLACE_ANIMALS_INFO__" in html_text:
        html_text_replaced = html_text.replace(
                                    "__REPLACE_ANIMALS_INFO__",
                                    string_with_animals)
        return html_text_replaced
    else:
        raise Exception("Error: the __REPLACE_ANIMALS_INFO__ is not in the template.")


def main():
    try:
        animals_data = load_data("animals_data.json")
        string_with_animals = add_animals_to_html(animals_data)
        html_text = get_html()
        working_html_text = html_text # work with a copy and don't touch the original
        html_text_replaced = replace_html_with_animals(working_html_text, string_with_animals)
        write_html(html_text_replaced)
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()