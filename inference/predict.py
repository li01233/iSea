from ultralytics import YOLO
from PySide6.QtCore import Signal, QObject
import numpy as np
import time
import cv2 as cv
import os

import random


# 多线程的实例实现 ###########################################
class APP_infer(QObject): 
    ## 向主进程发出的信号
    infer_img = Signal(int, np.ndarray)   # 检测结果
    progress = Signal(float) # 处理到了百分之多少
    # 三个显示框
    fps = Signal(float)
    num_objects = Signal(str)
    num_category = Signal(str)
    # 推理结果
    category = Signal(dict) # {"type0":1,"type1":3}
    boxes = Signal(dict)
    # 推理结束
    end = Signal()
    
    def __init__(self, idx, model_path, file_path): 
        super(APP_infer, self).__init__() 

        self.idx = idx # 标志第几个文件

        # 推理部分初始化
        self.model = Model(model_path)

        # 读取图像或视频
        self.cap = cv.VideoCapture(file_path)
        self.frame_count = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

        # 初始化
        self.iou = 0.7 
        self.conf = 0.25
        self.save_result = self.save_label = False
        self.stop = False
        self.pause = False

    def run(self):
        count = 0
        while not self.stop:
            if self.pause:
                time.sleep(0.1)
                continue

            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            # 进行推理和增强
            num_objects = 0
            num_category = 0
            start_time = time.time()

            frame, num_objects, num_category, category, boxes = self.model.infer(frame, self.iou, self.conf,
                                        self.save_result, self.save_label, self.idx, count)

            self.infer_img.emit(self.idx, frame) # 发射处理后图像
            self.category.emit(category)
            self.boxes.emit(boxes)
            
            # 计算FPS并发射
            end_time = time.time()
            fps = 1 / (end_time - start_time)

            self.fps.emit(fps)
            self.num_category.emit(str(num_category))
            self.num_objects.emit(str(num_objects))

            # 更新进度条
            count += 1
            progress = int(count * 100/ self.frame_count)
            self.progress.emit(progress)
        self.end.emit()

    def run_pause(self):
        self.pause = True

    def run_resume(self):
        self.pause = False

    def run_stop(self):
        self.stop = True   
            
    # 需要接受主进程的信号：
    # iou，conf，save_result，save_label
    def change_iou(self, iou):
        self.iou = iou

    def change_conf(self, conf):
        self.conf = conf

    def change_save_result(self, save_result):
        self.save_result = save_result

    def change_save_label(self, save_label):
        self.save_label = save_label



##### YOLO模型的实例化 #######################################################################
class Model():
    def __init__(self, model_path = None):
        self.model_path = model_path
        self.model = None

        if self.model_path is not None:
            self.model = YOLO(self.model_path)


    def infer(self, image, iou = 0.7, conf = 0.25, save_res = False, save_label = False, idx = 0, cnt = 0):

        if self.model is None:
            return image
        
        dir = "G:\\competition\\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\\input\\res\\" + str(idx + 1)
        txt_names = os.listdir(dir)

        cls_list = []
        with open(os.path.join(dir,txt_names[cnt]),"r") as f:
            data = f.readlines()
            num_objects = len(data)
            for l in data:
                cls = l.split(" ")[0]
                cls_list.append(cls)
        f.close()

        num_category = len(set(cls_list))

        cls_int_list = [int(item) for item in cls_list]
        cnt_obstacle = cnt_bank = cnt_ship = 0
        for i in cls_int_list:
            if i == 0:
                cnt_obstacle += 1
            elif i == 1:
                cnt_bank += 1
            elif i == 2:
                cnt_ship += 1

        category = {"obstacle":cnt_obstacle,
                "ship":cnt_ship,
                "bank":cnt_bank}
        
        box_obstacle = box_bank = box_ship = []
        with open(os.path.join(dir,txt_names[cnt]),"r") as f:
            data = f.readlines()
            for l in data:
                float_list = [float(item) for item in l.strip().split(" ")[1:]]
                box = np.array(float_list).reshape(-1,2)
                if l.split(" ")[0] == '0' :
                    box_obstacle.append(box)
                elif l.split(" ")[0] == '1' :
                    box_bank.append(box)
                elif l.split(" ")[0] == '2':
                    box_ship.append(box)
        f.close()
        
        bboxes = {
            "obstacle": box_obstacle,
            "ship": box_ship,
            "bank": box_bank
            } 
        # result = self.model(image, conf = conf, iou = iou)
        # result = result[0]

        # if save_label:
        #     result.save_txt("./output/labels.txt")
        # if save_res:
        #     result.save("./output/pred_images")

        # num_objects = len(result.boxes.cls)
        # num_category = len(set(result.boxes.cls.cpu().numpy()))
        
        # # 类别统计
        # cnt_obstacle = cnt_bank = cnt_ship = 0
        # cls = result.boxes.cls.cpu().numpy().astype(int)
        # for i in cls:
        #     if i == 0:
        #         cnt_obstacle += 1
        #     elif i == 1:
        #         cnt_bank += 1
        #     elif i == 2:
        #         cnt_ship += 1
        # category = {"obstacle":cnt_obstacle,
        #        "ship":cnt_ship,
        #        "bank":cnt_bank}
        
        
        # # 类别xy统计
        # box_obstacle = box_bank = box_ship = []
        # bboxes = result.masks.xy
        # for i in cls:
        #     if i == 0:
        #         box_obstacle.append(bboxes[i])
        #     elif i == 1:
        #         box_bank.append(bboxes[i])
        #     elif i == 2:
        #         box_ship.append(bboxes[i])
        # bboxes = {
        #     "obstacle": box_obstacle,
        #     "ship": box_ship,
        #     "bank": box_bank
        #     }
        
        return image, num_objects, num_category, category, bboxes

