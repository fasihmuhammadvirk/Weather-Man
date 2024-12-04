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

# dic = {}
#
#
# dic["2011"] = {}
# dic["2011"]["9"]= {}
# dic['2011']['9']['8'] = "this is the data"
#
#
#
# dic["2012"] = {}
# dic["2012"]["9"]= {}
# dic['2012']['9']['8'] = "this is the data"
#
# dic["2013"] = {}
# dic["2013"]["9"]= {}
# dic['2013']['9']['8'] = "this is the data"
# dic["2013"]["8"]= {}
# dic['2013']['9']['8'] = "this is the data"
#
#
# dic["2014"] = {}
# dic["2014"]["9"]= {}
# dic['2014']['9']['8'] = "this is the data"
# print(dic)
#
class wd():

    def __init__(self):
        print('hi')
        dic = {
            "2011": {"9": {"1": "data",
                           "2": "data", },
                     "8": {"1": "data",
                           "2": "data",
                           }

                     },
            "2012": {"9": {"1": "data",
                           "2": "data", },
                     "8": {"1": "data",
                           "2": "data",
                           }

                     },
        }
        self.data = dic

    def add_data(self,y,m,d,dd):
        if y in self.data.keys():
            if m in self.data[y].keys():
                self.data[y][m][d] = dd
            else:
                self.data[y][m] = {}
                self.data[y][m][d] = dd
        else:
            self.data[y] = {}
            self.data[y][m] = {}
            self.data[y][m][d] = dd

        # print(self.data)

    def get_d(self):
        return self.data


all_d = wd()

all_d.add_data("2013","9","1","this is the data")
all_d.add_data("2013","8","2","this is the data")


print(all_d.get_d())



# print(all_d.get_d())

# dic = {
#     "2011": {"9": {"1": "data",
#                    "2": "data", },
#              "8": {"1": "data",
#                    "2": "data",
#                    }
#
#              },
#     "2012": {"9": {"1": "data",
#                    "2": "data", },
#              "8": {"1": "data",
#                    "2": "data",
#                    }
#
#              },
# }
#
#
# dic["2011"]['7'] = {3:"data"}
#
# dic['2012'] = {"1" : {}}
# print(dic)