# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# GUI_data_window.py
# pyside6 GUI data window class.
# display the necessary data from the file

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
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QGridLayout, QSizePolicy
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput #music !!


#
#
# Class imports
#
#

from XY_datachart import XYDatachart



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

        self.dataWindowsetup()

    def dataWindowsetup(self):
        y_data = [30, 26, 33, 28, 36, 40, 50]
        x_data = [-24, -20, -15, -11, -8, -3, 0]

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        color = QColor(135, 206, 250)  # Nice blue color
        self.chart = XYDatachart(x_data, y_data, 'Air Humidity', '24', 'hours', 'h', '%', color)
        self.chart.setStyleSheet("border: 1px solid white ;")
        #self.setCentralWidget(self.chart)
        layout.addWidget(self.chart, 0, 0)  # Add chart at row 0, column 0

        color2 = QColor(255, 165, 0)  # Nice orange color (RGB: 255, 165, 0)
        self.chart2 = XYDatachart(x_data, y_data, 'Air Humidity', '24', 'hours', 'h', '%', color2)
        self.chart2.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart2, 0, 1)  # Add chart2 at row 0, column 1

        color3 = QColor(255, 0, 0)  # Nice red color (RGB: 255, 0, 0)
        self.chart3 = XYDatachart(x_data, y_data, 'Air Humidity', '24', 'hours', 'h', '%', color3)
        self.chart3.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart3, 1, 0)  # Add chart3 at row 1, column 0

        color4 = green = QColor(0, 128, 0)  # Nice green color (RGB: 0, 128, 0)
        self.chart4 = XYDatachart(x_data, y_data, 'Air Humidity', '24', 'hours', 'h', '%', color4)
        self.chart4.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart4, 1, 1)  # Add chart3 at row 1, column 1

        color5 = purple = QColor(128, 0, 128)  # Nice purple color (RGB: 128, 0, 128)
        self.chart5 = XYDatachart(x_data, y_data, 'Air Humidity', '24', 'hours', 'h', '%', color5)
        self.chart5.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart5, 2, 0)  # Add chart3 at row 2, column 0

        color6 = QColor(135, 206, 250)
        self.chart6 = XYDatachart(x_data, y_data, 'Air Humidity', '24', 'hours', 'h', '%', color6)
        self.chart6.setStyleSheet("border: 1px solid white ;")
        layout.addWidget(self.chart6, 2, 1)  # Add chart3 at row 2, column 1

        # Set the size policy of the charts to expand in both directions
        self.chart.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.chart2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.chart3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.chart4.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.chart5.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.chart6.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Set the size policy of the central widget to expand with the main window
        central_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)



if __name__ == "__main__": # allows the code inside the block to run only if the script is executed directly, and not when it is imported as a module.
    app = QApplication(sys.argv) #You need one (and only one) QApplication instance per application. Pass in sys.argv to allow command line arguments for your app.
    window = dataWindow()
    window.show()
    # Start the event loop.
    app.exec()
    # Your application won't reach here until you exit and the event loop has stopped.



