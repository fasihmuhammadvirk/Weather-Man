from src.parsers import get_files_data
from os import listdir

if __name__ == "__main__":

    # path to the dataset directory
    path = "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"

    # converting the files into a list
    list_of_files = listdir(path)

    # parsing the files data
    data = get_files_data(path , list_of_files)
    print(data[0])

