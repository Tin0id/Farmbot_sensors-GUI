##
##
## Modules imports & error check
##
##

import imp
import sys
if "sys" not in dir():
    sys.exit("Error: sys not imported")

import re
if "re" not in sys.modules:
    sys.exit("Error: re not imported")

import numpy as np
if 'numpy' not in sys.modules:
    sys.exit("Error: numpy package not imported")

import pandas as pd
if 'pandas' not in sys.modules:
    sys.exit("Error: pandas package not imported")

import matplotlib.pyplot as plt
if 'matplotlib.pyplot' not in sys.modules:
    sys.exit("Error: pyplot package not imported")
plt.close("all") #Closes all matplotlib plots

##
##
## File Download API
##
##






##
##
## File error check
##
##

path_data= "Data/falsedata.csv"

#Error check file empty or not 
file = open(path_data, "r")
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
headers_line = split_file_lines[0].split(',')
nb_headers= len(split_file_lines[0].split(','))

#Delete unused variables
del(file,file_content, split_file_values, split_file_lines, hl_dec )


##
##
## Data acquisition & processing (pandas)
##
##


#Read csv and converts data to pandas dataframe
raw_df = pd.read_csv(path_data) 

#Cleaning empty & wrong format cells
data_df = raw_df.dropna()

#Conversion to numpy array for easier manipulation
data_np = data_df.to_numpy()

#Seperate dataframe into series for each column(header=sensor data)


##
## Data UI - Basic matplotlib plotting
##


### plot data in for loop in seperate figures
for i in range(nb_headers):
    plt.figure(i)
    data_df.iloc[:, i:i+1].plot()
    print(i)
plt.show()