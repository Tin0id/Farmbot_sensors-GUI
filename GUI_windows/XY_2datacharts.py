# Farmbot project 2023, Sensors & GUI, Mathieu Stawarz
# XY_2datachart.py
# XY chart widget class definition
# Plots a XY chart with 2lines

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
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtWidgets import  QWidget, QHBoxLayout
from PySide6.QtCharts import QChart, QChartView, QLineSeries

# Only needed for access to command line arguments

class XY2Datachart(QWidget):
    def __init__(self, x_data, y1_data, y2_data, chartname1, chartname2, xunits, yunits, color1, color2):
        super().__init__()

        self.x_data = x_data
        self.y1_data = y1_data
        self.y2_data = y2_data

        self.chart = QChart()
        self.chart.setBackgroundBrush(QColor(25, 25, 25))
        title = f'<span style="font-size: 20pt; font-weight: bold; color: {color1.name()}">{chartname1}</span>' \
                f'<span style="font-size: 20pt; font-weight: bold; color: white">{" & "}</span>' \
                f'<span style="font-size: 20pt; font-weight: bold; color: {color2.name()}">{chartname2}</span>' 
        self.chart.setTitle(title)

        self.series1 = QLineSeries()
        self.series2 = QLineSeries()

        for x, y1, y2 in zip(x_data, y1_data, y2_data):
            self.series1.append(x, y1)
            self.series2.append(x, y2)

        self.chart.addSeries(self.series1)
        self.chart.addSeries(self.series2)

        series_pen1 = QPen(color1)
        series_pen1.setWidth(3)
        series_pen1.setJoinStyle(Qt.RoundJoin)
        self.series1.setPen(series_pen1)

        series_pen2 = QPen(color2)
        series_pen2.setWidth(3)
        series_pen2.setJoinStyle(Qt.RoundJoin)
        self.series2.setPen(series_pen2)

        self.chart.createDefaultAxes()
        self.chart.legend().setVisible(False)

        axes = self.chart.axes()

        x_axis = axes[0]
        x_axis.setLabelsColor(Qt.white)
        x_axis_labels = x_axis.labelsFont()
        x_axis_labels.setPointSize(15)
        x_axis.setLabelsFont(x_axis_labels)
        x_axis.setTickCount(6)
        xlabel_format =  "%.1f" + xunits
        x_axis.setLabelFormat(xlabel_format)
        x_axis.setRange(max(x_data), min(x_data))

        y_axis = axes[1]
        y_axis_labels = y_axis.labelsFont()
        y_axis.setLabelsColor(Qt.white)
        y_axis_labels.setPointSize(15)
        y_axis.setLabelsFont(y_axis_labels)
        y_axis.setTickCount(5)
        ylabel_format1 = "%.1f" + '&nbsp;' + yunits + '&nbsp;'
        y_axis.setLabelFormat(ylabel_format1)
        # Get the minimum and maximum values from both y1_data and y2_data
        y_min = min(min(y1_data), min(y2_data))
        y_max = max(max(y1_data), max(y2_data))
        y_axis.setRange(y_min, y_max)

        grid_pen = QPen(Qt.darkGray)
        dash_pattern = [2, 5, 8, 5]
        grid_pen.setStyle(Qt.CustomDashLine)
        grid_pen.setDashPattern(dash_pattern)
        x_axis.setGridLinePen(grid_pen)
        y_axis.setGridLinePen(grid_pen)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setContentsMargins(0, 0, 0, 0)

        layout = QHBoxLayout(self)
        layout.addWidget(self.chart_view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.setFixedSize(690, 240)
