# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *
from PySide6.QtGui import QGuiApplication,QPixmap,QImage
from PySide6.QtCore import Qt,QThread
from PySide6.QtWidgets import QFileDialog

from inference.predict import APP_infer
from inference.augmentor import APP_aug

import webbrowser
import requests
import winreg
import os

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////
class AppFunctions(MainWindow):

    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")

    # 推理功能 ##################################################################################################
    # 推理多线程初始化
    def infer_multi_thread(self):
        self.predictorList.clear()
        self.predict_threadList.clear()
        for i in range(len(self.files_path)):
            self.predictorList.append(APP_infer(i,self.model_path,self.files_path[i]))
            thread = QThread()
            self.predict_threadList.append(thread)
    
        for idx in range(len(self.predict_threadList)):
            m = self.predictorList[idx]
            # 绑定子线程到主线程的信号
            m.infer_img.connect(self.set_infer_img)
            m.fps.connect(self.set_infer_fps)
            m.num_category.connect(self.set_num_category)
            m.num_objects.connect(self.set_num_objects)
            m.progress.connect(self.set_infer_progress)
            m.category.connect(self.set_infer_result)
            m.boxes.connect(self.set_infer_boxes)
            m.end.connect(self.infer_finish)
            
            # 绑定主线程到子线程的信号
            self.main2infer_signal_iou.connect(m.change_iou)
            self.main2infer_signal_conf.connect(m.change_conf)
            self.main2infer_signal_save_result.connect(m.change_save_result)
            self.main2infer_signal_save_label.connect(m.change_save_label)

            self.main2infer_signal_begin.connect(m.run)

            m.moveToThread(self.predict_threadList[idx])
    
    # 初始化推理子进程模型参数
    def init_infer_param(self):
        self.main2infer_signal_save_result.emit(self.save_result)
        self.main2infer_signal_save_label.emit(self.save_label)
        self.main2infer_signal_iou.emit(self.iou)
        self.main2infer_signal_conf.emit(self.conf)

    # 开始推理，向predictor发送开始信号
    def start_inference(self):
        self.main2infer_signal_begin.emit()

    # 退出推理子进程
    def stop_inference(self):
        for m in self.predictorList:
            m.run_stop() # 退出推理器

        for thread in self.predict_threadList:
            if thread.isRunning():
                thread.quit() # 退出进程 quit()
                thread.wait()

        for m in self.predictorList:
            m.deleteLater() # 删除推理器

        for thread in self.predict_threadList: # 删除进程
            thread.deleteLater()

    # 增强功能 ##################################################################################################
    # 增强多线程初始化
    def aug_multi_thread(self):
        self.augmentorList.clear()
        self.aug_threadList.clear()
        for i in range(len(self.files_path)):
            self.augmentorList.append(APP_aug(i,self.files_path[i]))
            thread = QThread()
            self.aug_threadList.append(thread)
    
        for idx in range(len(self.aug_threadList)):
            m = self.augmentorList[idx]
            # 绑定子线程到主线程的信号
            m.aug_img.connect(self.set_aug_img)
            m.pre_img.connect(self.set_pre_img)
            m.progress.connect(self.set_aug_progress)
            m.end.connect(self.aug_finish)
            
            # 绑定主线程到子线程的信号
            self.main2aug_signal_fog.connect(m.change_fog)
            self.main2aug_signal_dusk.connect(m.change_dusk)
            self.main2aug_signal_rain.connect(m.change_rain)
            self.main2aug_signal_night.connect(m.change_night)
            self.main2aug_signal_fog_param.connect(m.change_fog_param)
            self.main2aug_signal_rain_param.connect(m.change_rain_param)
            self.main2aug_signal_night_param.connect(m.change_night_param)
            self.main2aug_signal_dusk_param.connect(m.change_dusk_param)

            self.main2aug_signal_begin.connect(m.run)

            m.moveToThread(self.aug_threadList[idx])
    
    # 初始化推理子进程模型参数
    def init_aug_param(self):
        self.main2aug_signal_fog.emit(self.fog)
        self.main2aug_signal_dusk.emit(self.dusk)
        self.main2aug_signal_rain.emit(self.rain)
        self.main2aug_signal_night.emit(self.night)
        self.main2aug_signal_fog_param.emit(self.fog_param)
        self.main2aug_signal_rain_param.emit(self.rain_param)
        self.main2aug_signal_night_param.emit(self.night_param)
        self.main2aug_signal_dusk_param.emit(self.dusk_param)

    # 开始增强，向augmentor发送开始信号
    def start_aug(self):
        self.main2aug_signal_begin.emit()

    # 退出增强子进程
    def stop_aug(self):
        for m in self.augmentorList:
            m.run_stop() # 退出增强器

        for thread in self.aug_threadList:
            if thread.isRunning():
                thread.quit() # 退出进程 quit()
                thread.wait()

        for m in self.augmentorList:
            m.deleteLater() # 删除增强器
        for thread in self.aug_threadList: # 删除进程
            thread.deleteLater()

    # 监控功能 #############################################################################################
    def monitor_multi_thread(self):
        self.main2monitorpannel_signal_cpu.connect(self.ui.cpu_gauge.setValue)
        self.main2monitorpannel_signal_gpu.connect(self.ui.gpu_gauge.setValue)

        self.main2monitorchart_signal_cpu.connect(self.cpu_monitor.change_cpu) # 给的是一个列表
        self.main2monitorpannel_signal_gpu.connect(self.gpu_monitor.change_gpu)

        self.main2monitortemp_signal_cpu.connect(self.ui.cpu_temperature.setValue)
        self.main2monitortemp_signal_gpu.connect(self.ui.gpu_temperature.setValue)
    
    def start_monitor(self):
        # 用于改变label的数字和向仪表盘发送数据，绑定了change_monitor
        self.timer_3.start(100)

    # 投影展示功能 ####################################################################################
    def proj_show_multi_thread(self):
        # FPS CPU GPU 仪表盘绑定
        self.main2monitorpannel_signal_cpu.connect(self.ui.cpu_usage.setValue)
        self.main2monitorpannel_signal_gpu.connect(self.ui.gpu_usage.setValue)
        self.main2projfps_signal_fps.connect(self.ui.fps_gauge.change_value)
        # 散点图 饼图 折线图绑定
        self.main2projchart_signal_category.connect(self.res_chart.change_value)
        self.main2projpie_signal_category.connect(self.res_pie.change_value)
        self.main2projscatter_signal_bbox.connect(self.res_scatter.change_value)


    # 按钮功能 #####################################################################################
    # 打开帮助文档 #################################
    def openDocument(self):
        os.startfile("help.pdf")

    # 保存截屏
    def saveScreen(self):
        saveScreen_Path, _ = QFileDialog.getSaveFileName(self,"打开保存截图目录","./output",".jpg")
        screen = QGuiApplication.primaryScreen()
        pixmap = screen.grabWindow(0)
        pixmap.save(saveScreen_Path + ".jpg", "jpg")
    
    # 打开官网
    def openUrl(self, url):
        webbrowser.open(url)

    # 开机显示1秒LOGO
    def show_logo(self):
        # 展示1秒LOGO就切换页面
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.change_page)
        self.timer.start(1000)
    
    
    # 时钟设置
    def set_time(self):
        # 每一秒更新一下时钟
        self.timer_2 = QTimer()
        self.timer_2.timeout.connect(self.change_pagenowtime)
        self.timer_2.start(1000)

    
    # 天气设置
    def set_weather(self, cityName):
        self.ui.lb_city.setText(cityName)
        
        # 获取天气并设置天气
        def getCode(cityName):
            cityDict = {"青岛": "370200"}
            return cityDict.get(cityName, '101010100')
        cityCode = getCode(cityName)
        r = requests.get(\
            "https://restapi.amap.com/v3/weather/weatherInfo?key=086607ab379791b53b1db9819f7e1b86&city={}".format(
                cityCode))
        if r.status_code == 200:
            data = r.json()['lives'][0]
            self.ui.lb_temp.setText(data['temperature']+"℃")
            self.ui.lb_windpower.setText(data['windpower'])
            self.ui.lb_winddirection.setText(data['winddirection'])
            self.ui.lb_humidity.setText(data['humidity'])
            self.ui.lb_weather.setText(data['weather'])

            icon = getWeatherIcon(data['weather'])
            self.ui.btn_weather.setStyleSheet("border-image: {};".format(icon))
        else:
            print('天气查询失败，请稍后再试！')

    def get_CPUGPUname(self):
        # 打开注册表
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
        # QueryValueEx 获取指定注册表中指定字段的内容
        cpu_name = winreg.QueryValueEx(key, "ProcessorNameString")[0]  # 获取cpu名称
        key.Close()
        
        gpu_name = pynvml.nvmlDeviceGetName(handle=self.handle)
        return cpu_name, gpu_name 

