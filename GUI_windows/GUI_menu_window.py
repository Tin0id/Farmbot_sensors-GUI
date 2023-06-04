# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# GUI_menu_window.py
# File that contains the menu window class 
# Allows the user to enter a start and ending date and download + process the data

# Pyside6 module :
# pip3 install pyside6
# Tutorial : https://www.pythonguis.com/pyside6-tutorial/
#Plotting pyside6 : https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/


#
#
# Modules imports
#
#


import sys
from PySide6.QtCore import Qt, QTimer, QUrl, QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QDateTimeEdit, QPushButton
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput #music !!

#
#
# Class imports
#
#

from file_processing.file_download import fileDownload
from file_processing.file_general_processing import generalProcessing
from GUI_windows.GUI_data_window import dataWindow



##
##
## MenuWindow display
##
##

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Sensors data Date-Time"
        self.setStyleSheet("background-color: rgb(25,25,25);")
        self.top = 200 # pixels # Where the window will be located 
        self.left = 400
        self.width = 650 #pixels # Size of the window 
        self.height = 500

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create the central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignHCenter)

        # Instruction label
        label = QLabel("Select up to 24-hours back in time for quick data display")
        font= label.font()
        font.setPointSize(16)  # Set the font size
        font.setItalic(True)
        label.setFont(font)
        label_width = self.width
        label_height = 30
        label.setFixedSize(label_width, label_height)
        label.setStyleSheet("background-color: transparent; color: white; border: white")
        label.setToolTip("<h3 style='background-color: beige; color: black; border: none'> Select start date</h3>")
        label.setAlignment(Qt.AlignHCenter)  # Center align the label horizontally

        # Start date label
        start_label = QLabel("Start Date-Time:")
        font1= start_label.font()
        font1.setPointSize(20)  # Set the font size
        font1.setBold(True)
        start_label.setFont(font1)
        start_label_width = self.width
        start_label_height = 50
        start_label.setFixedSize(start_label_width, start_label_height)
        start_label.setStyleSheet("background-color: transparent; color: white; border: white")
        start_label.setToolTip("<h3 style='background-color: beige; color: black; border: none'> Select start date</h3>")
        start_label.setAlignment(Qt.AlignHCenter)  # Center align the label horizontally

        # End date label
        end_label = QLabel("End Date-Time:")
        font2= end_label.font()
        font2.setPointSize(20)  # Set the font size
        font2.setBold(True)
        end_label.setFont(font2)
        end_label_width = self.width
        end_label_height = 50
        end_label.setFixedSize(end_label_width, end_label_height)
        end_label.setStyleSheet("background-color: transparent; color: white; border: white")
        end_label.setToolTip("<h3 style='background-color: beige; color: black; border: none'> Select end date</h3>")
        end_label.setAlignment(Qt.AlignHCenter)  # Center align the label horizontally

        # Create date-time edit widgets
        self.start_datetime_edit = QDateTimeEdit()
        self.start_datetime_edit.setCalendarPopup(True)
        self.start_datetime_edit.setStyleSheet("background-color: white; color: black; border: white")
        self.start_datetime_edit.setDateTime(QDateTime.currentDateTime())  # Set default end date and time to current time
        self.end_datetime_edit = QDateTimeEdit()
        self.end_datetime_edit.setCalendarPopup(True)
        self.end_datetime_edit.setStyleSheet("background-color: white; color: black; border: white")
        self.end_datetime_edit.setDateTime(QDateTime.currentDateTime())  # Set default end date and time to current time

        # Create button layout
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignHCenter)

        # Create button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_data)
        self.save_button.setStyleSheet(
            "background-color: rgb(46, 139, 87); color: white; border: 2px solid white;"
        )  # Nice green colour
        button_width = 200
        button_height = 75
        fontp = self.font()
        fontp.setPointSize(20)  # Set the font size
        fontp.setBold(True)
        self.save_button.setFont(fontp)
        self.save_button.setFixedSize(button_width, button_height)
        self.save_button.setToolTip(
            "<h3 style='background-color: beige; color: black; border: none'> Save & launch data window </h3>"
        )  # small pop-up text near the button

        # Add button to button layout
        button_layout.addWidget(self.save_button)

        # Add widgets to layout
        layout.addWidget(start_label, alignment=Qt.AlignHCenter)
        layout.addWidget(self.start_datetime_edit, alignment=Qt.AlignHCenter)
        layout.addSpacing(40) 
        layout.addWidget(end_label, alignment=Qt.AlignHCenter)
        layout.addWidget(self.end_datetime_edit, alignment=Qt.AlignHCenter)
        layout.addSpacing(40) 
        layout.addWidget(label, alignment=Qt.AlignHCenter)
        layout.addSpacing(10) 
        layout.addLayout(button_layout)  # Add the button layout to the main layout

        self.show() #show window

    def save_data(self):
        self.playerb = QMediaPlayer() #music button
        self.audio_outputb = QAudioOutput()
        self.playerb.setAudioOutput(self.audio_outputb)
        self.playerb.setSource(QUrl.fromLocalFile("GUI_medias/success.mp3"))
        self.audio_outputb.setVolume(50)
        self.playerb.play()
        self.startdatetime = int(self.start_datetime_edit.dateTime().toString("yyyyMMddhhmmss")) # Convert in int datetime
        self.enddatetime = int(self.end_datetime_edit.dateTime().toString("yyyyMMddhhmmss")) # Converts in int datetime
        #print("Start Date-Time:", self.startdatetime)
        #print("End Date-Time:", self.enddatetime)
        #print(type(self.startdatetime))
        self.save_button.setEnabled(False)  # Disable the button temporarily
        self.save_button.setText("Saved!")  # Set the button text clicks
        #Timer
        QTimer.singleShot(1000, self.data_download)

    def data_download(self):
        self.save_button.setText("Downloading data...")  # Set the button text clicks
        fileDownload(self.startdatetime,self.enddatetime)
        QTimer.singleShot(1000, self.data_processing)

    def data_processing(self):
        self.save_button.setText("Processing data...")  # Set the button text clicks
        generalProcessing()
        QTimer.singleShot(1000, self.show_dataWindow)

    def show_dataWindow(self):
        self.w = dataWindow() #Creates a new instance w
        self.close() #closes the main_window
        self.w.show() #Show the new window 2

#if __name__ == "__main__":
#   app = QApplication(sys.argv)
#   window = MenuWindow()
#   sys.exit(app.exec())
