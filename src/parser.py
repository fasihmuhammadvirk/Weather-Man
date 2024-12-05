import csv
from src.data_strucutres import WeatherData, lst_of_files_object
from src.utils import  formate_key_value

def parsing_files_data(path:str, files_name_lst : list )-> list:

    """
    Parse a list of weather data files and organize the data into a structured format.

    Args:
        path (str) : Path to the directory containing all files.
        files_name_lst (list): A list of file names containing weather data.

    Returns:
        lst_of_file_object: A List of instance of `WeatherData` containing the parsed and organized weather data.
    """

    for file_names in files_name_lst:

        #opening file
        with open(f'{path + "/" + file_names}', mode='r') as file:

            # reading the files as a dictionary
            reader = csv.DictReader(file)

            for rows in reader:

                # using the function to remove spaces from header and converting values into desire datatypes
                rows = formate_key_value(rows)

                # creating and appending the instance of WeatherData in the list
                lst_of_files_object.append(WeatherData(**rows))

    return lst_of_files_object
