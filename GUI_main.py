# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# GUI_main.py
# Main file for launching GUI

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
from PySide6.QtWidgets import QApplication

##
##
## Class imports
##
##

from GUI_start_window import startWindow

##
##
## Windows display
##
##

## Main window :
# Constructor responsible for  initializing the object and setting up the main attributes and components of the mainwindow
class Window(startWindow):  # <=== the Window class inherits all the attributes and methods from the startWindow class.
    def __init__(self):
        super().__init__()


if __name__ == "__main__": # allows the code inside the block to run only if the script is executed directly, and not when it is imported as a module.
    app = QApplication(sys.argv) #You need one (and only one) QApplication instance per application. Pass in sys.argv to allow command line arguments for your app.
    window = Window()
    # Start the event loop.
    app.exec()
    # Your application won't reach here until you exit and the event loop has stopped.







