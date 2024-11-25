# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the line/bar example from Qt v5.x"""

import sys
from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QPainter, QColor
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from PySide6.QtCharts import (QBarCategoryAxis, QBarSeries, QBarSet, QChart,
                              QChartView, QLineSeries, QValueAxis)
from PySide6.QtCore import QTimer
import time


class ResultChart(QMainWindow):
    def __init__(self):
        super().__init__()

        self.set = {
            "obstacle":QBarSet("obstacle"),
            "ship":QBarSet("ship"),
            "bank":QBarSet("bank")}

        self.bar_series = QBarSeries()
        for k in self.set:
            if k == "obstacle":
                self.set[k].setColor(QColor(27,211,60))
            elif k == "ship":
                self.set[k].setColor(QColor(233,16,62))
            elif k == "bank":
                self.set[k].setColor(QColor(222,214,9))    
            self.bar_series.append(self.set[k])

        self.line_series = QLineSeries()
        self.line_series.setColor(QColor(27,130,211))
        self.line_series.setName("total")

        self.chart = QChart()
        self.chart.addSeries(self.bar_series)
        self.chart.addSeries(self.line_series)
        self.chart.setTitle("监控结果")
        self.chart.setBackgroundVisible(False)
        # self.chart.setTheme(QChart.ChartTheme.ChartThemeBlueIcy)

        self.axis_x = QValueAxis()
        self.axis_x.setLabelFormat("%i s")  # 设置X轴标签格式为秒"% i s"
        self.axis_x.setTitleText("Time (s)")  # 设置X轴标题
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)  # 将X轴添加到图表底部
        self.line_series.attachAxis(self.axis_x)
        self.bar_series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 40)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.line_series.attachAxis(self.axis_y)
        self.bar_series.attachAxis(self.axis_y)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self.chart_view)

        # 初始化定时器，用于定期数据
        self.timer = QTimer(self, interval=100)  # 设置定时器更新间隔为100毫秒
        self.timer.timeout.connect(self.update)  # 定时器超时触发update_cpu_usage函数
        self.timer.start()  # 启动定时器
        self.current_time = time.time()

        self.total = 0


    def change_value(self, value):
        self.total = 0
        for k,v in value.items():
            self.total += v
            self.set[k].append(v)

    def update(self):
        # # 获取当前时间戳
        current_time = time.time()
        now_time = current_time - self.current_time

        # 获取GPU的当前使用率
        self.line_series.append(now_time, self.total)

        # 更新图表的X轴范围，设置为当前时间减去60秒到当前时间，确保显示最近60秒的数据
        self.chart.axisX().setRange(now_time-30, now_time)

        # 调用图表的重绘方法，以更新显示
        self.chart_view.repaint()

