# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# GUI_data_window.py
# pyside6 GUI data window class.
# display the necessary data from the file in the datawindow

# Pyside6 module :
# pip3 install pyside6
# Tutorial : https://www.pythonguis.com/pyside6-tutorial/
#Plotting pyside6 : https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/

#Musics : #free music: https://pixabay.com/sound-effects/search/energy/


#
#
# Modules imports
#
#

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import  QMainWindow, QWidget, QGridLayout, QSizePolicy
from PySide6.QtGui import QColor

import pandas as pd
if 'pandas' not in sys.modules:
    sys.exit("Error: pandas package not imported")

from datetime import datetime

#
#
# Class imports
#
#

from GUI_windows.XY_datachart import XYDatachart
from GUI_windows.XY_2datacharts import XY2Datachart
from file_processing.file_check import filecheckf



#
#
# Window class definition
#
#

class dataWindow(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensors Data")
        self.setStyleSheet("background-color: rgb(25,25,25);")
        self.top = 100 # pixels
        self.left = 100
        self.width = 2000 #pixels
        self.height = 1500
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowFlags(Qt.Window | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)  # Enable window resizing
        self.data_acquisition()
        self.dataWindowsetup()

    def data_acquisition(self):
        file_path = 'Data/processed_data.csv'
        df = pd.read_csv(file_path) #Read csv and converts data to pandas dataframe
        self.headers, nb_headers = filecheckf(file_path) # Extract Nb of headers & headers line + check csv file
        self.data_columns = [] #list of list
        for i in range(nb_headers): # Extract columns without headers
            self.data_columns.append(df[self.headers[i]].tolist())
        current_time = datetime.now()
        #Convert temps_mesure columns into relative hours
        hours_list=[] # empty list
        for date in self.data_columns[0]:
            date_time = datetime.strptime(date, '%Y-%m-%d %H:%M:%S') # Convert the date to datetime object
            # Calculate the relative hours
            relative_hours = -(current_time - date_time).total_seconds() / 3600 # Calculate the relative hours
            hours_list.append(round(relative_hours, 2))# Append relative hours to the list with 2 decimals
        self.data_columns[0]=hours_list # assign new relative hours list


    def dataWindowsetup(self):
        #Test data
        #y_data = [30, 26, 33, 28, 36, 40, 50]
        #x_data = [-24, -20, -15, -11, -8, -3, 0]

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        #Air pressure display
        color = QColor(135, 206, 250)  # Nice blue color
        self.chart = XYDatachart(self.data_columns[0], self.data_columns[1], 'Air pressure', 'h', 'hPa', color)
        self.chart.setStyleSheet("border: 1px solid white ;")
        #self.setCentralWidget(self.chart)
        layout.addWidget(self.chart, 0, 0)  # Add chart at row 0, column 0

        #Air humidity display
        color2 =  QColor(255, 182, 193)  # Light pink color
        self.chart2 = XYDatachart(self.data_columns[0], self.data_columns[8], 'Air Humidity', 'h', '%', color2)
        self.chart2.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart2, 0, 1)  # Add chart2 at row 0, column 1

        #Air temperature display
        color3 = QColor(152, 251, 152)  # Light green color
        self.chart3 = XYDatachart(self.data_columns[0], self.data_columns[9], 'Air Temperature', 'h', 'Celsius', color3)
        self.chart3.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart3, 1, 0)  # Add chart3 at row 1, column 0

        color4 =  QColor(255, 165, 0)   # Nice orange color (RGB: 255, 165, 0)
        color5 =QColor(200, 180, 255) # Nice purple color (RGB: 128, 0, 128)
        self.chart4 = XY2Datachart(self.data_columns[0], self.data_columns[2],self.data_columns[3], 'Infrared', 'Visible light', 'h', 'lm', color4, color5)
        self.chart4.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart4, 1, 1)  # Add chart3 at row 1, column 1

        color6 =  QColor(255, 165, 0)    # Nice orange color (RGB: 255, 165, 0)
        color7 = QColor(200, 180, 255)   # Nice purple color (RGB: 128, 0, 128)
        self.chart5 = XY2Datachart(self.data_columns[0], self.data_columns[6],self.data_columns[7], 'CO2', 'O2', 'h', 'ppm', color6, color7)
        self.chart5.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart5, 2, 0)  # Add chart3 at row 2, column 0

        color8 = QColor(255, 0, 0)  # Nice red color (RGB: 255, 0, 0) 
        self.chart6 = XYDatachart(self.data_columns[0], self.data_columns[4], 'Ultraviolet', 'h', 'UV index', color8)
        self.chart6.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart6, 2, 1)  # Add chart3 at row 2, column 1

        # Set the size policy of the central widget to expand with the main window
        central_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)




