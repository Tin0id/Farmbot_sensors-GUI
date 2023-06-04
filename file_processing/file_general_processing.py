# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# file_general_processing.py
# Function that will process the CSV file downloaded from the drive and create a new CSV file
# Function will aslo call the filecheckf function to check the csv file see file_check.py for more information
# No inputs (the file path of th downloaded file is constant : always downloaded on the desktop)
# Output a new CSV file in the Data folder with the name "processed_data"

# General processing : 
# Clean the useless column, delete empty lines, avg same type of data from different sensors, convert timestamp to datetime...


##
##
## Modules import
##
##

import os
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
## Modules import
##
##

from file_processing.file_check import filecheckf # Imports function


## Class

def generalProcessing():

    ##
    ##
    ## File extraction and download check
    ##
    ##

    file_path = "~/Desktop/latest_daily_version_farmbot_data.csv"
    expanded_path = os.path.expanduser(file_path)
    absolute_path = os.path.abspath(expanded_path)
    headers, nb_headers = filecheckf(absolute_path) # Extract Nb of headers & headers line + check csv file


    ##
    ##
    ## Data acquisition & processing (pandas)
    ##
    ##


    raw_df = pd.read_csv(absolute_path) #Read csv and converts data to pandas dataframe

    data_df = raw_df.dropna() #Cleaning empty & wrong format cells, delete lines with NaN or NaT.
    # Sort the dataframe by the timestamp column
    data_df = data_df.sort_values(by=headers[1])
    # Reset the indices after sorting
    data_df = data_df.reset_index(drop=True)
    #print(data_df.head(5))
    #print(headers)
    data_df.loc[:,'Air humidity'] = data_df.loc[:,[headers[5],headers[12]]].mean(axis=1) # Avg of the two columns values into a new column added at the end
    data_df.loc[:,'Air temperature'] = data_df.loc[:,[headers[2],headers[11]]].mean(axis=1)
    data_df.loc[:,headers[1]] = data_df.loc[:,headers[1]].round(0) # Format the values in column to 0 decimal places
    data_df.loc[:, 'Air humidity'] = data_df.loc[:, 'Air humidity'].round(2) # Format the values in column to 2 decimal places
    data_df.loc[:, 'Air temperature'] = data_df.loc[:, 'Air temperature'].round(2)
    headers_to_drop = [headers[0],headers[2],headers[4], headers[5], headers[11], headers[12] ]
    data_df1 = data_df.drop(headers_to_drop, axis=1) # Deletes the columns associated to the headers given
    #data_np = data_df.to_numpy() #Conversion to numpy array for easier manipulation
    data_df1 = data_df1.reset_index(drop=True) # Resets the indices
    data_df1[headers[1]] = pd.to_datetime(data_df1[headers[1]], unit='s') #returns a series not a column, #Converting the timestamp column to a datetime
    #The universal start date for timestamps, also known as the Unix epoch, is January 1, 1970, at 00:00:00 UTC. 
    # print(data_df1.head(5))
    #self.startdatetime = int(self.start_datetime_edit.dateTime().toString("yyyyMMddhhmmss"))
    data_df1.to_csv('Data/processed_data.csv', index=False) # Creates a new csv file in the Data folder
