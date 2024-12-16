from src.compute_reports import compute_highest_report_for_year_data
from src.compute_reports import compute_average_report_for_month_data
from src.compute_reports import compute_bar_chart_of_eachday

def display_computed_result(computed_report_results : any) -> None:

    """
    Display computed weather report results based on the input data structure.

    Parameters:
        computed_report_results (list): A list containing computed report data. The structure of the list
        determines the type of report displayed:
        
            - If the first element is a dictionary, it displays the highest temperature, lowest temperature,
              and maximum humidity with their respective dates.
            - If the list contains strings, it prints each string, assumed to be bar chart data.
            - Otherwise, it displays the highest average temperature, lowest average temperature, and
              maximum average humidity.

    Returns:
        None
    """

    if isinstance(computed_report_results,list):

        for bar_char in computed_report_results:
            print(bar_char)

    elif isinstance(computed_report_results[0],dict):

        maximum_temperature  = "Highest: {}C on {}".format(computed_report_results[0]["max_temp"] ,
                                                            computed_report_results[0]["date"])

        lowest_temperature = "Lowest: {}C on {}".format(computed_report_results[1]["low_temp"] ,
                                                        computed_report_results[1]["date"])

        max_humidity = "Humidity: {}% on {}".format (computed_report_results[2]["max_humidity"] ,
                                                     computed_report_results[2]["date"])

        print(maximum_temperature)
        print(lowest_temperature)
        print(max_humidity)

    else:

        highest_average_temperature = "Highest Average: {}C".format(computed_report_results[0])
        lowest_average_temperature = "Lowest Average: {}C".format(computed_report_results[1])
        maximum_average_humidity = "Average Mean Humidity: {}%".format(computed_report_results[2])

        print(highest_average_temperature)
        print(lowest_average_temperature)
        print(maximum_average_humidity)


def generate_and_display_report(switch : str , data : list , date : str) -> None:

    """
    Generates and displays a weather report based on the specified mode and data.

    Parameters:
        switch (str): The mode of report generation. 'c' for bar chart, otherwise average report.
        data (list): The weather data to be processed.
        date (str) : The date of which to generate the report.

    Returns:
        None
    """

    # if the given mode is -c
    if switch == "-c":
        year , month = date.split("/")
        computational_results = compute_bar_chart_of_eachday(year , month , data)
        display_computed_result(computational_results)

    # if the given mode is -a
    elif switch == '-a':
        year, month = date.split("/")
        computational_results = compute_average_report_for_month_data(year , month , data)
        display_computed_result(computational_results)

    # if the given mode is -e
    elif switch == '-e':
        year = date
        computational_results = compute_highest_report_for_year_data(year , data)
        display_computed_result(computational_results)

    else:
        print("This is Not a Define Mode")
