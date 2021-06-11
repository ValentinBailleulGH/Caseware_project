
import ctypes  # Used to create a pop-up error message

FICHIER_DE_BASE             = "../ressources/fichier_de_base_unit_testing.txt"
LISTE_DES_CODES_COMPLETE    = "../ressources/liste_des_codes_complete.txt"
ERROR_DICT = dict([
    ('Error in fichier_de_base.txt',
        "Beware ! This file contains wrong characters or expressions."),
    ('Error in liste_des_codes_complete.txt',
        "Beware ! This file contains wrong characters or expressions.")
])



def code_extractor():
    """
    Returns a list that will be added to fichier_de_base.txt

    Returns:
        list_to_add_in_FichierBase: A list of codes
    """

    # the list that will be returned at the end of the function
    list_to_add_in_FichierBase = []

    # the two following function will permit to open 
    # each .txt file to copy its content in an empty list or dict 
    with open(LISTE_DES_CODES_COMPLETE, mode='r', encoding='utf8') as ListeCodesComplete:
        
        # creates an empty list. Will be added 
        # each line from liste_des_codes_complete.txt
        ListeCodesComplete_list = [elem.split('\n')[0] for elem in ListeCodesComplete]

            # adds a new element, which is a line 
            # from liste_des_codes_complete.txt
            # into the ListeCodesComplete_list.

            # From '1.0.1.9\n' it would split this way:
            # ListeCodesComplete_list.append('1.0.1.9')
    

    with open(FICHIER_DE_BASE, mode='r', encoding='utf8') as FichierBase:
        
        # creates an empty dict in that will 
        # be added each line from fichier_de_base.txt
            
        try:
            # adds a new element, which is a line from fichier_de_base.txt
            # into to the FichierBase_dict.
            #
            # From the element '1.0.1=BP.1.01.01\n' it would split this way:
            # FichierBase_dict['1.0.1'] = 'BP.1.01.01'
            #
            # Each element of FichierBase is cut 
            # and added in the FichierBase_dict dictionary.
            #
            # Will be removed from the dictionary 
            # the '\n' and the line [MAPTOMAP]
            FichierBase_dict = {
                elem.split("=")[0] : elem.split("=")[1].split('\n')[0]
                for elem in FichierBase if elem != "[MAPTOMAP]\n"
            }
        
        except IndexError:
            return ERROR_DICT.get('Error in fichier_de_base.txt')


    # each '.txt' document is now copied into its own list or dict
    
    for ListeCodesComplete_line in ListeCodesComplete_list:
        
        try:

            # 'b' is the boolean that will be used to compare
            # the one element 'ListeCodesComplete_line'
            # to every 'FichierBase_line' that
            # will be created just below
            compare_bool = False

            # 's' is the string that will be overwritten and may be added
            # to the 'list_to_add_in_FichierBase' that will be returned
            # if it turns out to be useful
            group_code_string = "" 

            for FichierBase_line in FichierBase_dict.items():

                try:
                    # Example :  1.0.1=BP.1.01.01 is taken from FichierBase
                    # code_FichierBase  would represent  1.0.1
                    # group_code_FichierBase would represent  BP.1.01.01
                    code_FichierBase   = FichierBase_line[0]
                    group_code_FichierBase  = FichierBase_line[1]

                    # A boolean that looks for consistency between
                    # the characters of code_FichierBase and those 
                    # with which ListeCodesComplete_line begins.
                    start_matches = ListeCodesComplete_line.startswith(code_FichierBase)

                    # A boolean that checks if the two series of characters
                    # are the same
                    is_same_string = (code_FichierBase == ListeCodesComplete_line)

                    # If there is a match AND both series of characters
                    # aren't the same size (meaning that they are 
                    # two differents expressions), then ListeCodesComplete_line
                    # could be added in the final list.
                    if start_matches and not is_same_string:
                        compare_bool = True
                        # replaces the string with the group code
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
            list_to_add_in_FichierBase.append(ListeCodesComplete_line + '=' + group_code_string)

    # at this point, the returned list contains
    # every complete code that should be added in
    # fichier_de_base.txt . Otherwise, it contains
    # an error message that will be interpreted
    # later by the main function
    return list_to_add_in_FichierBase



def main():
    """
    The main function running the code.
    It allows to add in the fichier_de_base.txt
    all the lines coming from the 
    liste_des_codes_complete.txt and which need
    to be added.

    Before doing so, it checks whether the list
    returned by the code_extractor function c
    ontains any error messages, in which case 
    an error message is printed.
    """
    # runs the code_extractor function
    list_to_add = code_extractor()
    
    # opens fichier_de_base.txt with reading and writing allowed
    with open(FICHIER_DE_BASE, mode='a+', encoding='utf8') as FichierBase:
        # checks if the function returned an error
        for error in ERROR_DICT.items():
            # error[1] represents the value of the error dictionary
            # in this case it would be the error message itself
            if list_to_add == error[1]:

                # Prints an error message on your screen.
                #
                # error[1] is the message
                # error[0] is the key of the message, in fact its name
                # error[0] would be the title of the box whereas
                # error[1] would be its content        
                ctypes.windll.user32.MessageBoxW(0, error[1], error[0], 1)
                return

        # This counter permits to avoid putting
        # a last '\n' at the very end of the loop.
        counter_ = 0
        
        for elem in list_to_add:
            if counter_ < len(list_to_add):
                # Only adds '\n' at the end of
                # the line if there is still 
                # something to write afterward.
                #
                # if counter reaches the length of
                # the list added in fichier_de_base,
                # then no '\n' will be writen.
                # 
                # Thus, you won't face an 
                # IndexError while running 
                # the code twice.
                FichierBase.write('\n')

            # Writes a new line in fichier_de_base.txt
            # containing the newborn code
            FichierBase.write(elem)

            counter_ += 1


if __name__ == "__main__":
    main()
