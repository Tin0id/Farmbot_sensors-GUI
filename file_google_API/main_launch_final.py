# Farmbot project 2023, Sensors & UI, Vincente Galdini
# main_launch_final.py
# Main python code that runs functions_download_data.py and functions_download_daily_user.py

# Take three inputs: 
#       1) from_date = year_month_day_hour_minute_seconde is the begining of range of time.
#       2) to_date = year_month_day_hour_minute_seconde is the end of the range of time.
#       3) key word = 'raw data' or 'daily data' is a parameter that choose the type of file downloaded. 

# If inputs are wrong, code won't run.

# This code will download a .txt and .csv file on user's OS.
# latest_version_farmbot_data.txt if keyword = 'raw data'
# latest_daily_version_farmbot_data.txt if keyword = 'daily data'

#------------------------------------------
from file_google_API.functions_download_data import authorization_authentication1, access_API1, txt_to_csv1
from file_google_API.functions_download_daily_user import authorization_authentication2, access_API2, txt_to_csv2
#--> better way to import the functions.

# Choice of the range of time. This range of time will be applied to the raw data or daily data.
#from_date = 20230513000000
#to_date = 20240501001000

# If the latest file only is needed.
#from_date = None
#to_date = None

# By choosing the keyword we select the type of files that will be downloaded. 
#keyword = 'raw data' # Warning: Depending of the range of time this will take a lot of time.
#keyword = 'daily data' 


def rocket_launch(from_date, to_date, keyword):
    if (keyword != 'raw data' and keyword != 'daily data') or (
        len(str(from_date)) != 14 and len(str(from_date)) != 4) or (
        len(str(to_date)) != 14 and len(str(to_date)) != 4):

        print('Wrong inputs !')
        exit(404)

    if keyword == 'raw data':
        creds = authorization_authentication1()
        access_API1(creds, from_date, to_date)
        txt_to_csv1()

    if keyword == 'daily data':
        creds = authorization_authentication2()
        access_API2(creds, from_date, to_date)
        txt_to_csv2()



