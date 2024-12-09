import sys

from src.parsers import get_files_data, get_parsed_data
from src.utils import validate_input , process_input , get_switch_and_date
from src.report_generators import generate_and_display_report
if __name__ == "__main__":



    input_values = sys.argv[1:]

    input_is_valid = validate_input(input_values)

    if input_is_valid:

        path , list_of_switch_date = process_input(input_values)

        list_of_files_data = get_files_data(path)
        parsed_weather_data = get_parsed_data(list_of_files_data)

        switches_and_date_generator = get_switch_and_date(list_of_switch_date)

        for switch , date in switches_and_date_generator:
            generate_and_display_report(switch , parsed_weather_data , date)

    else:
        print("Please Enter Valid Input and `Try Again`")





