from src.utils import get_month_name_and_date_str , color_text_red , color_text_cyan

def compute_highest_report_for_year_data(year : str , weather_data_object_list : list) -> dict:

    weather_data_highest_report_dic = {

        "highest_temperature":{
            "value":0,
            "date":""
        },
        "lowest_temperature": {
            "value": 0,
            "date": ""
        },
        "highest_humidity": {
            "value": 0,
            "date": ""
        },

    }

    # iterating through each of the object in weather data weather_data_object list
    for weather_data_object in weather_data_object_list:

        # checking if the give year is in the object
        if year in weather_data_object.pkt:

            date_with_month_name = get_month_name_and_date_str(weather_data_object.pkt)
            # checking if the maximum temperature is greater that current
            if weather_data_object.max_temperaturec >= weather_data_highest_report_dic['highest_temperature']["value"]:
                weather_data_highest_report_dic['highest_temperature']["value"] = weather_data_object.max_temperaturec
                weather_data_highest_report_dic['highest_temperature']["date"] = date_with_month_name

            # checking if the minimum temperature is greater that current
            if weather_data_object.min_temperaturec >= weather_data_highest_report_dic["lowest_temperature"]["value"]:
                weather_data_highest_report_dic["lowest_temperature"]["value"] = weather_data_object.min_temperaturec
                weather_data_highest_report_dic["lowest_temperature"]["date"] = date_with_month_name

            # checking if the maximum humidity is greater that current
            if weather_data_object.max_humidity >= weather_data_highest_report_dic["highest_humidity"]["value"]:
                weather_data_highest_report_dic["highest_humidity"]["value"] = weather_data_object.max_humidity
                weather_data_highest_report_dic["highest_humidity"]["date"] = date_with_month_name

    # returning a tuple of dictionaries of maximum - minimum temperature and maximum humidity
    return weather_data_highest_report_dic

def compute_average_report_for_month_data(year : str , month : str , weather_data_object_list : list ) -> dict:

    weather_date_average_report_dic = dict()

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
    weather_date_average_report_dic["average_highest_temperature"] = sum_highest_temperature // total_values
    weather_date_average_report_dic["average_lowest_temperature"] = sum_lowest_temperature // total_values
    weather_date_average_report_dic["average_mean_humidity"] = sum_mean_humidity // total_values

    # returning a tuple of average values
    return weather_date_average_report_dic


def compute_bar_chart_of_eachday(year : str , month : str , weather_data_object_list : list) -> list:

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
