from src.parsers import get_files_data
from os import listdir

from src.report_generators import display_computed_result
from src.report_generators import compute_highest_report_for_year_data
from src.report_generators import compute_average_report_for_month_data
from src.report_generators import compute_bar_chart_of_eachday

if __name__ == "__main__":

    # path to the dataset directory
    path = "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"

    # converting the files into a list
    list_of_files = listdir(path)

    # parsing the files data
    data = get_files_data(path , list_of_files)

    new_data = compute_bar_chart_of_eachday("2004","6",data)

    # new_data = compute_highest_report_for_year_data("2004",data)
    # new_data = compute_average_report_for_month_data("2006","8",data)
    display_computed_result(new_data)
