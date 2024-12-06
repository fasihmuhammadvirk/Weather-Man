from src.utils import get_month_name_and_date

def get_report_by_year(year : str , data : list) -> tuple:

    current_highest_temperature = {
        "max_temp":0,
        "date": ""
    }

    current_lowest_temperature = {
        "low_temp":0,
        "date": ""
    }

    current_highest_humidity = {
        "max_humidity":0,
        "date": ""
    }

    for obj in data:

        if year in obj.pkt:

            if obj.max_temperaturec >= current_highest_temperature["max_temp"]:

                current_highest_temperature["max_temp"] = obj.max_temperaturec

                current_highest_temperature["date"] = get_month_name_and_date(obj.pkt)

            if obj.min_temperaturec >= current_lowest_temperature["low_temp"]:

                current_lowest_temperature["low_temp"] = obj.min_temperaturec

                current_lowest_temperature["date"] = get_month_name_and_date(obj.pkt)

            if obj.max_humidity >= current_highest_humidity["max_humidity"]:

                current_highest_humidity["max_humidity"] = obj.max_humidity

                current_highest_humidity["date"] = get_month_name_and_date(obj.pkt)


    return current_highest_temperature , current_lowest_temperature , current_highest_humidity


def get_report_by_month(year,month,data):

    sum_highest_temperature = 0
    sum_lowest_temprature = 0
    sum_mean_humidity = 0
    total_values = 0

    for obj in data:
        if year in obj.pkt and month in obj.pkt.split('-')[1]:
            # print("hello")
            total_values += 1
            sum_highest_temperature += obj.max_temperaturec
            sum_lowest_temprature += obj.min_temperaturec
            sum_mean_humidity += obj.mean_humidity

    # print(total_values)

    average_highest_temprature = sum_highest_temperature// total_values
    average_lowest_temprature = sum_lowest_temprature//total_values
    average_mean_humidity = sum_mean_humidity//total_values

    # print(average_highest_temprature , average_lowest_temprature , average_mean_humidity)

    return average_highest_temprature , average_lowest_temprature , average_mean_humidity

def prRed(index , text , colortext): print( index , "\033[91m {}\033[00m" .format(colortext) , text+"C")
def prCyan(index , text , colortext): print(index ,"\033[96m {}\033[00m" .format(colortext),   text+"C")

def show_report_by_month(year,month,data):

    index = 0
    for obj in data:
        if year in obj.pkt and month in obj.pkt.split('-')[1]:

            index += 1

            prRed(index , str(obj.max_temperaturec) , "+"*obj.max_temperaturec)
            prCyan(index , str(obj.min_temperaturec) , "-"*obj.min_temperaturec)
            print('\n')


