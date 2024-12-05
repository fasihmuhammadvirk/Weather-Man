from dataclasses import dataclass

# list that contain all the instances weather data files
lst_of_files_object = []

# dataclass for the weather data files
@dataclass
class WeatherData:
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


# formated dictionary for format_key_value functions in utils
formated_dic = {}

