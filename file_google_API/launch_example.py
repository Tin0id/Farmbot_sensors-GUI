import main_launch_final

# Parameters define by the user:

from_date = 20200513000000 # or None
to_date = 20240501001000 # or None

#keyword = 'raw data' # Warning: Depending of the range of time this will take a lot of time.
keyword = 'daily data' # Faster

main_launch_final.rocket_launch(from_date, to_date, keyword)