# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# XY_datachart.py
# XY chart widget class definition

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
import sys, math
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtWidgets import  QWidget, QHBoxLayout, QSizePolicy
from PySide6.QtCharts import QChart, QChartView, QLineSeries

# Only needed for access to command line arguments



# XYDataChart class definition

class XYDatachart(QWidget):
    def __init__(self, x_data, y_data, chartname, timerange ,timeunits, xunits, yunits, color): #color Qcolor
        super().__init__()

        self.x_data = x_data
        self.y_data = y_data

        #Creates the chart background
        self.chart = QChart()
        self.chart.setBackgroundBrush(QColor(25, 25, 25)) # chart background colour !!
        title = f'<span style="font-size: 20pt; color: {color.name()}; font-weight: bold;">{chartname}</span>' #the title is wrapped in an HTML <span> tag, and the font size and color are set using inline CSS style.
        self.chart.setTitle(title)

        #Creates Line series by appending x & y data to it and display it
        self.series = QLineSeries()
        for x, y in zip(x_data, y_data):
            self.series.append(x, y)
        self.chart.addSeries(self.series) #adds the series to the chart
        series_pen = QPen(color)  # Blue color with transparency
        series_pen.setWidth(4)  # Increase line thickness for plotted line
        series_pen.setJoinStyle(Qt.RoundJoin)  # Set round join style for smoother line
        self.series.setPen(series_pen)

        #set up axes for the chart 
        self.chart.createDefaultAxes()
        self.chart.legend().setVisible(False) #hide the default legend component.
        axes = self.chart.axes() #Axis pointer that returns a list of all the axes associated with the chart.

        # Customize X-axis
        x_axis = axes[0] #select axis x
        #xtitle = 'Last ' + timerange + '-' + timeunits 
        #Xtitle = f'<span style="font-size: 15pt; color: white;">{xtitle}</span>' # Set axis colour & size in HTML CSS style
        #x_axis.setTitleText(Xtitle)  # Set axis title
        x_axis.setLabelsColor(Qt.white) # Set axis labels colour
        x_axis_labels = x_axis.labelsFont()
        x_axis_labels.setPointSize(15)  # Set axis labels font size
        x_axis.setLabelsFont(x_axis_labels)
        x_axis.setTickCount(5) # Set the approximate number of ticks (labels) to be displayed on the X-axis
        xlabel_format =  "%.1f" + xunits # br HTML line break
        x_axis.setLabelFormat(xlabel_format)  # Format the labels to display one decimal place
        x_axis.setRange(max(x_data), min(x_data))  # Set the range of the X-axis

        # Customize Y-axis
        y_axis = axes[1] #select axis y
        y_axis_labels = y_axis.labelsFont()
        y_axis.setLabelsColor(Qt.white) # Set axis labels colour
        y_axis_labels.setPointSize(15)  # Set font size
        y_axis.setLabelsFont(y_axis_labels)
        y_axis.setTickCount( 3) # Set the approximate number of ticks (labels) to be displayed on the Y-axis
        ylabel_format = "%.1f" + yunits + '&nbsp;' #&nbsp; HTML non breaking spaces
        y_axis.setLabelFormat(ylabel_format)  # Format the labels to display one decimal place
        y_axis.setRange(min(y_data), max(y_data))  # Set the range of the X-axis

        # Customize grid color and style
        grid_pen = QPen(Qt.darkGray)  # Set grid color (gray in this case)
        dash_pattern = [2, 5, 8, 5]  # Custom dash pattern (alternating lengths of dashes and spaces)
        grid_pen.setStyle(Qt.CustomDashLine)
        grid_pen.setDashPattern(dash_pattern)
        x_axis.setGridLinePen(grid_pen)
        y_axis.setGridLinePen(grid_pen)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setContentsMargins(0, 0, 0, 0)


        layout = QHBoxLayout(self)  # Create a vertical layout
        layout.addWidget(self.chart_view)  # Add the chart view widget to the layout
        layout.setContentsMargins(0, 0, 0, 0)  # Remove any margins from the layout
        self.setLayout(layout)  # Set the layout for the XYDatachart widget

        self.setFixedSize(690, 240) #Set fixed size

