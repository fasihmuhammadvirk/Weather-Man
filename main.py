from os import listdir
from src.parser import parsing_files_data
from src.data_strucutres import  lst_of_files_object

if __name__ == "__main__":

    # path to the dataset directory
    path = "/Users/fasihmuhammadvirk/Desktop/Github/Weather-Man/data"

    # converting the files into a list
    files_lst = listdir(path)

    # parsing the files data
    parsing_files_data(path,files_lst)

    # running and testing data from data structure
    data = lst_of_files_object
    print(data[0])


