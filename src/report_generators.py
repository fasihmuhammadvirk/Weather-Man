from src.compute_reports import compute_highest_report_for_year_data
from src.compute_reports import compute_average_report_for_month_data
from src.compute_reports import compute_bar_chart_of_eachday


def display_computed_result(switch: str, computed_report_results: any) -> None:
    if switch == '-c':

        for bar_char in computed_report_results:
            print(bar_char)

    elif switch == '-e':

        maximum_temperature = computed_report_results['highest_temperature']['value']
        maximum_temperature_on = computed_report_results['highest_temperature']['date']

        lowest_temperature = computed_report_results['lowest_temperature']['value']
        lowest_temperature_on = computed_report_results['lowest_temperature']['date']

        highest_humidity = computed_report_results['highest_humidity']['value']
        highest_humidity_on = computed_report_results['highest_humidity']['date']

        report_to_display = """Highest Temperature : {}C on {} \nLowest Temperature : {}C on {} \nHumidity : {}% on {}
        """.format(maximum_temperature, maximum_temperature_on,
                   lowest_temperature, lowest_temperature_on,
                   highest_humidity, highest_humidity_on
                   )

        print(report_to_display)

    else:

        average_maximum_temperature = computed_report_results['average_highest_temperature']

        average_lowest_temperature = computed_report_results['average_lowest_temperature']

        average_mean_humidity = computed_report_results['average_mean_humidity']

        report_to_display = """Highest Temperature : {}C \nLowest Temperature : {}C \nHumidity : {}% """.format(
            average_maximum_temperature,
            average_lowest_temperature,
            average_mean_humidity)

        print(report_to_display)


def generate_and_display_report(switch: str, data: list, date: str) -> None:
    # if the given mode is -c
    if switch == "-c":
        year, month = date.split("/")
        computational_results = compute_bar_chart_of_eachday(year, month, data)
        display_computed_result(switch, computational_results)

    # if the given mode is -a
    elif switch == '-a':
        year, month = date.split("/")
        computational_results = compute_average_report_for_month_data(year, month, data)
        display_computed_result(switch, computational_results)

    # if the given mode is -e
    elif switch == '-e':
        year = date
        computational_results = compute_highest_report_for_year_data(year, data)
        display_computed_result(switch, computational_results)

    else:
        print("This is Not a Define Mode")
