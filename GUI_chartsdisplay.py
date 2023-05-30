# Farmbot project 2023, Sensors & UI, Mathieu Stawarz
# GUI_chartdisplays.py
# pyside6 GUI test display

# Pyside6 module :
# pip3 install pyside6
# Qt charts module install
# https://www.qt.io/qt-for-python : official website
# Tutorial : https://www.pythonguis.com/pyside6-tutorial/
#Plotting pyside6 : https://www.pythonguis.com/tutorials/pyside6-plotting-pyqtgraph/

#
#
# Modules imports
#
#
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QLineSeries

# Only needed for access to command line arguments


#
#
# GUI code
#
#

# Pie chart widget
class Piechart(QWidget):
    def __init__(self):
        super().__init__()
        self.series = QPieSeries()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)

        self.series.append('Jane', 1)
        self.series.append('Joe', 5)
        self.series.append('Andy', 3)
        self.series.append('Barbara', 4)
        self.series.append('Axel', 5)

        self.slice = self.series.slices()[1]
        self.slice.setExploded()
        self.slice.setLabelVisible()
        self.slice.setPen(QPen(Qt.darkGreen, 2))
        self.slice.setBrush(Qt.green)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle('Simple piechart example')
        self.chart.legend().hide()

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)
        


class XYDataChart(QWidget):
    def __init__(self, x_data, y_data):
        super().__init__()
        self.x_data = x_data
        self.y_data = y_data

        self.chart = QChart()
        self.chart.setTitle('XY Data Chart')

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)

        self.series = QLineSeries()
        for x, y in zip(x_data, y_data):
            self.series.append(x, y)
        self.chart.addSeries(self.series)

        self.chart.createDefaultAxes()
        self.chart.legend().setVisible(False)

        series_pen = QPen(QColor("#FF00FF"))  # Shiny red color
        series_pen.setWidth(4)  # Increase line thickness for plotted line
        self.series.setPen(series_pen)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(palette)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        layout = QVBoxLayout()
        layout.addWidget(self.chart_view)
        self.setLayout(layout)

        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # When you subclass a Qt class you must always call 
        # the super __init__ function to allow Qt to set up the object.
        layout = QGridLayout()
        self.setWindowTitle("My App")
        self.setStyleSheet("background-color: black;")

        x_data = [1, 2, 3, 4, 5]
        y_data = [1, 4, 9, 16, 25]

        chart1 = Piechart()
        chart2 = XYDataChart(x_data,y_data)
        chart3 = Piechart()
        chart4 = XYDataChart(x_data,y_data)

        widget = QWidget()
        widget.setLayout(layout)
        widget.setStyleSheet("background-color: black;")
        self.setCentralWidget(widget)

        layout.addWidget(chart1._chart_view, 0, 0)
        layout.addWidget(chart2, 1, 0)
        layout.addWidget(chart3._chart_view, 1, 1)
        layout.addWidget(chart4, 2, 1)




# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# window = QWidget()
window = MainWindow()
window.resize(2000, 1500)
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()

# Your application won't reach here until you exit and the event
# loop has stopped.





