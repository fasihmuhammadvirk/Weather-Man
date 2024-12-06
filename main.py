from src.parsers import get_files_data
from os import listdir

from src.reports import get_report_by_year, get_report_by_month, show_report_by_month

if __name__ == "__main__":

    # path to the dataset directory
    path = "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"

    # converting the files into a list
    list_of_files = listdir(path)

    # parsing the files data
    data = get_files_data(path , list_of_files)
    # report = get_report_by_year("2006",data)
    report = get_report_by_month("2004","8",data)
    show_report_by_month("2006","8",data)

    # print(report)
