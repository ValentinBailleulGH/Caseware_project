# coding:utf-8

import ctypes  # Used to create a pop-up error message for Windows OS
import sys

ERROR_DICT = dict([
    ("Error in fichier_de_base.txt",
        "Beware ! fichier_de_base.txt contains wrong characters or expressions."),
    ("Error in liste_des_codes_complete.txt",
        "Beware ! liste_des_codes_complete.txt contains wrong characters or expressions."),
    ("ID error in fichier_de_base.txt",
        "Beware ! This file may not contain the TWO-LETTER CODE required in one of its lines :\n\n\'1.0.1=B.0.1\' or \'1.0.1=1.10.1\' for instance."),
    ("Empty Space error in fichier_de_base.txt",
        "Beware ! This file contains EMPTY SPACES :\n\n\'1.0.1=\' or \'=BP.1.10.1\' for instance."),
    ("Opening error",
        "The file is not found.\nMake sure you have written \'cd C:\\Users\\...\\main\\src\'."),
    ("Successfully copied",
        " elements have been added to fichier_de_base.txt")
])


def code_extractor(FICHIER_DE_BASE, LISTE_DES_CODES_COMPLETE):
    """
    Returns a list that will be added to fichier_de_base.txt.
    Can return an error message if there is one.

    Returns:
        list_to_add_in_FichierBase: a list of codes in this format '2.3.4=TZ.9.87'.
    """

    # the list that will be returned at the end of the function
    list_to_add_in_FichierBase = []

    ListeCodesComplete_list = []
    FichierBase_dict = dict()

    try:
        # Open each '.txt' file to copy its content in an empty list or dict

        with open(LISTE_DES_CODES_COMPLETE, mode='r', encoding='utf8') as ListeCodesComplete:
            ListeCodesComplete_list = [
                elem.split('\n')[0] for elem in ListeCodesComplete
            ]
            

        with open(FICHIER_DE_BASE, mode='r', encoding='utf8') as FichierBase:

            try:
                # From the line '1.0.1=BP.1.01.01\n'
                # this will be divided as follows:
                # FichierBase_dict['1.0.1'] = 'BP.1.01.01'.
                # (doesn't count '[MAPTOMAP]' and '\n')

                for elem in FichierBase:

                    if elem == "[MAPTOMAP]\n":
                        continue

                    FB_code = elem.split("=")[0]  # '1.0.1'
                    FB_key = elem.split("=")[1].split('\n')[0]  # 'BP.1.01.01'

                    # {'1.0.1' : 'BP.1.01.01'}
                    FichierBase_dict[FB_code] = FB_key
                    
                    # Returns an error if either FB_code or FB_key is an empty string.
                    if FB_code == "" or FB_key == "":
                        return ERROR_DICT.get('Empty Space error in fichier_de_base.txt')
                    
                    # Returns an error if there isn't the two-letter ID in FB_key.
                    if not(FB_key[0].isalpha() and FB_key[1].isalpha()):
                        return ERROR_DICT.get('ID error in fichier_de_base.txt')


                    
            # Returns an error if there is a wrong character wherever in fichier_de_base.txt
            except IndexError:
                return ERROR_DICT.get('Error in fichier_de_base.txt')

    except FileNotFoundError:
        return ERROR_DICT.get('Opening error')

    # each '.txt' document is now copied into its own list or dict

    for ListeCodesComplete_line in ListeCodesComplete_list:

        try:

            # A boolean that will be used to compare 'ListeCodesComplete_line'
            # to every 'FichierBase_line' that will be looped just below.
            compare_bool = False

            # A string that will be overwritten and may be added
            # to 'list_to_add_in_FichierBase'
            group_code_string = ""

            for FichierBase_line in FichierBase_dict.items():

                try:
                    # From '1.0.1=BP.1.01.01' :
                    code_FichierBase = FichierBase_line[0]  # '1.0.1'
                    # 'BP.1.01.01'
                    group_code_FichierBase = FichierBase_line[1]

                    # A boolean that looks for consistency between
                    # the characters of code_FichierBase and those
                    # with which ListeCodesComplete_line begins.
                    start_matches = ListeCodesComplete_line.startswith(
                        code_FichierBase)

                    # A boolean that checks if the two series of characters
                    # are the same
                    is_same_string = (code_FichierBase ==
                                      ListeCodesComplete_line)

                    # Add ListeCodesComplete_line if that's useful.
                    if start_matches and not is_same_string:
                        compare_bool = True
                        # replaces the string with the group code (e.g.'BP.1.01.01')
                        group_code_string = str(group_code_FichierBase)

                    if is_same_string:
                        # resets the string
                        compare_bool = False

                # returns if there is a wrong character
                # in fichier_de_base.txt
                except IndexError:
                    return ERROR_DICT.get('Error in fichier_de_base.txt')

        # returns if there is a wrong character
        # in liste_des_codes_complete.txt
        except IndexError:
            return ERROR_DICT.get('Error in liste_des_codes_complete.txt')

        if compare_bool:
            # At the end of the second loop,
            # if it appears that there isn't this specific
            # code already in FichierBase,the code will be added.
            list_to_add_in_FichierBase.append(
                ListeCodesComplete_line + '=' + group_code_string
            )

    return list_to_add_in_FichierBase


def main(FICHIER_DE_BASE, LISTE_DES_CODES_COMPLETE):
    """
    The main function running the code.
    It allows to add in the fichier_de_base.txt
    all the lines coming from the 
    liste_des_codes_complete.txt and which need
    to be added.

    Before doing so, it checks whether the list
    returned by the code_extractor function
    contains any error messages, in which case 
    an error message is printed.
    """
    list_to_add = code_extractor(FICHIER_DE_BASE, LISTE_DES_CODES_COMPLETE)
    try:
        # Writing is allowed here.
        with open(FICHIER_DE_BASE, mode='a+', encoding='utf8') as FichierBase:
            # checks if the function returned an error
            for error in ERROR_DICT.items():
                # error[1] -> the error message
                if list_to_add == error[1]:
                    # error[0] -> the error title
                    print_error(error[1], error[0])
                    return
            counter_ = 0
            for elem in list_to_add:
                if counter_ < len(list_to_add):
                    # Only adds '\n' at the end of
                    # the line if there is still
                    # something to write afterward.
                    # (avoiding errors)
                    FichierBase.write('\n')

                FichierBase.write(elem)
                counter_ += 1
            print_writing_is_done(counter_)

    except FileNotFoundError:
        print_opening_error()
        return


#
# All functions displaying a message
#
def print_error(message, title):
    """
    Displays an error message from ERROR_DICT.
    """
    try:
        # Only works on Windows
        ctypes.windll.user32.MessageBoxW(0, message, title, 1)
    except:
        # Mac, Linux ...
        print("  [ " + message + " ] :\n  " + title)


def print_opening_error():
    """
    Displays an error message if a \'.txt\' file is not found.
    """
    try:
        # Only works on Windows
        ctypes.windll.user32.MessageBoxW
        (
            0, ERROR_DICT.get("Opening error"), "Opening error", 1
        )
    except:
        # Mac, Linux ...
        print("Opening error :\n", ERROR_DICT.get("Opening error"))


def print_writing_is_done(counter):
    """
    Displays a success message.
    """
    try:
        # Only works on Windows
        ctypes.windll.user32.MessageBoxW(
            0, str(counter) +
            ERROR_DICT.get("Successfully copied"), "Successfully copied", 1
        )
    except:
        # Mac, Linux ...
        print("Done !\n\n"+str(counter) +
              " elements have been added to fichier_de_base.txt")




if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
