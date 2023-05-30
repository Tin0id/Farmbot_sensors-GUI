# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# GUI_start_windows.py
# GUI start window class setup

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
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtWidgets import  QMainWindow, QPushButton, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput #music !!
from PySide6.QtMultimediaWidgets import QVideoWidget #video widget

##
##
## Modules Class imports from other files 
##
##


from GUI_menu_window import menuWindow #import menuwindow class



##
##
## Windows display
##
##

## Main window :
# Constructor responsible for  initializing the object and 
# setting up the main attributes and components of the mainwindow
class startWindow(QMainWindow): 
    def __init__(self):
        super().__init__() # When you subclass a Qt class you must always call the super __init__ function to allow Qt to set up the object.

        self.title = "Farmbot Sensors"
        self.setStyleSheet("background-color: rgb(25,25,25);")
        self.top = 125 # pixels # Where the window will be located 
        self.left = 100
        self.width = 1250 #pixels # Size of the window 
        self.height = 650

        self.startWindowsetup() # call start window method
    
    ##starting window setup
    # separate method that sets up the main interface of the window by creating and 
    # configuring widgets like labels and setting the window's title and geometry.
    def startWindowsetup(self):
        #plays Startwindow song 
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile("GUI_medias/relaxing_song.mp3"))
        self.audio_output.setVolume(50)
        self.player.play()

        ##QPushbutton widget
        self.pushButton = QPushButton("Start", self)
        self.pushButton.clicked.connect(self.open_menuWindow)  # <=== connect to open_menuWindow submethod
        #Qbutton widget setup
        self.pushButton.setStyleSheet("background-color: rgb(46, 139, 87); color: white; border: 2px solid white;") #Nice green colour
        self.button_width = 200
        self.button_height = 75
        fontp = self.pushButton.font()
        fontp.setPointSize(25)  # Set the font size to 16
        fontp.setBold(True)
        self.pushButton.setFont(fontp)
        self.pushButton.setFixedSize(self.button_width, self.button_height)
        self.pushButton.move( (self.width - self.button_width) / 2 , (self.height - self.button_height) / 2)
        self.pushButton.setToolTip("<h3 style='background-color: beige; color: black; border: none'> Start the GUI - Data acquisition </h3>") # small pop-up text near the button

        ##Video Widget
        video_widget = QVideoWidget(self) 
        self.playerv = QMediaPlayer()
        self.playerv.mediaStatusChanged.connect(self.handle_media_status_changed) # <=== connect to handle_media_status_changed submethod, restart music !
        #Video widget setup
        video_widget_width = 400/1.25 #400pixel orig. size
        video_widget_height = 300/1.25 #300pixels orig. size
        video_widget.setFixedSize(video_widget_width, video_widget_height)
        video_widget.move(self.width - video_widget_width - 50, self.height - video_widget_height - 50)
        video_widget.setToolTip("<h3 style='background-color: beige; color: black; border: none'> Sensor Panel overview </h3>")
        self.playerv.setVideoOutput(video_widget)
        self.playerv.setSource(QUrl.fromLocalFile("GUI_medias/sensor_panel_video.mp4"))
        self.playerv.play()


        #icon label1 widget
        icon_label = QLabel(self)
        icon_top = 50 # pixels # Where the window will be located ?
        icon_left = 50
        icon_label_width = 2560/15 #2560pixel orig. size
        icon_label_height = 745/15 #745 pixels orig. size
        icon_label.setFixedSize(icon_label_width, icon_label_height)
        icon_label.setAlignment(Qt.AlignCenter)
        logo_pixmap = QPixmap("GUI_medias/Logo_EPFL.png").scaled(icon_label_width, icon_label_height, Qt.AspectRatioMode.KeepAspectRatio)
        # Get the size of the image
        #width = logo_pixmap.width() = 2560pixel 
        #height = logo_pixmap.height() = 745 pixels
        # Print the image size print(f"Image size: {width} x {height}")
        icon_label.setPixmap(logo_pixmap)
        icon_label.setGeometry(icon_left, icon_top, icon_label_width, icon_label_height)
        icon_label.setToolTip("<h3 style='background-color: beige; color: black;'>Ecole polytechnique fédérale de Lausanne </h3>")
        icon_label.setStyleSheet("QToolTip { color: black; background-color: beige }")

        #icon label2
        icon_label2 = QLabel(self)
        icon_label2_width = 1500/10 #440pixel orig. size
        icon_label2_height = 500/10 #375pixels orig. size
        icon_top2 = self.height - icon_label2_height  - 50  # pixels # Where the window will be located ?
        icon_left2 = 50
        icon_label2.setFixedSize(icon_label2_width, icon_label2_height)
        icon_label2.setAlignment(Qt.AlignCenter)
        logo_pixmap2 = QPixmap("GUI_medias/logo_createlab.jpeg").scaled(icon_label2_width, icon_label2_height,Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label2.setPixmap(logo_pixmap2)
        icon_label2.setGeometry(icon_left2, icon_top2, icon_label2_width, icon_label2_height)
        icon_label2.setToolTip("<h3 style='background-color: beige; color: black;'> Computational Robot Design & Fabrication Lab</h3>")

        #icon label3
        icon_label3 = QLabel(self)
        icon_label3_width = 1340/7 #1340pixel orig. size
        icon_label3_height = 1282/7 #1282pixels orig. size
        icon_top3 =  50  # pixels # Where the window will be located ?
        icon_left3 = self.width - icon_label3_width - 50 
        icon_label3.setFixedSize(icon_label3_width, icon_label3_height)
        icon_label3.setAlignment(Qt.AlignCenter)
        logo_pixmap3 = QPixmap("GUI_medias/farmbot_genesis.png").scaled(icon_label3_width, icon_label3_height,Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label3.setPixmap(logo_pixmap3)
        icon_label3.setGeometry(icon_left3, icon_top3, icon_label3_width, icon_label3_height)
        icon_label3.setToolTip("<h3 style='background-color: beige; color: black;'> FarmBot Genesis v1.6</h3>")

        #Label 1
        label = QLabel("Farmbot project 2023 : Sensors & GUI", self)
        font = label.font()
        font.setPointSize(32)  # Set the font size 
        font.setBold(True)
        label.setFont(font)
        label_width = 575
        label_height = 50
        label.setFixedSize(label_width, label_height)
        label.setAlignment(Qt.AlignCenter)
        label.move((self.width - label_width) / 2, (self.height - label_height) / 2 - 2 * self.button_height )
        label.setStyleSheet("background-color: transparent; color: white;")

        #Label 2
        label2 = QLabel("Create Lab - Concurrent Engineering Project (ME-314)", self)
        font2 = label2.font()
        font2.setItalic(True)
        font2.setPointSize(15) 
        label2.setFont(font2)
        label2_width = 1000
        label2_height = 100
        label2.setFixedSize(label2_width, label2_height)
        label2.setAlignment(Qt.AlignCenter)
        label2.move((self.width - label2_width) / 2, (self.height - label2_height) / 2 - 1.6 * self.button_height )
        label2.setStyleSheet("background-color: transparent; color: grey;")
        label2.setToolTip("<h3 style='background-color: beige; color: black;'>  Mechanical Engineering Faculty - Mandatory project for Bachelor students  </h3>")

        #Label 3
        label3 = QLabel("Mathieu Stawarz & Vincente Galdini", self)
        font3 = label3.font()
        font3.setPointSize(15)  # Set the font size to 16
        font3.setItalic(True)
        label3.setFont(font3)
        label3_width = 300
        label3_height = 50
        label3.setFixedSize(label3_width, label3_height)
        label3.setAlignment(Qt.AlignCenter)
        label3.move((self.width - label3_width) / 2, (self.height - label3_height) / 2 -  self.button_height )
        label3.setStyleSheet("background-color: transparent; color: white")
        label3.setToolTip("<h3 style='background-color: beige; color: black; border: none'> The motivated students who have worked on this project</h3>")
        #icon_label3.setStyleSheet("QToolTip { color: black; background-color: beige }")

        #window style and display
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    
    #Restart the video and plays it again
    def handle_media_status_changed(self, media_status):
        if media_status == QMediaPlayer.EndOfMedia:
            self.playerv.setPosition(0)  # Restart the video from the beginning
            self.playerv.play()

    # Opens 2nd window with delay and plays a nice launch music !
    def open_menuWindow(self): 
        self.player.stop() #stops start music
        #Plays launch music
        self.playerb = QMediaPlayer() #music button
        self.audio_outputb = QAudioOutput()
        self.playerb.setAudioOutput(self.audio_outputb)
        self.playerb.setSource(QUrl.fromLocalFile("GUI_medias/success.mp3"))
        self.audio_outputb.setVolume(50)
        self.playerb.play()
        #Push button update
        self.pushButton.setEnabled(False)  # Disable the button temporarily
        self.pushButton.setText("Launching ...")  # Set the button text clicks
        #Timer
        QTimer.singleShot(3000, self.show_menuWindow)  # Start a timer for delay (ms)

    #Show window and close main window
    def show_menuWindow(self):   
        self.playerb.stop()                                          # <===
        self.w = menuWindow() #Creates a new instance w
        self.w.show() #Show the new window 2
        self.close() #closes the main_window
