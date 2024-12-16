from src.parsers import get_files_data , get_parsed_data
from src.input_validators import validate_input , switch_and_date_generator
from src.report_generators import generate_and_display_report

if __name__ == "__main__":

    input_values_and_validation = validate_input()
    is_input_valid = input_values_and_validation['is_valid']

    if is_input_valid:

        path = input_values_and_validation['path']
        list_of_switch_date = input_values_and_validation['list_of_switch_date']

        # getting and parsing data
        list_of_files_data = get_files_data(path)
        parsed_weather_data = get_parsed_data(list_of_files_data)

        # a generator to generate switch - date pair one by one
        generated_switch_and_date = switch_and_date_generator(list_of_switch_date)

        for switch , date in generated_switch_and_date:
            generate_and_display_report(switch , parsed_weather_data , date)
            print(" ")  # just to add space between reports

    else:
        print("Please Enter Valid Input and `Try Again`")
