# import csv
# from dataclasses import dataclass
# from os import listdir
#
# from scipy.constants import value
#
#
# @dataclass
# class Files:
#
#     PKT: str
#     MaxTemperatureC: int
#     MeanTemperatureC: int
#     MinTemperatureC: int
#     DewPointC: int
#     MeanDewPointC: int
#     MinDewpointC: int
#     MaxHumidity: int
#     MeanHumidity: int
#     MinHumidity: int
#     MaxSeaLevelPressurehPa: int
#     MeanSeaLevelPressurehPa: int
#     MinSeaLevelPressurehPa: int
#     MaxVisibilityKm: int
#     MeanVisibilityKm: int
#     MinVisibilitykM: int
#     MaxWindSpeedKmh: int
#     MeanWindSpeedKmh: int
#     MaxGustSpeedKmh: int
#     Precipitationmm: int
#     CloudCover: int
#     Events: int
#     WindDirDegrees: int
#
#
# path = "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"
# files_lst = listdir(path)
#
# # print(files_lst)
#
#
#
# def remove_spaces(dic:dict) -> dict:
#     new_dic = {}
#     for key, value in dic.items():
#         new_key = key.replace(" ", "").replace("/", "")
#         new_dic[new_key] = value
#
#     return new_dic
#
#
# files_name_dir = {}
# for files_path in files_lst:
#
#     with open(f'{path + "/" + files_path}', mode='r') as file:
#         reader = csv.DictReader(file)
#         files = []
#         for row in reader:
#             row = remove_spaces(row)
#             files.append(Files(**row))
#
#         file_name = files_path.replace(path, "")
#         files_name_dir[f'{file_name}'] = files
#
# # print(files_name_dir["Murree_weather_2011_May.txt"])
# for key in files_name_dir.keys():
#     if "2011" in key and "May" in key:
#         print(key)
#
#
# # # print(files_name_dir["Murree_weather_2011_May.txt"])
# # for key in files_name_dir.keys():
# #     if "2011" in key and "May" in key:
# #         print(key)



dic = {
    "2011":{
        "9":{
            1:"This is the data"
        }
    }
}


print(dic["2011"]["9"][1])
dic['2011']['9'][3] = "This is the new data"
dic['2012'] = '10'



print(dic)