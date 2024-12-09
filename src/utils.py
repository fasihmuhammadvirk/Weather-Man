from ast import literal_eval
import csv
from datetime import datetime
import os

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
        if value.strip("-").replace(".","").isdigit():

            # converting each value to its desire datatype
            formated_dic[new_key] = literal_eval(value.strip())

        else:

            if value == "" or value == " ":
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

    test_date = datetime(int(date_in_list[0]) , int(date_in_list[1]) , int(date_in_list[2]))

    month_name = test_date.strftime("%B")

    return str(month_name + " " + date_in_list[2])

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

def get_switch_and_date(list_of_switches_and_dates : list):

    index_to_find_date = 1
    for index_to_find_switch in range(0 , len(list_of_switches_and_dates) , 2):

        switch = list_of_switches_and_dates[index_to_find_switch]
        date = list_of_switches_and_dates[index_to_find_date]

        index_to_find_date += 2

        yield switch , date

def validate_switches_and_date(list_of_switches_and_dates : list ):

    if len(list_of_switches_and_dates)//2 > 3:
        print("Please Enter only three values of switch and date to get Report")
        return []

    if len(list_of_switches_and_dates) % 2 != 0:
        print("One of the Switch or Date is Missing")
        return []

    list_of_valid_switches = ['-e', '-a', '-c']
    index_to_find_date = 1
    for index_to_find_switch in range(0, len(list_of_switches_and_dates), 2):

        switch = list_of_switches_and_dates[index_to_find_switch]
        date = list_of_switches_and_dates[index_to_find_date]
        year , month = get_year_month(date)

        if switch in list_of_valid_switches:

            if switch == list_of_valid_switches[0] and month is not None:
                print(print(f"{switch} This switch date should not contain value of month"))
                return []

            elif switch == list_of_valid_switches[1] and month is None:
                print(print(f"{switch} This switch date should contain value of month"))
                return []

            elif switch == list_of_valid_switches[2] and month is None:
                print(print(f"{switch} This switch date should contain value of month"))
                return []
        else:
            print(f"{switch} This is not a valid switch")
            return []

        index_to_find_date += 2

    return True

def validate_input(command_line_arguments):
    valid_path = command_line_arguments[0]

    if os.path.isdir(valid_path):

        is_switch_date_valid = validate_switches_and_date(command_line_arguments[1:])

        if is_switch_date_valid:
            return True
        else:
            return False
    else:

        print(f"There is no such Directory as {valid_path}")
        return False


def process_input(command_line_arguments):
    path = command_line_arguments[0]
    list_of_switches_and_date = command_line_arguments[1:]

    return path , list_of_switches_and_date