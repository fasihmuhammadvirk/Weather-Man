import sys
from ast import literal_eval
from datetime import datetime
from os import listdir

def clean_and_convert_dic(dic : dict) -> dict:

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

        # removing . and - (minus) sign from values to check the digits
        if value.strip("-").replace(".","").isdigit():

            # converting each value to its desire datatype
            formated_dic[new_key] = literal_eval(value.strip())
        else:
            if value.strip() == "":
                formated_dic[new_key] = 0
            else:
                formated_dic[new_key] = value

    return formated_dic

def color_text_red(text : str) -> str:

    # converting the text in the string red
    return "\033[91m{}\033[00m".format(text)

def color_text_cyan(text : str) -> str:

    # converting the text in the string cyan
    return "\033[96m{}\033[00m" .format(text)

def get_month_name_and_date_str(date : str) -> str:

    # taking a date formate and providing the month name and year
    date_in_list = date.split("-")
    test_date = datetime(int(date_in_list[0]) , int(date_in_list[1]) , int(date_in_list[2]))
    month_name = test_date.strftime("%B")

    return str(month_name + " " + date_in_list[2])

def get_max_min_year_in_filedata() -> dict:

    path = sys.argv[1]
    list_of_file_names = listdir(path)
    maximum_and_minimum_year_dic = dict()
    maximum_and_minimum_year_dic['maximum_year'] = ''
    maximum_and_minimum_year_dic['minimum_year'] = list_of_file_names[0]

    for filename_with_year in list_of_file_names:

        # getting the year from the name of the file
        year = filename_with_year.split('_')[2]

        if year > maximum_and_minimum_year_dic['maximum_year']:
            maximum_and_minimum_year_dic['maximum_year'] = year

        if year < maximum_and_minimum_year_dic['minimum_year']:
            maximum_and_minimum_year_dic['minimum_year'] = year

    return maximum_and_minimum_year_dic
