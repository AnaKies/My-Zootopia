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
        output_animals_data += "<div class='card__title'>"

        if "name" in animal.keys():
            output_animals_data += f"{animal['name']}<br/>"
        output_animals_data += "</div>"

        output_animals_data += "<p class='card__text'>"
        if "characteristics" in animal.keys():
            characteristic_is_there = True
            if "diet" in animal["characteristics"]:
                diet = animal["characteristics"]["diet"]
                output_animals_data += "<strong>Diet: </strong>"
                output_animals_data += f"{diet}<br/>"

        if "locations" in animal.keys():
            if animal["locations"]:  # check if the list is not empty
                first_location = animal["locations"][0]
                output_animals_data += "<strong>Location: </strong>"
                output_animals_data += f"{first_location}<br/>"

        if characteristic_is_there:
            if "type" in animal["characteristics"]:
                type_of_animal = animal["characteristics"]["type"]
                output_animals_data += "<strong>Type: </strong>"
                output_animals_data += f"{type_of_animal}<br/>"
        output_animals_data += "</p>"
        output_animals_data += "</li>"

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


def add_utf8_to_html(html_text):
    """
    Adds UTF-8 to HTML content for the correct formatting of the HTML file.
    :param html_text: html content of the HTML file as string.
    :return: HTML content with <meta> tag in the head block
    """
    return html_text.replace("<head>", """<head>
        <meta charset=\"UTF-8\">""")


def main():
    try:
        animals_data = load_data("animals_data.json")
        string_with_animals = get_string_with_animals(animals_data)
        html_text = get_html()
        working_html_text = html_text # work with a copy and don't touch the original
        working_html_text = add_utf8_to_html(working_html_text)
        html_text_replaced = replace_html_with_animals(working_html_text, string_with_animals)
        write_html(html_text_replaced)
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()