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

import sys
import os
import platform
import datetime
import pynvml
import psutil
import numpy as np
import sys
import random

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%
from components.new_widget import InferRessult

from components.chart import ResultChart
from components.monitor import (CPUUsageMonitor, GPUUsageMonitor)
from components.pie import Pie
from components.scatter import Scatter

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    # The main window sends an execution signal to the yolo instance
    # 定义主进程到推理子线程的信号
    main2infer_signal_iou = Signal(float)
    main2infer_signal_conf = Signal(float)
    main2infer_signal_save_result = Signal(bool)
    main2infer_signal_save_label = Signal(bool)
    main2infer_signal_begin = Signal() # 开始信号

    # 定义主进程到增强子线程的信号
    main2aug_signal_fog = Signal(bool)
    main2aug_signal_dusk = Signal(bool)
    main2aug_signal_night = Signal(bool)
    main2aug_signal_rain = Signal(bool)
    main2aug_signal_fog_param = Signal(float)
    main2aug_signal_dusk_param = Signal(float)
    main2aug_signal_night_param = Signal(float)
    main2aug_signal_rain_param = Signal(float)
    main2aug_signal_begin = Signal() # 开始信号

    # 定义主进程到监控页仪表盘子线程的信号
    main2monitorpannel_signal_gpu = Signal(float)
    main2monitorpannel_signal_cpu = Signal(float)

    # 定义主进程到监控页绘图仪子线程的信号
    main2monitorchart_signal_cpu = Signal(list)

    # 定义主进程到监控页温度计子线程的信号
    main2monitortemp_signal_gpu = Signal(float)
    main2monitortemp_signal_cpu = Signal(float)

    # 定义主进程到投影页绘图仪子线程信号
    main2projchart_signal_category = Signal(dict)

    # 定义主进程到投影页饼图子线程信号
    main2projpie_signal_category = Signal(dict)

    # 定义主进程到投影页散点图子线程信号
    main2projscatter_signal_bbox = Signal(dict)

    # 定义主进程到投影页fps子线程信号
    main2projfps_signal_fps = Signal(float)

    # 定义主进程到双击放大子线程信号
    main2click_signal_img = Signal(np.ndarray) # 发送推理到的图片
    
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "iSea"
        description = "iSea"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # 参数初始化
        self.param_init()
        # 初始化控件
        self.control_init()

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.bind()
        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = True
        self.themeFile = ["themes\my_theme.qss", "themes\py_dracula_dark.qss", "themes\py_dracula_light.qss"]
        self.theme_idx = 0

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, self.themeFile[self.theme_idx], True)
            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.welcome_page)
        AppFunctions.show_logo(self)

    #############################################################################################################
        
    def param_init(self): # 设置参数初始状态
        ######################抽屉：增强参数######################################
        # 初始化每种增强的状态
        self.fog = True
        self.rain = True
        self.dusk = True
        self.night = True
        # 初始化每种增强的参数
        self.fog_param = 0.95
        self.rain_param = 0.65
        self.dusk_param = 0.65
        self.night_param = 1.0

        ########################抽屉：模型参数######################################
        # 初始化模型文件路径
        self.model_save_dir = './model'
        self.model_name_list = self.grap_model(self.model_save_dir) #获取model文件夹下所有model的名称
        if len(self.model_name_list) > 0:
            self.model_path = os.path.join(self.model_save_dir, self.model_name_list[0])
        else:
            QMessageBox.information(self, 'Wrong', "model下无模型文件,请自行选择文件路径", QMessageBox.StandardButton.Ok)
            self.model_path = None
        self.files_path = None
        # 初始化模型参数
        self.conf = 0.25
        self.iou = 0.7
        # 初始化模型保存状态
        self.save_label = False
        self.save_result = False

        ####################推理页####################################################
        self.infer_img = {"left": None, "right": None, "front": None, "back": None}
        self.detect_enable_pause = False
        self.aug_enable_pause = False

        ##############################进程管理###########################################
        self.predictorList = [] 
        self.predict_threadList = []# 存放子进程，每个角度一个推理器
        self.augmentorList = [] 
        self.aug_threadList = []# 增强子进程

        #####################组件管理####################################################
        self.lb_infer = [widgets.lb_front_img, widgets.lb_right_img, widgets.lb_left_img, widgets.lb_back_img]
        self.lb_aug_pre = [widgets.lb_aug_rain, widgets.lb_pre_dusk, widgets.lb_pre_night, widgets.lb_pre_fog]
        self.lb_aug_after = [widgets.lb_pre_rain, widgets.lb_aug_dusk, widgets.lb_aug_night, widgets.lb_aug_fog]
        self.aug_minProgress = 0
        self.detect_minProgress = 0
        
    
    def control_init(self): # 设置控件初始状态
        ######################抽屉：增强参数######################################
        widgets.spin_rain.setValue(self.rain_param)
        widgets.slider_rain.setValue(self.rain_param * 100)
        widgets.spin_fog.setValue(self.fog_param)
        widgets.slider_fog.setValue(self.fog_param * 100)
        widgets.spin_dusk.setValue(self.dusk_param)
        widgets.slider_dusk.setValue(self.dusk_param * 100)
        widgets.spin_night.setValue(self.night_param)
        widgets.slider_night.setValue(self.night_param * 100)
        widgets.check_dusk.setChecked(self.dusk)
        widgets.check_night.setChecked(self.night)
        widgets.check_fog.setChecked(self.fog)
        widgets.check_rain.setChecked(self.rain)

        ########################抽屉：模型参数######################################
        widgets.spin_iou.setValue(self.iou)
        widgets.spin_conf.setValue(self.conf)
        widgets.slider_iou.setValue(self.iou * 100)
        widgets.slider_conf.setValue(self.conf * 100)

        # 模型选项框
        widgets.combo_model_choose.addItems(self.model_name_list)
        
        ####################增强页####################################################
        widgets.aug_infer_progress.setValue(self.aug_minProgress) # 进度条
        
        # 设置暂停和停止按钮disable
        widgets.aug_Pause.setDisabled(True)
        widgets.aug_Close.setDisabled(True)

        ####################推理页####################################################
        widgets.detect_infer_progress.setValue(self.detect_minProgress) # 进度条
        
        # 设置暂停和停止按钮disable
        widgets.detect_Pause.setDisabled(True)
        widgets.detect_Close.setDisabled(True)

        # 设置推理页天气和地图
        # 设置天气和时间
        AppFunctions.set_weather(self, "青岛")
        AppFunctions.set_time(self)
        
        # 用于更新子窗口的图片
        # 实例化计时器并稳定更新
        self.timer_4 = QTimer()
        self.timer_4.timeout.connect(self.updateInferResult)

        # 实例化一个新窗口
        self.infer_widget = InferRessult()

        ####################监控页####################################################
        # 用于改变label的数字和向仪表盘发送数据
        self.timer_3 = QTimer()
        self.timer_3.timeout.connect(self.change_monitor)

        # 显示CPU GPU信息
        # 初始化显卡读取状态
        pynvml.nvmlInit()
        self.handle = pynvml.nvmlDeviceGetHandleByIndex(0) # 显卡句柄（只有一张显卡）
        cpu_name, gpu_name = AppFunctions.get_CPUGPUname(self)
        widgets.lb_cpu_info.setText(cpu_name)
        widgets.lb_gpu_info.setText(gpu_name)
        
        # 开始监控 ########################
        # 设置仪表盘显示
        widgets.cpu_gauge.setDevice("CPU")
        widgets.gpu_gauge.setDevice("GPU")
        # processring 显示占用
        widgets.cpu_gauge.show()
        widgets.gpu_gauge.show()
        # chart 显示占用
        self.cpu_monitor = CPUUsageMonitor()
        self.gpu_monitor = GPUUsageMonitor()
        widgets.layout_cpu_monitor.addWidget(self.cpu_monitor)
        widgets.layout_gpu_monitor.addWidget(self.gpu_monitor)
        self.cpu_monitor.show()
        self.gpu_monitor.show()
        # 显示温度
        widgets.cpu_temperature.show()
        widgets.gpu_temperature.show()
        # 显示磁盘占用
        widgets.device_memory.show()
        widgets.device_memory.verticalHeader().setDefaultSectionSize(60)
        # 绑定信号
        AppFunctions.monitor_multi_thread(self)
        AppFunctions.start_monitor(self)

        ####################投影页####################################################
        # 设置仪表盘显示
        widgets.cpu_usage.setDevice("CPU")
        widgets.gpu_usage.setDevice("GPU")
        # 显示时钟
        widgets.clock.show()
        # 显示cpu占用 gpu占用
        widgets.cpu_usage.show()
        widgets.gpu_usage.show()
        # 显示FPS
        widgets.fps_gauge.show()
        # 显示结果
        # 实例化三个绘图窗口
        self.res_chart = ResultChart()
        self.res_pie = Pie()
        self.res_scatter = Scatter()
        # 将其放于布局中
        widgets.layout_chart.addWidget(self.res_chart)
        widgets.layout_pie.addWidget(self.res_pie)
        widgets.layout_scatter.addWidget(self.res_scatter)
        # 显示
        self.res_chart.show()
        self.res_pie.show()
        self.res_scatter.show()
        # 绑定信号
        AppFunctions.proj_show_multi_thread(self)

    #############################################################################################################

    # 绑定信号区
    def bind(self):
        # TOGGLE MENU 隐藏功能区
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # BUTTONS CLICK 控件绑定信号区
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        # 切换不同页面
        widgets.btn_detect_page.clicked.connect(self.buttonClick)
        widgets.btn_aug_page.clicked.connect(self.buttonClick)
        widgets.btn_bev_page.clicked.connect(self.buttonClick)
        widgets.btn_monitor_page.clicked.connect(self.buttonClick)
        
        # 按检测和增强则显示侧边栏
        # EXTRA LEFT BOX
        def openCloseLeftBox_detect():
            UIFunctions.toggleLeftBox_detect(self, True)
        def openCloseLeftBox_aug():
            UIFunctions.toggleLeftBox_aug(self, True)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox_detect)
        widgets.extraCloseColumnBtn_2.clicked.connect(openCloseLeftBox_aug) 
        widgets.btn_detect.clicked.connect(openCloseLeftBox_detect)
        widgets.btn_aug.clicked.connect(openCloseLeftBox_aug)
        
        # 右侧设置栏
        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)
        # 设置菜单按钮
        widgets.btn_saveScreen.clicked.connect(self.buttonClick)
        widgets.btn_github.clicked.connect(self.buttonClick)
        widgets.btn_contact.clicked.connect(self.buttonClick)
        widgets.btn_theme.clicked.connect(self.buttonClick)
        widgets.link_btn.clicked.connect(self.buttonClick)

        # 打开文件
        widgets.btn_file.clicked.connect(self.openModel)
        # 帮助文档
        widgets.btn_help.clicked.connect(self.buttonClick)
        
        # 参数设置
        ## 增强参数 ################################################################
        widgets.check_dusk.stateChanged.connect(self.checkbox_click)
        widgets.check_fog.stateChanged.connect(self.checkbox_click)
        widgets.check_night.stateChanged.connect(self.checkbox_click)
        widgets.check_rain.stateChanged.connect(self.checkbox_click)

        widgets.spin_rain.valueChanged.connect(self.spin_change)
        widgets.spin_fog.valueChanged.connect(self.spin_change)
        widgets.spin_dusk.valueChanged.connect(self.spin_change)
        widgets.spin_night.valueChanged.connect(self.spin_change)
        
        widgets.slider_rain.valueChanged.connect(self.slide_change)
        widgets.slider_fog.valueChanged.connect(self.slide_change)
        widgets.slider_dusk.valueChanged.connect(self.slide_change)
        widgets.slider_night.valueChanged.connect(self.slide_change)


        ## 模型参数 ################################################################
        widgets.btn_model_choose.clicked.connect(self.openModel)
        widgets.combo_model_choose.currentIndexChanged.connect(self.openDefaultModel)

        widgets.spin_iou.valueChanged.connect(self.spin_change)
        widgets.slider_iou.valueChanged.connect(self.slide_change)

        widgets.spin_conf.valueChanged.connect(self.spin_change)
        widgets.slider_conf.valueChanged.connect(self.slide_change)

        widgets.check_save_img.stateChanged.connect(self.checkbox_click)
        widgets.check_save_label.stateChanged.connect(self.checkbox_click)

        ### 页面按钮 ##########################################################################
        # 设置增强页面按钮
        widgets.aug_Start.clicked.connect(self.buttonClick)
        widgets.aug_Pause.clicked.connect(self.buttonClick)
        widgets.aug_Close.clicked.connect(self.buttonClick)

        # 设置推理页面按钮
        widgets.detect_Start.clicked.connect(self.buttonClick)
        widgets.detect_Pause.clicked.connect(self.buttonClick)
        widgets.detect_Close.clicked.connect(self.buttonClick)
        widgets.btn_left_img.clicked.connect(self.buttonClick)
        widgets.btn_right_img.clicked.connect(self.buttonClick)
        widgets.btn_back_img.clicked.connect(self.buttonClick)
        widgets.btn_front_img.clicked.connect(self.buttonClick)
  
        # 绑定子界面更新信号
        self.main2click_signal_img.connect(self.infer_widget.update_img)


    #############################################################################################################   
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE ######################################################################
        # 按检测则显示检测界面
        if btnName == "btn_detect_page":
            widgets.stackedWidget.setCurrentWidget(widgets.detect_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 按增强则显示增强界面
        if btnName == "btn_aug_page":
            widgets.stackedWidget.setCurrentWidget(widgets.aug_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        
        # 按俯视图则显示俯视图界面
        # SHOW WIDGETS PAGE
        if btnName == "btn_bev_page":
            widgets.stackedWidget.setCurrentWidget(widgets.bev_page)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # 按仪表盘则显示监控界面
        if btnName == "btn_monitor_page":
            widgets.stackedWidget.setCurrentWidget(widgets.monitor_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        # 设置菜单栏对应按钮 ############################################################
        if btnName == "btn_saveScreen":
            AppFunctions.saveScreen(self)

        if btnName == "btn_github":
            AppFunctions.openUrl(self, "https://github.com/li01233")

        if btnName == "btn_contact":
            AppFunctions.openUrl(self, "https://smartship.cn/index.php")

        if btnName == "btn_theme":
            self.change_theme()
         
        if btnName == "link_btn":
            AppFunctions.openUrl(self, "https://github.com/li01233")

        if btnName == "btn_help":
            AppFunctions.openDocument(self)

        # 设置推理按钮 ################################################
        if btnName == "detect_Start":
            if self.files_path is None:
                QMessageBox.information(self, 'Error', "未选择推理文件", QMessageBox.StandardButton.Ok)
            elif self.model_path is None:
                QMessageBox.information(self, 'Error', "模型无法读取", QMessageBox.StandardButton.Ok)
            else:
                self.files_path = self.files_path[:4] if len(self.files_path) > 4 else self.files_path
                self.detect_start() 
                
        if btnName == "detect_Pause":
            self.detect_pause() 
            
        if btnName == "detect_Close":
            self.detect_stop()
        
        # 设置增强按钮 #################################################
        if btnName == "aug_Start":
            if self.files_path is None:
                QMessageBox.information(self, 'Error', "未选择推理文件", QMessageBox.StandardButton.Ok)
            elif self.model_path is None:
                QMessageBox.information(self, 'Error', "模型无法读取", QMessageBox.StandardButton.Ok)
            else:
                self.files_path = self.files_path[:4] if len(self.files_path) > 4 else self.files_path
                self.aug_start()
                
        if btnName == "aug_Pause":
            self.aug_pause()

        if btnName == "aug_Close":
            self.aug_stop()

        # 打开新窗口按钮#########################
        if btnName == "btn_left_img":
            self.openInferResult("left")
        if btnName == "btn_right_img":
            self.openInferResult("right")
        if btnName == "btn_back_img":
            self.openInferResult("back")
        if btnName == "btn_front_img":
            self.openInferResult("front")    

    # 打开模型文件按钮 ###############################
    def openModel(self):
        btn = self.sender()
        btnName = btn.objectName()
        
        if btnName == "btn_model_choose":
            self.model_path, _ = QFileDialog.getOpenFileName(self, "打开模型文件", "./model","*.pt")
        if btnName == "btn_file":
            self.files_path, _ = QFileDialog.getOpenFileNames(self, "打开推理图像或视频", "./input","*.png *.jpg *.mp4")

    def openDefaultModel(self, idx):
        self.model_path = os.path.join(self.model_save_dir, self.model_name_list[idx])
    
    # 打开大图
    def openInferResult(self, pos):
        img = self.infer_img[pos]
        self.infer_pos = pos
        if img is not None:
            # 显示子窗口
            self.infer_widget.show()
            # 计时器开始
            self.timer_4.start(100)
    
    def updateInferResult(self):
        self.main2click_signal_img.emit(self.infer_img[self.infer_pos])

    # check box集成 ###############################
    def checkbox_click(self, able):
        # GET check box CLICKED
        checkbox = self.sender()
        checkboxName = checkbox.objectName()

        if checkboxName == "check_rain":
            self.rain = True if able else False
            self.augmentorList[0].change_rain(self.rain)
            if self.rain:
                self.augmentorList[0].change_rain_param(self.rain_param)

        if checkboxName == "check_dusk":
            self.dusk = True if able else False
            self.augmentorList[1].change_dusk(self.dusk)
            if self.dusk:
                self.augmentorList[1].change_dusk_param(self.dusk_param)

        if checkboxName == "check_night":
            self.night = True if able else False
            self.augmentorList[2].change_night(self.night)
            if self.night:
                self.augmentorList[2].change_night_param(self.night_param)

        if checkboxName == "check_fog":
            self.fog = True if able else False
            self.augmentorList[3].change_fog(self.fog)
            if self.fog:
                self.augmentorList[3].change_fog_param(self.fog_param)

        if checkboxName == "check_save_img":
            self.save_result = True if able else False
            self.main2infer_signal_save_result.emit(self.save_result)
            
        if checkboxName == "check_save_label":
            self.save_label = True if able else False
            self.main2infer_signal_save_label.emit(self.save_label)
    
    # 滑条与数值框 ###############################
    def slide_change(self, value):
        slide = self.sender()
        slideName = slide.objectName()

        if slideName == "slider_iou":
            self.iou = value / 100
            widgets.spin_iou.setValue(self.iou)
            for m in self.predictorList:
                m.change_iou(self.iou)

        if slideName == "slider_conf":
            self.conf = value / 100
            widgets.spin_conf.setValue(self.conf)
            for m in self.predictorList:
                m.change_conf(self.conf)

        if slideName == "slider_rain":
            self.rain_param = value / 100
            widgets.spin_rain.setValue(self.rain_param)
            self.augmentorList[0].change_rain_param(self.rain_param)

        if slideName == "slider_dusk":
            self.dusk_param = value / 100
            widgets.spin_dusk.setValue(self.dusk_param)
            self.augmentorList[1].change_dusk_param(self.dusk_param)

        if slideName == "slider_fog":
            self.fog_param = value / 100
            widgets.spin_fog.setValue(self.fog_param)
            self.augmentorList[3].change_fog_param(self.fog_param)

        if slideName == "slider_night":
            self.night_param = value / 100
            widgets.spin_night.setValue(self.night_param)
            self.augmentorList[2].change_night_param(self.night_param)

    def spin_change(self, value):
        spin = self.sender()
        spinName = spin.objectName()

        if spinName == "spin_iou":
            self.iou = value
            widgets.slider_iou.setValue(self.iou * 100)
            for m in self.predictorList:
                m.change_iou(self.iou)

        if spinName == "spin_conf":
            self.conf = value
            widgets.slider_conf.setValue(self.conf * 100)
            for m in self.predictorList:
                m.change_conf(self.conf)

        if spinName == "spin_rain":
            self.rain_param = value
            widgets.slider_rain.setValue(self.rain_param * 100)
            self.augmentorList[0].change_rain_param(self.rain_param)
        
        if spinName == "spin_dusk":
            self.dusk_param = value
            widgets.slider_dusk.setValue(self.dusk_param * 100)
            self.augmentorList[1].change_dusk_param(self.dusk_param)
        
        if spinName == "spin_fog":
            self.fog_param = value
            widgets.slider_fog.setValue(self.fog_param * 100)
            self.augmentorList[3].change_fog_param(self.fog_param)

        if spinName == "spin_night":
            self.night_param = value
            widgets.slider_night.setValue(self.night_param * 100)
            self.augmentorList[2].change_night_param(self.night_param)


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips 拉伸window
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW 拖拽window
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


    ####一些功能性函数##########################################################
    def grap_model(self, dir):
        model_name = os.listdir(dir)
        return model_name
    
    # 改变主题
    def change_theme(self): 
        self.theme_idx += 1
        self.theme_idx %= 3
        UIFunctions.theme(self, self.themeFile[self.theme_idx], True)
        # SET HACKS
        AppFunctions.setThemeHack(self)
    
    # 槽函数 ###################################################################################################################
    def change_pagenowtime(self):
        # 当前时间
        current_time = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
        widgets.lb_nowtime.setText(current_time)

    def change_page(self):
        widgets.stackedWidget.setCurrentWidget(widgets.detect_page)
        widgets.btn_detect_page.setStyleSheet(UIFunctions.selectMenu(widgets.btn_detect_page.styleSheet()))

    
    # 主进程槽函数 #########################################################################################################
    ###推理#############################################################################################################
    # 将推理后图片放到label中
    def set_infer_img(self, idx, frame):
        # 将frame保存起来
        if idx % 4 == 0:
            self.infer_img["front"] = frame
        elif idx % 4 == 1:
            self.infer_img["right"] = frame
        elif idx % 4 == 2:
            self.infer_img["left"] = frame
        elif idx % 4 == 3:
            self.infer_img["back"] = frame

        infer_img = QImage(frame.data, frame.shape[1], frame.shape[0],
                                frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
        infer_img_1 = infer_img.scaled(widgets.lb_front_img.size(),Qt.KeepAspectRatio)
        self.lb_infer[idx].setPixmap(QPixmap.fromImage(infer_img_1))
        # 放到投影页中去
        if idx == 0:
            infer_img_2 = infer_img.scaled(widgets.lb_infer_front1.size(),Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            widgets.lb_infer_front1.setPixmap(QPixmap.fromImage(infer_img_2))
            widgets.lb_infer_front1.setAlignment(Qt.AlignmentFlag.AlignCenter)
            # size = widgets.lb_infer_front1.size()
            # desktop = 
            
    
    # 设置FPS 类别数 box数
    def set_infer_fps(self, fps):
        widgets.lb_fps.setText("{:.2f}".format(fps))
        self.main2projfps_signal_fps.emit(fps)

    def set_num_objects(self, num_objects):
        widgets.lb_object.setText(num_objects)

    def set_num_category(self, num_category):
        widgets.lb_category.setText(num_category)
    
    # 推理的字典结果
    def set_infer_result(self, result):
        # 投影页绘图
        self.main2projchart_signal_category.emit(result)
        self.main2projpie_signal_category.emit(result)
        # 滚动box
        for k,v in result.items():
            widgets.lb_information.append("type:"+str(k)+"\n"+"num:"+str(v)+"\n")

    def set_infer_boxes(self, bboxes):
        # 投影页绘图
        self.main2projscatter_signal_bbox.emit(bboxes)

    def infer_finish(self):
        AppFunctions.stop_inference(self)  # 退出进程
        # 按钮使能
        widgets.detect_Pause.setDisabled(True)
        widgets.detect_Close.setDisabled(True)
        widgets.detect_Start.setEnabled(True)
        
        widgets.btn_file.setEnabled(True)
        
        # 抽屉能用了
        widgets.check_save_img.setEnabled(True)
        widgets.check_save_label.setEnabled(True)
        widgets.combo_model_choose.setEnabled(True)
        widgets.btn_model_choose.setEnabled(True)

        self.detect_minProgress = 0
        widgets.detect_infer_progress.setValue(self.detect_minProgress)

        for lb in self.lb_infer:
            lb.clear()

    ###增强#############################################################################################################
    # 设置进度条
    def set_aug_progress(self, progress):
        if progress > self.aug_minProgress:
            self.aug_minProgress = progress
        widgets.aug_infer_progress.setValue(self.aug_minProgress)  

    def set_infer_progress(self, progress):  
        if progress > self.detect_minProgress:
            self.detect_minProgress = progress
        widgets.detect_infer_progress.setValue(self.detect_minProgress)
    
    # 设置增强图片
    def set_pre_img(self, idx, frame):
        ori_img = QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
        ori_img = ori_img.scaled(widgets.lb_pre_rain.size(),Qt.KeepAspectRatio)
        self.lb_aug_pre[idx].setPixmap(QPixmap.fromImage(ori_img))

    def set_aug_img(self, idx, frame):
        aug_img = QImage(frame.data, frame.shape[1], frame.shape[0],
                                frame.shape[2] * frame.shape[1],
                         QImage.Format_RGB888)
        aug_img = aug_img.scaled(widgets.lb_aug_rain.size(),Qt.KeepAspectRatio)
        self.lb_aug_after[idx].setPixmap(QPixmap.fromImage(aug_img))

    def aug_finish(self):
        AppFunctions.stop_aug(self)  # 退出进程
        # 改变控件状态
        # 按钮使能
        widgets.aug_Pause.setDisabled(True)
        widgets.aug_Close.setDisabled(True)
        widgets.aug_Start.setEnabled(True)

        widgets.btn_file.setEnabled(True)
        
        self.aug_minProgress = 0
        widgets.aug_infer_progress.setValue(self.aug_minProgress)

        for lb in self.lb_aug_after:
            lb.clear()

        for lb in self.lb_aug_pre:
            lb.clear()


    ###监控#############################################################################################################
    # 发送cpu gpu状态
    def change_monitor(self):
        lst = psutil.cpu_percent(interval=0, percpu=True)
        cpu = sum(lst)/len(lst)

        widgets.detect_lb_cpu_monitor.setText("{:.2f}".format(cpu)+"%")
        self.main2monitorpannel_signal_cpu.emit(cpu)
        self.main2monitorchart_signal_cpu.emit(lst)

        gpu_memory = pynvml.nvmlDeviceGetMemoryInfo(self.handle)# 显卡内存信息
        gpu_memory_total = gpu_memory.total
        gpu_memory_used = gpu_memory.used
        gpu = gpu_memory_used / gpu_memory_total * 100

        gpu_temp = pynvml.nvmlDeviceGetTemperature(self.handle, 0)
        widgets.detect_lb_gpu_monitor.setText("{:.2f}".format(gpu)+"%")
        self.main2monitorpannel_signal_gpu.emit(gpu)
        self.main2monitortemp_signal_gpu.emit(gpu_temp)
        self.main2monitortemp_signal_cpu.emit(int(random.random() * 5 + 70))

    
    # 按了开始后运行 ###########################################################################################
    def detect_start(self):
        # 改变控件状态
        # 按钮使能
        widgets.detect_Pause.setEnabled(True)
        widgets.detect_Close.setEnabled(True)
        widgets.detect_Start.setDisabled(True)

        widgets.btn_file.setDisabled(True)
        # 抽屉不能用
        widgets.check_save_img.setDisabled(True)
        widgets.check_save_label.setDisabled(True)
        widgets.combo_model_choose.setDisabled(True)
        widgets.btn_model_choose.setDisabled(True)

        # 多线程推理
        AppFunctions.infer_multi_thread(self) # 初始化推理器 绑定信号
        AppFunctions.init_infer_param(self)
        for thread in self.predict_threadList:
            if not thread.isRunning():
                thread.start()
        # 开始推理
        AppFunctions.start_inference(self)

        # 多线程投影页展示结果
        AppFunctions.proj_show_multi_thread(self)

    def aug_start(self):
        # 改变控件状态
        # 按钮使能
        widgets.aug_Pause.setEnabled(True)
        widgets.aug_Close.setEnabled(True)
        widgets.aug_Start.setDisabled(True)

        widgets.btn_file.setDisabled(True)

        # 多线程
        AppFunctions.aug_multi_thread(self) # 初始化增强器 绑定信号
        AppFunctions.init_aug_param(self) # 发送iou等信号
        for thread in self.aug_threadList:
            if not thread.isRunning():
                thread.start() # 进程开始
        # 开始推理
        AppFunctions.start_aug(self) # run函数开始

    ############## 按了暂停键 #############################################################################
    def detect_pause(self):
        self.detect_enable_pause = not self.detect_enable_pause
        if self.detect_enable_pause:
            for m in self.predictorList:
                m.run_pause()
        else:
            for m in self.predictorList:
                m.run_resume()

    def aug_pause(self):
        self.aug_enable_pause = not self.aug_enable_pause
        if self.aug_enable_pause:
            for m in self.augmentorList:
                m.run_pause()
        else:
            for m in self.augmentorList:
                m.run_resume()


    ############## 按了停止键 #############################################################################
    def detect_stop(self):
        AppFunctions.stop_inference(self)  # 退出进程
        # 按钮使能
        widgets.detect_Pause.setDisabled(True)
        widgets.detect_Close.setDisabled(True)
        widgets.detect_Start.setEnabled(True)
        
        widgets.btn_file.setEnabled(True)
        
        # 抽屉能用了
        widgets.check_save_img.setEnabled(True)
        widgets.check_save_label.setEnabled(True)
        widgets.combo_model_choose.setEnabled(True)
        widgets.btn_model_choose.setEnabled(True)

        self.detect_minProgress = 0
        widgets.detect_infer_progress.setValue(self.detect_minProgress)

        for lb in self.lb_infer:
            lb.clear()


    def aug_stop(self):
        AppFunctions.stop_aug(self)  
        
        # 改变控件状态
        # 按钮使能
        widgets.aug_Pause.setDisabled(True)
        widgets.aug_Close.setDisabled(True)
        widgets.aug_Start.setEnabled(True)

        widgets.btn_file.setEnabled(True)

        self.aug_minProgress = 0
        widgets.aug_infer_progress.setValue(self.aug_minProgress)

        for lb in self.lb_aug_after:
            lb.clear()

        for lb in self.lb_aug_pre:
            lb.clear()




def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/images/images/images/PyDracula.png"))
    window = MainWindow()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
    
