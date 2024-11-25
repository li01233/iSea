# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the Pie Chart Example from Qt v5.x"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtCharts import QChart, QChartView, QPieSeries,QPieSlice
from PySide6.QtCore import QTimer

class Pie(QMainWindow):

    def __init__(self):
        super().__init__()

        self.set = {
            "obstacle":QPieSlice("obstacle",10),
            "ship":QPieSlice("ship",10),
            "bank":QPieSlice("bank",10)}
        
        self.series = QPieSeries()
        for k in self.set:
            self.set[k].setLabelVisible(True)
            if k == "obstacle":
                self.set[k].setColor(QColor(27,211,60))
            elif k == "ship":
                self.set[k].setColor(QColor(233,16,62))
                self.set[k].setExploded(True)
            elif k == "bank":
                self.set[k].setColor(QColor(222,214,9))    
            self.series.append(self.set[k])

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setBackgroundVisible(False)
        # self.chart.legend().hide()
        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(self._chart_view)

        # 初始化定时器，用于定期更新数据
        self.timer = QTimer(self, interval=100)  # 设置定时器更新间隔为100毫秒
        self.timer.timeout.connect(self.update) 
        self.timer.start(100)  # 启动定时器
        self.value = {}

    def change_value(self, value):
        for k in value:
            self.set[k].setValue(value[k])

