# Farmbot project 2023, Sensors & UI, Mathieu Stawarz
# file_check.py
# function that check the CSV file and extract the headers line

# Function name : filecheckf
# Functions input : csv file pathname
# Function outputs : 
# 1. list containing the csv file headers
# 2. int containing the nb of headers of the csv file

# Fonctions errors check :
# Emptiness of the file?
# Headers or not ? 

#
#
# Module imports
#
#

import sys
if "sys" not in dir():
    sys.exit("Error: sys not imported")

import re
if "re" not in sys.modules:
    sys.exit("Error: re not imported")


#
#
# filecheckf function
#
#


def filecheckf(path_data):
    file = open(path_data, "r")

    #Error check if files is empty or has headers only
    file_content = file.read()
    file.close()
    if file_content == "":
        sys.exit("\n File '{}' is empty".format(path_data))
    else:
        if "\n" not in file_content:
            sys.exit("\n File '{}' contains headers only.\n".format(path_data))

    #Error check file has headers or not 
    split_file_values = re.split('\n|,', file_content) #regex split, use | as or for mutliole delimiters
    split_file_lines = file_content.split('\n')
    header_line = split_file_lines[0].split(',')
    hl_dec = re.split(r'\.|,', split_file_lines[0]) # hl_d = headline_decimals & r'\.' dot split added too for isdigit
    if any(hl_dec[i].isdigit() for i in range(len(hl_dec)) ): # Check if there are only digits in 1st line cells
        sys.exit("\n File '{}' headers are incomplete or non-existent \n".format(path_data))

    #Extract Nb of headers & headers line
    headers_line = split_file_lines[0].split(',') #List containing all the headers
    nb_headers= len(split_file_lines[0].split(',')) #int containing nb of headers

    #Delete unused variables --> useless since system will automatically delete the function variables
    #del(file,file_content, split_file_values, split_file_lines, hl_dec )

    return  headers_line, nb_headers


