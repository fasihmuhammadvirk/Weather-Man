from dataclasses import dataclass


# dataclass for the weather data files
@dataclass
class WeatherData:
    pkt: str
    max_temperaturec: any
    mean_temperaturec: any
    min_temperaturec: any
    dew_pointc: any
    meandew_pointc: any
    min_dewpointc: any
    max_humidity: any
    mean_humidity: any
    min_humidity: any
    max_sea_level_pressurehpa: any
    mean_sea_level_pressurehpa: any
    min_sea_level_pressurehpa: any
    max_visibilitykm: any
    mean_visibilitykm: any
    min_visibilitykm: any
    max_wind_speedkmh: any
    mean_wind_speedkmh: any
    max_gust_speedkmh: any
    precipitationmm: any
    cloudcover: any
    events: any
    winddirdegrees: any



