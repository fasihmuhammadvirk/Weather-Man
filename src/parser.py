import csv
from dataclasses import dataclass
from os import listdir
from ast import literal_eval


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

def conversion(dic:dict) -> dict:
    """
This function take a dictionary remove spaces from its key and convert its each value into appropriate data type and
return a new dictionary.

Args:
    dic: take a dictionary
return:
    dict : return a dictionary
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

# parser
def parser(files_name_lst:list) -> None:
    """
    Take a List of filename and prase the data of each file name in the list.

    Args:
        files_name_lst: take a list conditioning of filenames

    Return:
        None
    """
    # data structure to store the file name with its data
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
            file_name = file_names.replace(path, "")
            files_name_dir[f'{file_name}'] = files


#path to the dataset directory
path = "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"
files_lst = listdir(path)

# uploading data
parser(files_lst)



