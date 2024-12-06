from ast import literal_eval
import csv
from datetime import datetime

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


def get_month_name_and_date(date : str) -> str:

    # taking a date formate and providing the month name and year
    date_in_list = date.split("-")

    test_date = datetime(int(date_in_list[0]),int(date_in_list[1]),int(date_in_list[2]))

    month_name = test_date.strftime("%B")

    return str(month_name + " " +date_in_list[2])

def color_text_red(text : str) -> str:

    # converting the text in the string red
    return "\033[91m{}\033[00m".format(text)

def color_text_cyan(text : str) -> str:

    # converting the text in the string cyan
    return "\033[96m{}\033[00m" .format(text)

def get_year_month(date : str) -> tuple:

    # converting the date into year and month
    date = date.split("/")

    if len(date) == 2:
        year = date[0]
        month = date[1]
    else:
        year = date[0]
        month = None

    return year, month
