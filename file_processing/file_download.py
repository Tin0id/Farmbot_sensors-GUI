# Farmbot project 2023, Sensors & UI, Mathieu Stawarz
# file_download.py
# Download the CSV file from the drive,
# Inputs : start date and end date period in a int format see example below
# Output : dowloads .csv and .txt file on user desktop with name "latest_daily_version_farmbot_data"

# Necessary preinstalled module on OS for google API access :
#pip3 install requests
#pip3 install google-auth
#pip3 install google-cloud
#pip3 install google-auth-oauthlib
#pip3 install google-api-python-client

#imports
import os
from file_google_API.main_launch_final import rocket_launch # access  function

def fileDownload(from_date, to_date):
    #from_date = 20230513000000 # or None an int not a string !!
    #to_date = 20240501001000 # or None

    #Deletes json token file if it exists, can cause problems when connecting
    file_path = "token.json"
    #if os.path.exists(file_path): 
        #os.remove(file_path)
        #print("File 'token.json' deleted.")

    #keyword = 'raw data' # Warning: Depending of the range of time this will take a lot of time.
    keyword = 'daily data' # Faster
    rocket_launch(from_date, to_date, keyword)