def getWeatherIcon(weather):
    weatherDict = {
        "少云": "url(:/weather/images/weather/晴天.png)",
        "晴": "url(:/weather/images/weather/晴天.png)",
        "晴间多云": "url(:/weather/images/weather/晴转多云.png)",
        "多云": "url(:/weather/images/weather/多云.png)",
        "阴": "url(:/weather/images/weather/阴天.png)",
        "有风": "url(:/weather/images/weather/微风.png)",
        "微风": "url(:/weather/images/weather/微风.png)",
        "和风": "url(:/weather/images/weather/微风.png)",
        "清风": "url(:/weather/images/weather/微风.png)",
        "强风": "url(:/weather/images/weather/大风.png)",
        "劲风": "url(:/weather/images/weather/大风.png)",
        "疾风": "url(:/weather/images/weather/大风.png)",
        "大风": "url(:/weather/images/weather/大风.png)",
        "烈风": "url(:/weather/images/weather/飓风.png)",
        "风暴": "url(:/weather/images/weather/飓风.png)",
        "狂爆风": "url(:/weather/images/weather/飓风.png)",
        "飓风": "url(:/weather/images/weather/飓风.png)",
        "热带风暴": "url(:/weather/images/weather/台风.png)",
        "霾": "url(:/weather/images/weather/雾霾.png)",
        "中度霾": "url(:/weather/images/weather/雾霾.png)",
        "重度霾": "url(:/weather/images/weather/雾霾.png)",
        "严重霾": "url(:/weather/images/weather/雾霾.png)",
        "阵雨": "url(:/weather/images/weather/晴转多云.png)",
        "雷阵雨": "url(:/weather/images/weather/雷阵雨.png)",
        "雷阵雨并伴有冰雹": "url(:/weather/images/weather/雷阵雨加冰雹.png)",
        "小雨": "url(:/weather/images/weather/小雨.png)",
        "中雨": "url(:/weather/images/weather/中雨.png)",
        "大雨": "url(:/weather/images/weather/大雨.png)",
        "暴雨": "url(:/weather/images/weather/暴雨.png)",
        "大暴雨": "url(:/weather/images/weather/大暴雨.png)",
        "特大暴雨": "url(:/weather/images/weather/特大暴雨.png)",
        "强阵雨": "url(:/weather/images/weather/阵雨.png)",
        "强雷阵雨": "url(:/weather/images/weather/雷阵雨.png)",
        "极端降雨": "url(:/weather/images/weather/雷电.png)",
        "毛毛雨": "url(:/weather/images/weather/小雨.png)",
        "细雨": "url(:/weather/images/weather/小雨.png)",
        "雨": "url(:/weather/images/weather/小雨.png)",
        "雨夹雪": "url(:/weather/images/weather/雨夹雪.png)",
        "阵雨夹雪": "url(:/weather/images/weather/阵雪.png)",
        "冻雨": "url(:/weather/images/weather/冻雨.png)",
        "雪": "url(:/weather/images/weather/小雪.png)",
        "阵雪": "url(:/weather/images/weather/阵雪.png)",
        "小雪": "url(:/weather/images/weather/小雪.png)",
        "中雪": "url(:/weather/images/weather/中雪.png)",
        "大雪": "url(:/weather/images/weather/大雪.png)",
        "暴雪": "url(:/weather/images/weather/暴雪.png)",
        "特大暴雪": "url(:/weather/images/weather/特大暴雪.png)",
        "浮尘": "url(:/weather/images/weather/浮尘.png)",
        "扬沙": "url(:/weather/images/weather/扬沙.png)",
        "沙尘暴": "url(:/weather/images/weather/沙尘暴.png)",
        "强沙尘暴": "url(:/weather/images/weather/强沙尘暴.png)",
        "龙卷风": "url(:/weather/images/weather/强沙尘暴.png)",
        "雾": "url(:/weather/images/weather/雾.png)",
        "浓雾": "url(:/weather/images/weather/雾.png)",
        "强浓雾": "url(:/weather/images/weather/雾.png)",
        "轻雾": "url(:/weather/images/weather/雾.png)", 
        "特强浓雾": "url(:/weather/images/weather/雾.png)", 
        "热": "url(:/weather/images/weather/暖锋.png)", 
        "冷": "url(:/weather/images/weather/冷锋.png)",
    }
    return weatherDict.get(weather)          