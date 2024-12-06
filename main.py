from calendar import month

from src.parsers import get_files_data
from os import listdir
from src.report_generators import generate_and_display_report
import sys

if __name__ == "__main__":

    arguments = sys.argv[1:]



    # path to the dataset directory
    # "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"

    # saving the command line arguments
    path = arguments[0]
    mode = arguments[1]
    date = arguments[2]

    # creating a list of all the files in the provided directory
    list_of_files = listdir(path)

    # parsing the files data
    data = get_files_data(path , list_of_files)

    # generating reports
    generate_and_display_report(mode ,data, date)