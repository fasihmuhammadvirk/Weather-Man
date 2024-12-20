import os
import sys
from src.utils import get_max_min_year_in_filedata


def validate_date(date: str, switch: str) -> bool:
    max_and_min_year_in_data = get_max_min_year_in_filedata()
    maximum_year = max_and_min_year_in_data['maximum_year']
    minimum_year = max_and_min_year_in_data['minimum_year']
    month = None

    # checking if date contain month or not
    if len(date.split("/")) == 2:
        year, month = date.split("/")
    else:
        year = date

    # checking if the entered year and month is correct or not
    if int(maximum_year) >= int(year) >= int(minimum_year):
        # if month the switches are either -a or -c
        if month is not None and 12 >= int(month) >= 1 and switch != '-e':
            return True
        elif month is None and switch == '-e':
            return True
        else:
            return False
    # if the year is not correct
    else:
        return False


def validate_switch(switch: str) -> bool:
    list_of_valid_switches = ['-e', '-a', '-c']

    if switch in list_of_valid_switches:
        return True
    else:
        return False


def validate_switches_and_date(list_of_switches_and_dates: list) -> bool:
    is_switch_date_valid = False

    for index_switch_in_list in range(0, len(list_of_switches_and_dates), 2):

        # getting value of each switch and its date -> [switch , date]
        switch = list_of_switches_and_dates[index_switch_in_list]
        date = list_of_switches_and_dates[index_switch_in_list + 1]  # as date is in the next index to switch

        is_switch_valid = validate_switch(switch)
        is_date_valid = validate_date(date, switch)

        if is_switch_valid and is_date_valid:
            is_switch_date_valid = True
        else:
            return False

    return is_switch_date_valid


def validate_input() -> dict:
    input_values_and_validations_dict = dict()
    input_values_and_validations_dict['path'] = sys.argv[1]
    input_values_and_validations_dict['list_of_switch_date'] = sys.argv[2:]

    length_of_switch_date_list = len(input_values_and_validations_dict['list_of_switch_date'])

    # validating length and uneven pairs
    if length_of_switch_date_list > 6 or length_of_switch_date_list not in [2, 4, 6]:
        input_values_and_validations_dict['is_valid'] = False
        return input_values_and_validations_dict

    # validating path
    if os.path.isdir(input_values_and_validations_dict['path']):
        # validate switches and date
        is_switch_date_valid = validate_switches_and_date(input_values_and_validations_dict['list_of_switch_date'])

        if is_switch_date_valid:
            input_values_and_validations_dict['is_valid'] = True
            return input_values_and_validations_dict

        else:
            input_values_and_validations_dict['is_valid'] = False
            return input_values_and_validations_dict

    else:
        print(f"There is no such Directory as {input_values_and_validations_dict['path']}")
        input_values_and_validations_dict['is_valid'] = False
        return input_values_and_validations_dict


def switch_and_date_generator(list_of_switches_and_dates: list) -> tuple:
    # generating the value of each switch and date from the list
    for index_of_switch in range(0, len(list_of_switches_and_dates), 2):
        # switch and date are [switch,date] in list so date is one value above the switch
        switch = list_of_switches_and_dates[index_of_switch]
        date = list_of_switches_and_dates[index_of_switch + 1]

        yield switch, date
