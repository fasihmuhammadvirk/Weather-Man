import os
import sys
from src.utils import get_year_month

def switch_and_date_generator(list_of_switches_and_dates : list) -> tuple:

    # generating the value of each switch and date from the list

    for index_to_find_switch in range(0 , len(list_of_switches_and_dates) , 2):

        index_to_find_date = index_to_find_switch + 1

        switch = list_of_switches_and_dates[index_to_find_switch]
        date = list_of_switches_and_dates[index_to_find_date]

        index_to_find_date += 2

        yield switch , date

def validate_date(year : str , month : str) -> bool:

    if (int(year) <= 2006) and (int(year) >= 2004):

        if month is None:
            return True

        else:

            if (int(month) > 0) and (int(month) < 12):
                return True

            else:
                print("Please Enter a Valid Month")
                return False

    else:
        print("This is Not a Valid Year, we do not have data on this year")
        return False


def validate_switch(switch : str , month : str) -> bool:

    # list of the valid switches
    list_of_valid_switches = ['-e', '-a', '-c']

    # checking if the switch entered is correct
    if switch in list_of_valid_switches:

        if switch == list_of_valid_switches[0] and month is not None:
            print(print(f"{switch} This switch date should not contain value of month"))
            return False

        elif switch == list_of_valid_switches[1] and month is None:
            print(print(f"{switch} This switch date should contain value of month"))
            return False

        elif switch == list_of_valid_switches[2] and month is None:
            print(print(f"{switch} This switch date should contain value of month"))
            return False

        else:
            return True

    else:
        print(f"{switch} This is not a valid switch")
        return False



def validate_switches_and_date(list_of_switches_and_dates : list) -> bool:

    # checking if the user has entered more than three values of switch and date
    if len(list_of_switches_and_dates)//2 > 3:
        print("Please Enter only three values of switch and date to get Report")
        return False

    # checking if all the switches have their values
    if len(list_of_switches_and_dates) % 2 != 0:
        print("One of the Switch or Date is Missing")
        return False

    valid_input = False

    for index_to_find_switch in range(0, len(list_of_switches_and_dates), 2):

        index_to_find_date = index_to_find_switch + 1

        # getting value of each switch and its date
        switch = list_of_switches_and_dates[index_to_find_switch]
        date = list_of_switches_and_dates[index_to_find_date]

        # converting the date into year and month
        year , month = get_year_month(date)

        #validating if the format is correct also the date
        is_year_month_valid = validate_date(year , month)

        if is_year_month_valid:

            # validating the switches
            is_switch_valid = validate_switch(switch , month)

            if is_switch_valid:
                valid_input = True

            else:
                valid_input = False

        else:
            valid_input = False

    return valid_input

def validate_input() -> bool:

    command_line_arguments = sys.argv[1:]

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


def process_input() -> tuple:

    command_line_arguments = sys.argv[1:]

    path = command_line_arguments[0]
    list_of_switches_and_date = command_line_arguments[1:]

    return path , list_of_switches_and_date
