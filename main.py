import json


def load_data(file_path):
    """
    Loads JSON file.
    :param file_path: path to the JSON file
    :return: JSON data as string
    """
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)

    except FileNotFoundError as error:
        print(f"Error: File {file_path} is not found.\n{error}")
    except json.JSONDecodeError as error:
        print(f"Error: JSON {file_path} is not valid.\n{error}")
    except Exception as error:
        print(f"Error: Unexpected error at reading {file_path}.\n{error}")
    return None


def get_string_with_animals(animals_data):
    """
    Gets the single string with predefined animal data.
    :param animals_data: JSON formatted animal data.
    :return: string with predefined animal data.
    """
    output_animals_data = ""

    for animal in animals_data:
        # spare one if check later
        characteristic_is_there = False

        # append information to each string
        output_animals_data += "<li class='cards__item'>"

        if "name" in animal.keys():
            output_animals_data += f"Name: {animal['name']}<br/>\n"

        if "characteristics" in animal.keys():
            characteristic_is_there = True
            if "diet" in animal["characteristics"]:
                diet = animal["characteristics"]["diet"]
                output_animals_data += f"Diet: {diet}<br/>\n"

        if "locations" in animal.keys():
            first_location = animal["locations"][0]
            output_animals_data += f"Locations: {first_location}<br/>\n"

        if characteristic_is_there:
            if "type" in animal["characteristics"]:
                type_of_animal = animal["characteristics"]["type"]
                output_animals_data += f"Type: {type_of_animal}<br/>\n"
        output_animals_data += "</li>"
        output_animals_data += "\n"

    return output_animals_data


def get_html():
    """
    Reads the content of the HTML file.
    :return: Content of the HTML file.
    """
    try:
        file_name = "animals_template.html"
        with open(file_name, "r") as html_file:
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
        with open(file_name, "w") as html_file:
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
        string_with_animals = get_string_with_animals(animals_data)
        html_text = get_html()
        working_html_text = html_text # work with a copy and don't touch the original
        html_text_replaced = replace_html_with_animals(working_html_text, string_with_animals)
        write_html(html_text_replaced)
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()