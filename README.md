# CASEWARE Project

- ## Author

Valentin BAILLEUL.  
Second year of preparatory school at ESIEE PARIS, Gustave Eiffel University, France since Sept. 2019.  
Apprentice in Computer Science and Applications engineering.

- ## Language

Python3

- ## Description

This file is a project containing a Python code, which purpose is to copy from one document to another series of data according to their relationship with each other, while respecting several constraints.

- ## Project status

Completed.  
An error locator can be added.

- ## Usage

Download the ZIPed project.  
Then go in your downloads folder and unZIP it.  


<b>WINDOWS :</b>  

After opening your Windows CMD, type this to go in the appropriate folder :  
<b>--> 'cd C:\Users\ ...\Downloads\Caseware_project-main\Caseware_project-main\main'</b>  
_Please note that you must replace '...' with your own path to access your own Downloads folder_

Then run the .py file :  
<b>--> python Bailleul_Caseware_project.py resources\fichier_de_base.txt resources\liste_des_codes_complete.txt</b>

The unit testing file is foundable in the same folder. Every potential error can be tested by running :  
<b>--> python test_Bailleul_Caseware_project.py</b>


<b> MAC and LINUX :</b>  

Open your cmd and change your current directory to :  
<b>--> 'C:\Users\ ...\Downloads\Caseware_project-main\Caseware_project-main\main'</b>  
_Please note that you must replace '...' with your own path to access your own Downloads folder_

Then run the .py file :  
<b>--> python3 Bailleul_Caseware_project.py ./resources/fichier_de_base.txt ./resources/liste_des_codes_complete.txt</b>

The unit testing file is foundable in the same folder. Every potential error can be tested by running :  
<b>--> python3 ./test_Bailleul_Caseware_project.py</b>

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
