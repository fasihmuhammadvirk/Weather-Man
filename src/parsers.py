from src.data_strucutres import WeatherData
from src.utils import  clean_and_convert_dic , read_file_data

def get_files_data(path : str , list_of_files : list) -> list:

    """
    Returns a list of weather data files and organize the data into a structured format.

    Args:
        path (str) : Path to the directory containing all files.
        list_of_files (list): A list of files containing weather data.

    Returns:
        list_of_file_object: A List of instance of `WeatherData` containing the parsed and organized weather data.
    """

    list_of_files_object = []

    # iteration through each file from file list
    for file_name in list_of_files:

        # file_data_as_dic = read_file_data(path,file_name)
        file_data = read_file_data(path,file_name)

        for data in file_data:

            parsed_data = parse_file_data(data)

            list_of_files_object.append(parsed_data)

    return list_of_files_object

def parse_file_data(file_data : dict) -> object:

    """
    Parses file data into a WeatherData object.

    This function formats the input dictionary by adjusting keys and converting
    values to appropriate data types, then initializes a WeatherData object
    using the formatted data.

    Args:
        file_data (dict): The input dictionary containing weather data.

    Returns:
        WeatherData: An instance of WeatherData populated with the formatted data.
    """

    formated_file_data = clean_and_convert_dic(file_data)

    return WeatherData(**formated_file_data)



