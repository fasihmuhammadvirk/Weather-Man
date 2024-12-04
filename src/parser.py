import csv
from dataclasses import dataclass
from os import listdir
from ast import literal_eval
from calendar import month_abbr


#dataclass for the Files Data
@dataclass
class Files:
    PKT: str
    MaxTemperatureC: any
    MeanTemperatureC: any
    MinTemperatureC: any
    DewPointC: any
    MeanDewPointC: any
    MinDewpointC: any
    MaxHumidity: any
    MeanHumidity: any
    MinHumidity: any
    MaxSeaLevelPressurehPa: any
    MeanSeaLevelPressurehPa: any
    MinSeaLevelPressurehPa: any
    MaxVisibilityKm: any
    MeanVisibilityKm: any
    MinVisibilitykM: any
    MaxWindSpeedKmh: any
    MeanWindSpeedKmh: any
    MaxGustSpeedKmh: any
    Precipitationmm: any
    CloudCover: any
    Events: any
    WindDirDegrees: any


class WeathreData():

    def __init__(self):
        self.data = {}

    def add_data(self,year,month,date,datsa):
        """
        Add weather data for a specific date to the internal data structure.

        Args:
            year (str): The year of the data entry.
            month (str): The month of the data entry.
            date (str): The date of the data entry.
            datsa (Files): An instance of `Files` containing weather data to be added.

        This method updates the internal dictionary `self.data` by adding the
        provided weather data under the specified year, month, and date.
        """

        if year in self.data.keys():
            if month in self.data[year].keys():
                self.data[year][month][date] = datsa
            else:
                self.data[year][month] = {}
                self.data[year][month][date] = datsa
        else:
            self.data[year] = {}
            self.data[year][month] = {}
            self.data[year][month][date] = datsa


    def get_data(self,year,month,date):

        """
        Retrieve weather data for a specific date from the internal data structure.

        Args:
            year (int or str): The year of the data entry.
            month (int or str): The month of the data entry.
            date (int or str): The date of the data entry.

        Returns:
            Files: An instance of `Files` containing the weather data for the specified date,
            or prints "No Data Found" if the data is unavailable.
        """

        try:
            year = str(year)
            month = str(month)
            date = str(date)

            feteched_data =  self.data[year][month][date]
            return feteched_data
        except:
            print("No Data Found")




def conversion(dic:dict) -> dict:

    """
    Processes a dictionary by removing spaces and slashes from keys and converting values to appropriate data types.

    Args:
        dic (dict): The input dictionary with keys and values as strings.

    Returns:
        dict: A new dictionary with formatted keys and converted values.
    """

    new_dic = {}
    for key, value in dic.items():
        new_key = key.replace(" ", "").replace("/", "")

        # converting into appropriate data type
        # place PKT and Event in the if statement cause they are not properly formated so, cant be converted
        if new_key == "PKT":
            new_dic[new_key] = value
        elif new_key == "Events":
            new_dic[new_key] = value
        else:
            #checking for null value
            if value == "":
                new_dic[new_key] = value
            else:
                # converting each value to its desire datatype
                new_dic[new_key] = literal_eval(value)

    return new_dic


def get_month(month_name):

    """
    Convert a month abbreviation to its corresponding month number.

    Args:
        month_name (str): The three-letter abbreviation of the month.

    Returns:
        str: The month number as a string, or the original input if no match is found.
    """

    month = month_name
    for k, v in enumerate(month_abbr):
        if v == month:
            month = k
            break
    return str(month)


def parser( files_name_lst:list )-> object:


    """
    Parse a list of weather data files and organize the data into a structured format.

    Args:
        files_name_lst (list): A list of file names containing weather data.

    Returns:
        WeathreData: An instance of `WeathreData` containing the parsed and organized weather data.
    """

    files_name_dir = {}
    for file_names in files_name_lst:

        #opening file
        with open(f'{path + "/" + file_names}', mode='r') as file:

            # reading all row of the file
            reader = csv.DictReader(file)

            files = []
            for row in reader:

                # removing spaces and converting data into appropriate type
                row = conversion(row)
                files.append(Files(**row))

            #storing in the dic
            file_name = file_names.replace(path, "").replace("Murree_weather_","").replace(".txt","")
            files_name_dir[f'{file_name}'] = files

    #imported data from all the file
    imported_data = files_name_dir

    #instance of the class
    all_weather_data = WeathreData()

    #parsing data
    for key, value in imported_data.items():

        key = key.split("_")

        year = key[0]
        month = get_month(key[1])

        for indivual_value in value:

            date = indivual_value.PKT.split("-")
            date_y = date[0]
            date_m = date[1]
            date_d = date[2]
            if year  == date_y and month == date_m:
                all_weather_data.add_data(year = date_y,month = date_m,date = date_d,datsa=indivual_value)
                # print("yes")

    return all_weather_data




#path to the dataset directory
path = "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"
files_lst = listdir(path)
data = parser(files_lst)

print(data.get_data(2004,7,2))








