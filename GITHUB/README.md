# CASEWARE Project

- ## Author

Valentin BAILLEUL.  
Second year of preparatory school at ESIEE PARIS, Gustave Eiffel University, France since Sept. 2019.  
Apprentice in Computer Science and Applications engineering.

- ## Language

Python3

- ## Description

This file is a project containing a Python code, whose purpose is to copy from one document to another a series of data according to their relationship with each other, while respecting several constraints.

- ## Project status

Completed.
An error locator can be added.

- ## Usage

Go to the appropriate folder in the cmd using : 'cd C:\Users\ ... \main' or '/'  
Then run the .py file :
--> 'python src\Bailleul_Caseware_project.py resource\fichier_de_base.txt resource\liste_des_codes_complete.txt'

The unit testing file is foundable here 'cd C:\Users\ ... \test\src'
'Bailleul_Caseware_project_unit_testing.py(figure)' is the one that will apply the unit tests on a file containing various anomalies.
All potential errors can be tested by running one of the various .py projects.

After running, if no pop-up message is displayed, consider re-retyping 'cd C:\Users\ ... \main\src'

### A simple example:

##### fichier_de_base.txt

1.0.1=BP.1.01.01  
3.2.3.4=TS.3.4.5

##### liste_des_codes_complete.txt

1.0.1.9  
1.0.1  
3.2.3.4.9  
3.2.3.0

#### Results:

###### Should be added in fichier_de_base.txt

1.0.1.9=BP.1.01.01 since 1.0.1.9 matches 1.0.1 from fichier de base.txt  
3.2.3.4.9=TS.3.4.5 since 3.2.3.4.9 matches 3.2.3.4 from fichier de base.txt

###### Should NOT be added in fichier_de_base.txt

1.0.1 because 1.0.1 already exists  
3.2.3.0 because '3', '3.2' and '3.2.3' don't appear in fichier_de_base.txt
