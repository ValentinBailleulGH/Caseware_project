# coding:utf-8


# python test_Bailleul_Caseware_project.py "fichier_de_base_unit_testing(1).txt" liste_des_codes_complete.txt"
import unittest
import sys
from Bailleul_Caseware_project import code_extractor, ERROR_DICT
# print(sys.argv)

FB1 = "fichier_de_base_unit_testing(1).txt"
LCC = "liste_des_codes_complete.txt"


class TestProjet(unittest.TestCase):
    def test_no_ID_two_letters(self):
        self.assertEqual(code_extractor(FB1, LCC), "fichier_de_base_unit_testing(1).txt")
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

if __name__ == "__main__":
    unittest.main()
