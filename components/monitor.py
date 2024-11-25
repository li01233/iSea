import sys, psutil, time,datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCharts import QChart, QLineSeries, QValueAxis, QChartView,QDateTimeAxis,QAreaSeries
from PySide6.QtCore import Qt, QTimer, QPointF
from PySide6.QtGui import QGradient, QPen, QLinearGradient, QColor

# 定义一个用于监控CPU使用率的主窗口类
class CPUUsageMonitor(QMainWindow):
    def __init__(self):
        """
        初始化CPU核心使用率监控窗口。
        """
        super().__init__()  # 调用父类构造函数

        # 设置窗口标题和大小
        self.setWindowTitle("CPU 核心利用率")
        self.resize(400, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志为无边框窗口。
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置window背景为透明

        # 初始化图表和标题
        self.chart = QChart()
        self.chart.setTitle("CPU 核心利用率")
        self.chart.setBackgroundVisible(False)
        self.chart.setTheme(QChart.ChartTheme.ChartThemeBlueIcy)
        
        
        # 创建一个系列列表，为每个CPU核心创建一个独立的系列
        self.series_list = []
        for i in range(psutil.cpu_count()):
            if i > 3:
                break
            series = QLineSeries()
            series.setName(f"Core {i}")  # 设置系列名称为CPU核心编号
            self.series_list.append(series)
            self.chart.addSeries(series)  # 将系列添加到图表中

        # 初始化并设置X轴（时间轴）
        self.axis_x = QValueAxis()
        self.axis_x.setLabelFormat("%i s")  # 设置X轴标签格式为秒"% i s"
        self.axis_x.setTitleText("Time (s)")  # 设置X轴标题
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)  # 将X轴添加到图表底部
        for series in self.series_list:
            series.attachAxis(self.axis_x)  # 将每个系列绑定到X轴


        # 初始化并设置Y轴（CPU使用率轴）
        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 100)  # 设置Y轴范围为0-100，对应CPU使用率百分比
        self.axis_y.setTitleText("CPU 占用率 (%)")  # 设置Y轴标题
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)  # 将Y轴添加到图表左侧
        for series in self.series_list:
            series.attachAxis(self.axis_y)  # 将每个系列绑定到Y轴

        # 将图表视图设置为窗口的中心小部件
        self.chart_view = QChartView(self.chart)
        self.setCentralWidget(self.chart_view)
        
        # 初始化定时器，用于定期更新CPU使用率数据
        self.timer = QTimer(self, interval=100)  # 设置定时器更新间隔为500毫秒
        self.timer.timeout.connect(self.update_cpu_usage)  # 定时器超时触发update_cpu_usage函数
        self.timer.start()  # 启动定时器
        self.current_time = time.time() # 最开始的时间
        self.per_cpu_percent = [] # 存储CPU状态


    def change_cpu(self, per_cpu_percent):
        self.per_cpu_percent = per_cpu_percent

    # 更新CPU使用率数据
    def update_cpu_usage(self):
        """
        更新CPU使用率数据。
        无参数
        无返回值

        此方法通过调用psutil.cpu_percent获取当前每个CPU核心的使用率，并将数据点添加到对应的核心系列中。
        同时，更新图表的X轴范围，确保只显示最近60秒的数据。
        """

        # # 获取当前时间戳
        current_time = time.time()
        now_time = current_time - self.current_time
        # 遍历每个CPU核心的使用率，将其作为一个新数据点添加到对应的系列中
        for i, usage in enumerate(self.per_cpu_percent):
            if i > 3:
                break
            self.series_list[i].append(now_time, usage)

        # 更新图表的X轴范围，设置为当前时间减去60秒到当前时间，确保显示最近60秒的数据
        self.chart.axisX().setRange(now_time-30, now_time)
        # 调用图表的重绘方法，以更新显示
        self.chart_view.repaint()

class GPUUsageMonitor(QMainWindow):
    def __init__(self):
        """
        初始化CPU核心使用率监控窗口。
        """
        super().__init__()  # 调用父类构造函数

        # 设置窗口标题和大小
        self.setWindowTitle("GPU 核心利用率")
        self.resize(400, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置窗口标志为无边框窗口。
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置window背景为透明

        # 初始化图表和标题
        self.chart = QChart()
        self.chart.setTitle("GPU 核心利用率")
        self.chart.setBackgroundVisible(False)

        # 创建一个面积图的series
        self.series_0 = QLineSeries()
        self.series_1 = QLineSeries()
        self.series = QAreaSeries(self.series_0, self.series_1)

        self.pen = QPen(QColor(31, 84, 133))
        self.pen.setWidth(3)
        self.series.setPen(self.pen)

        self.series.setBrush(QColor(31, 84, 133))

        self.series.setName("GPU 0")  # 设置系列名称为GPU0
        self.chart.addSeries(self.series)  # 将系列添加到图表中

        # 初始化并设置X轴（时间轴）
        self.axis_x = QValueAxis()
        self.axis_x.setLabelFormat("%i s")  # 设置X轴标签格式为秒"% i s"
        self.axis_x.setTitleText("Time (s)")  # 设置X轴标题
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)  # 将X轴添加到图表底部
        self.series.attachAxis(self.axis_x)  # 将系列绑定到X轴

        # 初始化并设置Y轴（CPU使用率轴）
        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, 100)  # 设置Y轴范围为0-100，对应GPU使用率百分比
        self.axis_y.setTitleText("GPU 占用率 (%)")  # 设置Y轴标题
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)  # 将Y轴添加到图表左侧
        self.series.attachAxis(self.axis_y)  # 将每个系列绑定到Y轴

        # 将图表视图设置为窗口的中心小部件
        self.chart_view = QChartView(self.chart)
        self.setCentralWidget(self.chart_view)

        self.timer = QTimer(self, interval=100)  # 设置定时器更新间隔为500毫秒
        self.timer.timeout.connect(self.update_gpu_usage)  # 定时器超时触发update_cpu_usage函数
        self.timer.start()  # 启动定时器
        self.current_time = time.time()
        self.usage = 0
        

    def change_gpu(self, usage):
        self.usage = usage

    # 更新GPU使用率数据
    def update_gpu_usage(self):
        """
        更新GPU使用率数据。
        无参数
        无返回值
        """
        # # 获取当前时间戳
        current_time = time.time()
        now_time = current_time - self.current_time
        # 获取GPU的当前使用率
        self.series_1.append(now_time, self.usage)
        self.series_0.append(now_time, 0)

        # 更新图表的X轴范围，设置为当前时间减去60秒到当前时间，确保显示最近60秒的数据
        self.chart.axisX().setRange(now_time-30, now_time)
        # 调用图表的重绘方法，以更新显示
        self.chart_view.repaint()

