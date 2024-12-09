import sys
from src.parsers import get_files_data , get_parsed_data
from src.utils import validate_input , process_input , switch_and_date_generator
from src.report_generators import generate_and_display_report

if __name__ == "__main__":

    input_values = sys.argv[1:]

    input_is_valid = validate_input(input_values)

    if input_is_valid:

        path , list_of_switch_date = process_input(input_values)

        # getting and parsing data
        list_of_files_data = get_files_data(path)
        parsed_weather_data = get_parsed_data(list_of_files_data)

        generated_switch_and_date = switch_and_date_generator(list_of_switch_date)

        for switch , date in generated_switch_and_date:

            generate_and_display_report(switch , parsed_weather_data , date)
            print(" ")  # just to add space between reports

    else:
        print("Please Enter Valid Input and `Try Again`")
