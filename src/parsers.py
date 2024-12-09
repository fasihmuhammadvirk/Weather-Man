from src.data_strucutres import WeatherData
from src.utils import  clean_and_convert_dic , read_file_data
from os import listdir

def parse_file_data(file_data : dict) -> object:

    # parsing file data into weather data object
    formated_file_data = clean_and_convert_dic(file_data)
    return WeatherData(**formated_file_data)


def get_parsed_data(list_of_weather_data_objects : list) -> list:

    parsed_data_list = []

    for weather_data in list_of_weather_data_objects:

        for rows in weather_data:
            parsed_data = parse_file_data(rows)
            parsed_data_list.append(parsed_data)

    return parsed_data_list

def get_files_data(path : str) -> list:

    """
    Returns a list of file data as an dic object.

    Args:
        path (str) : Path to the directory containing all files.
        list_of_file_data_as_dic_object (list): A list of files containing weather data.

    Returns:
        list_of_file_object: A List of instance of `WeatherData` containing the parsed and organized weather data.
    """

    files_name_list = listdir(path)

    list_of_file_data_as_dic_object = []

    # iteration through each file from file list
    for file_name in files_name_list:

        # reading file data and getting data as dic object
        file_data_as_dic_object = read_file_data(path,file_name)
        list_of_file_data_as_dic_object.append(file_data_as_dic_object)

    return list_of_file_data_as_dic_object
