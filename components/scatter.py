import sys
import random
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtCharts import QScatterSeries, QChart, QChartView, QPolarChart

class Scatter(QMainWindow):
    def __init__(self):
        super(Scatter, self).__init__()
        self.chart = QChart()
        self.chartView = QChartView()

        bbox = [[[random.random(), random.random()],[random.random(), random.random()],[random.random(), random.random()]],
                 [[random.random(),random.random()],[random.random(),random.random()]],
                 [[random.random(),random.random()],[random.random(),random.random()],[random.random(), random.random()],[random.random(),random.random()]]]
        
        self.set = {
            "obstacle": bbox,
            "ship": bbox,
            "bank": bbox
        }

        self.set_scatter = {
            "obstacle": QScatterSeries(),
            "ship": QScatterSeries(),
            "bank": QScatterSeries()
        }
        for k in self.set_scatter:
            self.set_scatter[k]
            for box in self.set[k]:
                for point in box:
                    x, y = point
                    self.set_scatter[k].append(int(x * 2404), y * 1080)
        
        pen = QPen()
        pen.setColor(Qt.white)
        pen.setWidth(1)
        for k in self.set_scatter:
            self.set_scatter[k].setMarkerSize(8)
            self.set_scatter[k].setMarkerShape(QScatterSeries.MarkerShapeCircle) # 圆形标记
            if k == "obstacle":
                self.set_scatter[k].setColor(QColor(27,211,60))
            elif k == "ship":
                self.set_scatter[k].setColor(QColor(233,16,62))
            elif k == "bank":
                self.set_scatter[k].setColor(QColor(222,214,9)) 
            self.set_scatter[k].setPen(pen)
            self.chart.addSeries(self.set_scatter[k])

        self.chart.setBackgroundVisible(False)
        self.chart.createDefaultAxes()
        self.chart.setTitle("边界框x-y分布图")
        
        self.chartView.setChart(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(self.chartView)

        self.timer = QTimer(self, interval=100)  # 设置定时器更新间隔为100毫秒
        self.timer.timeout.connect(self.update_scatter)
        self.timer.start(100)  # 启动定时器

    def change_value(self, boxes):
        self.set = boxes

    def update_scatter(self):
        
        for k in self.set_scatter:
            self.set_scatter[k].clear()
            for box in self.set[k]:
                cnt = 0 # 每个box最多统计50对x y
                for point in box:
                    x, y = point
                    self.set_scatter[k].append(int(x * 2404), y * 1080)
                    
                    cnt += 1
                    if cnt >= 50:
                        break
        self.chartView.repaint()




