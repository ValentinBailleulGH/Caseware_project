# coding:utf-8

import unittest
from Bailleul_Caseware_project import code_extractor, ERROR_DICT

LCC = "resources/tests/liste_des_codes_complete_unit.txt"

def fb(number):
    """
    Returns a string composed this way:
    "resources/tests/fichier_de_base_unit_testing(1).txt"
    It correponds to a certain file in the tests folder.
    """
    return "resources/tests/fichier_de_base_unit_testing(" + str(number) + ").txt"
    

class TestProjet(unittest.TestCase):
    def test_all_good(self):
        self.assertEqual(code_extractor(fb(1), LCC),
            ["1.0.1.1=BP.10.10"]
        )
        
    def test_no_two_letters_ID(self):
        self.assertEqual(code_extractor(fb(2), LCC),
            ERROR_DICT.get("ID error in fichier_de_base.txt")
        )

    def test_nothing_after_equal_sign(self):
        self.assertEqual(code_extractor(fb(3), LCC),
            ERROR_DICT.get("Empty Space error in fichier_de_base.txt")
        )

    def test_before_after_equal_sign(self):
        self.assertEqual(code_extractor(fb(4), LCC),
            ERROR_DICT.get("Empty Space error in fichier_de_base.txt")
        )

    def test_no_equal_sign(self):
        self.assertEqual(code_extractor(fb(5), LCC),
            ERROR_DICT.get('Error in fichier_de_base.txt')
        )

    def test_empty_line(self):
        self.assertEqual(code_extractor(fb(6), LCC),
            ERROR_DICT.get('Error in fichier_de_base.txt')
        )

    def test_nothing_to_copy(self):
        self.assertEqual(code_extractor(fb(7), LCC),
            []
        )


        
if __name__ == "__main__":
    unittest.main()
