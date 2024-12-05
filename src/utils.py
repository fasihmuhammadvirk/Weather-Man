from ast import literal_eval
from src.data_strucutres import formated_dic

def formate_key_value(dic:dict) -> dict:

    """
    Processes a dictionary by removing spaces and slashes from keys and converting values to appropriate data types.

    Args:
        dic (dict): The input dictionary with keys and values as strings.

    Returns:
        dict: A new dictionary with formatted keys and converted values.
    """

    for key, value in dic.items():
        new_key = key.replace(" ", "").replace("/", "")

        # converting into appropriate data type

        # place PKT and Event in the if statement because they are not properly formated so, cant be converted
        if new_key == "PKT":
            formated_dic[new_key] = value

        elif new_key == "Events":
            formated_dic[new_key] = value

        else:

            # checking for null value
            if value == "":
                formated_dic[new_key] = value

            else:
                # converting each value to its desire datatype
                formated_dic[new_key] = literal_eval(value)

    return formated_dic


