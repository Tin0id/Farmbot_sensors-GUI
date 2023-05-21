# Farmbot project 2023, Sensors & UI, Mathieu Stawarz
# GUI_main.py
# main code that will be launched by the user : Frontend code.

# CSV file processing, errors check (re)
# Google API import (backend)
# Data processing (pandas, numpy)
# GUI 





##
##
## Modules imports
##
##

import sys
if "sys" not in dir():
    sys.exit("Error: sys not imported")

import numpy as np
if 'numpy' not in sys.modules:
    sys.exit("Error: numpy package not imported")

import pandas as pd
if 'pandas' not in sys.modules:
    sys.exit("Error: pandas package not imported")

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

path_data= "Data/falsedata.csv" #CSV file extraction

from file_check import filecheckf # Imports function
headers, nb_headers = filecheckf(path_data) # Extract Nb of headers & headers line


##
##
## Data acquisition & processing (pandas)
##
##


raw_df = pd.read_csv(path_data) #Read csv and converts data to pandas dataframe

data_df = raw_df.dropna() #Cleaning empty & wrong format cells, delete lines with NaN or NaT.

data_np = data_df.to_numpy() #Conversion to numpy array for easier manipulation


##
## Data UI
##

