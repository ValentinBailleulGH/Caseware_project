import ctypes
from Bailleul_Caseware_project import ERROR_DICT


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


