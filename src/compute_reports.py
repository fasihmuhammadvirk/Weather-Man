from src.utils import get_month_name_and_date_str , color_text_red , color_text_cyan

def compute_highest_report_for_year_data(year : str , weather_data_object_list : list) -> tuple:

    """
    Computes the highest and lowest temperature and highest humidity for a given year from a list of
    weather_data_object_list objects.
    
    Args:
        year (str): The year to filter the weather_data_object_list by.
        weather_data_object_list (list): A list of weather_data_object_list objects containing weather information.
    
    Returns:
        tuple: A tuple containing three dictionaries:
            - The highest temperature and its date.
            - The lowest temperature and its date.
            - The highest humidity and its date.
    """
    
    current_highest_temperature = {
        "max_temp":0,
        "date": ""
    }

    current_lowest_temperature = {
        "low_temp":0,
        "date": ""
    }

    current_highest_humidity = {
        "max_humidity":0,
        "date": ""
    }

    # iterating through each of the object in weather data weather_data_object list
    for weather_data_object in weather_data_object_list:

        # checking if the give year is in the object
        if year in weather_data_object.pkt:

            # checking if the maximum temperature is greater that current
            if weather_data_object.max_temperaturec >= current_highest_temperature["max_temp"]:
                current_highest_temperature["max_temp"] = weather_data_object.max_temperaturec
                current_highest_temperature["date"] = get_month_name_and_date_str(weather_data_object.pkt)

            # checking if the minimum temperature is greater that current
            if weather_data_object.min_temperaturec >= current_lowest_temperature["low_temp"]:
                current_lowest_temperature["low_temp"] = weather_data_object.min_temperaturec
                current_lowest_temperature["date"] = get_month_name_and_date_str(weather_data_object.pkt)

            # checking if the maximum humidity is greater that current
            if weather_data_object.max_humidity >= current_highest_humidity["max_humidity"]:
                current_highest_humidity["max_humidity"] = weather_data_object.max_humidity
                current_highest_humidity["date"] = get_month_name_and_date_str(weather_data_object.pkt)

    # returning a tuple of dictionaries of maximum - minimum temperature and maximum humidity
    return current_highest_temperature , current_lowest_temperature , current_highest_humidity

def compute_average_report_for_month_data(year : str , month : str , weather_data_object_list : list ) -> tuple:

    """
    Compute the average highest temperature, lowest temperature, and mean humidity
    for a given month and year from a list of weather data objects.

    Parameters:
        year (str): The year to filter the weather data.
        month (str): The month to filter the weather data.
        weather_data_object_list (list): A list of weather data objects containing
            attributes 'pkt', 'max_temperaturec', 'min_temperaturec', and 'mean_humidity'.

    Returns:
        tuple: A tuple containing the average highest temperature, average lowest
        temperature, and average mean humidity for the specified month and year.
    """

    sum_highest_temperature = 0
    sum_lowest_temperature = 0
    sum_mean_humidity = 0
    total_values = 0

    # iterating through each object from the weather data object list
    for weather_data_object in weather_data_object_list:

        # checking for the object that has the same year and month as desired
        if year in weather_data_object.pkt and month in weather_data_object.pkt.split('-')[1]:

            # keeping a count of each value
            total_values += 1

            # doing the sum of all value
            sum_highest_temperature += weather_data_object.max_temperaturec
            sum_lowest_temperature += weather_data_object.min_temperaturec
            sum_mean_humidity += weather_data_object.mean_humidity

    # calculating the average
    average_highest_temperature = sum_highest_temperature // total_values
    average_lowest_temperature = sum_lowest_temperature // total_values
    average_mean_humidity = sum_mean_humidity // total_values

    # returning a tuple of average values
    return average_highest_temperature , average_lowest_temperature , average_mean_humidity


def compute_bar_chart_of_eachday(year : str , month : str , weather_data_object_list : list) -> list:

    """
    Generates a bar chart representation of daily weather data for a specified month and year.

    Args:
        year (str): The year to filter the weather data.
        month (str): The month to filter the weather data.
        weather_data_object_list (list): A list of weather data objects containing temperature information.

    Returns:
        list: A list of strings representing the bar chart for each day's highest and lowest temperatures.
    """

    index = 0
    list_of_bar_chart_for_eachday = []

    # iterating through each object of the weather data object list
    for weather_data_object in weather_data_object_list:

        # checking for the object that has the same year and month as desired
        if year in weather_data_object.pkt and month == weather_data_object.pkt.split('-')[1]:

            # keeping count of each index
            index += 1

            # creating a string containing information of index , temperature and the horizontal bar chart
            highest_temperature = "{} {} {}".format(index , color_text_red("*") *
                                                    weather_data_object.max_temperaturec ,
                                                    str(weather_data_object.max_temperaturec)+"C" )

            lowest_temperature = "{} {} {}".format(index , color_text_cyan("-") *
                                                   weather_data_object.min_temperaturec ,
                                                   str(weather_data_object.min_temperaturec) + "C")

            list_of_bar_chart_for_eachday.append(highest_temperature)
            list_of_bar_chart_for_eachday.append(lowest_temperature)

    # returning a list
    return list_of_bar_chart_for_eachday
