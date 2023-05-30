# Farmbot project 2023, Sensors & UI, Mathieu Stawarz
# GUI_main.py
# main code that will be launched by the user : Frontend code.

# 1. Google API csv file download (from backend code, google drive access)
# 2. CSV file processing, errors check (re)
# 3. Data processing (pandas, numpy)
# 4. GUI 

# Necessary preinstalled module on OS for google API access :
#pip3 install requests
#pip3 install google-auth
#pip3 install google-cloud
#pip3 install google-auth-oauthlib
#pip3 install google-api-python-client


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
## File Download google API
##
##

from file_google_API.main_launch_final import rocket_launch # access the function

# Parameters define by the user:

from_date = 20230513000000 # or None
to_date = 20240501001000 # or None

#keyword = 'raw data' # Warning: Depending of the range of time this will take a lot of time.
keyword = 'daily data' # Faster

rocket_launch(from_date, to_date, keyword)


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
## GUI
##

