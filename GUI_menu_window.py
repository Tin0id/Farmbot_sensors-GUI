# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# GUI_menu_windows.py
# pyside6 GUI menu window class.
# Interaction with the user to let him choose the type & timegap data display

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
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput #music !!




class menuWindow(QMainWindow):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensors Data")

        # Specifies the distance from the top/bottom edge of the screen to the top/bottom edge of the window
        # Where the window will be located ?
        self.top = 100 # pixels
        self.left = 100
        # Specifies the distance from the top/bottom edge of the screen to the top/bottom edge of the window
        # Size of the window ?
        self.width = 2000 #pixels
        self.height = 1500

        self.setGeometry(self.top, self.left, self.width, self.height)



