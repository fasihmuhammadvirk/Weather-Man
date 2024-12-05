from ast import literal_eval
import csv

def clean_and_convert_dic(dic:dict) -> dict:

    """
    Processes a dictionary by removing spaces and slashes from keys and converting values to appropriate data types.

    Args:
        dic (dict): The input dictionary with keys and values as strings.

    Returns:
        dict: A new dictionary with formatted keys and converted values.
    """

    formated_dic = {}

    for key, value in dic.items():

        # removing space from start and end also replacing spaces b/w words into dashes `_`
        new_key = key.strip().replace(" ", "_").replace("/", "").lower()

        # converting into appropriate data type
        if value.isdigit():
            # converting each value to its desire datatype
            formated_dic[new_key] = literal_eval(value.strip())
        else:
            if value == "":
                formated_dic[new_key] = 0
            else:
                formated_dic[new_key] = value

    return formated_dic

def read_file_data(path : str , file_name : str) -> object:

    """
    Reads data from a CSV file and returns it as a dictionary-like object.

    Args:
        path (str): The directory path where the file is located.
        file_name (str): The name of the file to be read.

    Returns:
        object: A CSV reader object that iterates over lines in the given file as dictionaries.
    """

    # opening the file by given path and filename
    file = open(f'{path + "/" + file_name}', mode='r')

    # reading the data of the file
    file_data_as_dictionary = csv.DictReader(file)

    return file_data_as_dictionary


