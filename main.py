from src.parsers import get_files_data
from os import listdir
from src.report_generators import generate_and_display_report
import sys

if __name__ == "__main__":

    path = sys.argv[1]
    arguments = sys.argv[2:]

    # path to the dataset directory
    # "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"

    # creating a list of all the files in the provided directory
    list_of_files = listdir(path)

    # parsing the files data
    data = get_files_data(path , list_of_files)

    index_for_date = 1

    # iterating through all the possible arguments for reports
    for index_for_mode in range(0 , len(arguments) , 2):

        mode = arguments[index_for_mode]
        date = arguments[index_for_date]

        # generating reports
        generate_and_display_report(mode ,data, date)
        print('')

        index_for_date += 2
