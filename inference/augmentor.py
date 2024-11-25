from PySide6.QtCore import Signal, QObject
import numpy as np
import cv2 as cv
import time
from copy import deepcopy

# 多线程的实例实现 ###########################################
class APP_aug(QObject): 
    ## 向主进程发出的信号
    aug_img = Signal(int, np.ndarray)   # 增强结果
    pre_img = Signal(int, np.ndarray)  # 原始图片
    progress = Signal(float) # 处理到了百分之多少
    end = Signal()
    
    def __init__(self, idx, file_path): 
        super(APP_aug, self).__init__() 

        self.idx = idx # 标志第几个文件
        
        # 增强部分初始化
        if idx % 4 == 0:
            self.model = Augmentor_rain()
        elif idx % 4 == 1:
            self.model = Augmentor_dusk()
        elif idx % 4 == 2:
            self.model = Augmentor_night()
        elif idx % 4 == 3:
            self.model = Augmentor_fog()
        
        # 读取图像或视频
        self.cap = cv.VideoCapture(file_path)
        self.frame_count = int(self.cap.get(cv.CAP_PROP_FRAME_COUNT))

        # 初始化
        self.dusk = self.fog = self.night = self.rain = False
        self.dusk_param = self.fog_param = self.night_param = self.rain_param = 0.0
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

            if self.idx % 4 == 0:
                aug_img = self.model.aug(frame, self.rain, self.rain_param)
            elif self.idx % 4 == 1:
                aug_img = self.model.aug(frame, self.dusk, self.dusk_param)
            elif self.idx % 4 == 2:
                aug_img = self.model.aug(frame, self.night, self.night_param)
            elif self.idx % 4 == 3:
                aug_img = self.model.aug(frame, self.fog, self.fog_param)
            
            pre_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            aug_img = cv.cvtColor(aug_img, cv.COLOR_BGR2RGB)
            self.pre_img.emit(self.idx, pre_frame) # 发射处理前图像
            self.aug_img.emit(self.idx, aug_img) # 发射处理后图像   

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
    # fog,dusk,night,rain,以及他们的参数
    def change_fog(self, fog):
        self.fog = fog

    def change_dusk(self, dusk):
        self.dusk = dusk
    
    def change_night(self, night):
        self.night = night

    def change_rain(self, rain):
        self.rain = rain
    
    def change_fog_param(self, fog_param):
        self.fog_param = fog_param

    def change_dusk_param(self, dusk_param):
        self.dusk_param = dusk_param
    
    def change_night_param(self, night_param):
        self.night_param = night_param

    def change_rain_param(self, rain_param):
        self.rain_param = rain_param

###############################################################################################################
class Augmentor_rain():
    def aug(self, image, enable = False, param = 0.0):
        if enable:
            image = self.denoise_rain(image, param)
        return image
    
    def denoise_rain(self, image, param):
        param = (1-param)*5000
        noise = self.get_noise(image,value=param)
        rain = self.rain_blur(noise,length=30,angle=-30,w=1)
        res = self.alpha_rain(rain,image,beta=0.6)
        return res
    
    def get_noise(self,img,value=5000):
        noise = np.random.uniform(0,256,img.shape[0:2])
        #控制噪声水平，取浮点数，只保留最大的一部分作为噪声
        v = value *0.01
        noise[np.where(noise<(256-v))]=0
        #噪声做初次模糊
        k = np.array([ [0, 0.1, 0],
                        [0.1,  8, 0.1],
                        [0, 0.1, 0] ])
                
        noise = cv.filter2D(noise,-1,k)
        return noise

    def rain_blur(self, noise, length=30, angle=-30,w=1):
        trans = cv.getRotationMatrix2D((length/2, length/2), angle-45, 1-length/100.0)  
        dig = np.diag(np.ones(length))   #生成对焦矩阵
        k = cv.warpAffine(dig, trans, (length, length))  #生成模糊核
        k = cv.GaussianBlur(k,(w,w),0)    #高斯模糊这个旋转后的对角核，使得雨有宽度
        #k = k / length                         #是否归一化
        blurred = cv.filter2D(noise, -1, k)    #用刚刚得到的旋转后的核，进行滤波
        #转换到0-255区间
        cv.normalize(blurred, blurred, 0, 255, cv.NORM_MINMAX)
        blurred = np.array(blurred, dtype=np.uint8)
        return blurred
    
    def alpha_rain(self, rain,img,beta = 0.8):
    
        #输入雨滴噪声和图像
        #beta = 0.8   #results weight
        #显示下雨效果
        
        #expand dimensin
        #将二维雨噪声扩张为三维单通道
        #并与图像合成在一起形成带有alpha通道的4通道图像
        rain = np.expand_dims(rain,2)
        rain_effect = np.concatenate((img,rain),axis=2)  #add alpha channel

        rain_result = img.copy()    #拷贝一个掩膜
        rain = np.array(rain,dtype=np.float32)     #数据类型变为浮点数，后面要叠加，防止数组越界要用32位
        rain_result[:,:,0]= rain_result[:,:,0] * (255-rain[:,:,0])/255.0 + beta*rain[:,:,0]
        rain_result[:,:,1] = rain_result[:,:,1] * (255-rain[:,:,0])/255 + beta*rain[:,:,0] 
        rain_result[:,:,2] = rain_result[:,:,2] * (255-rain[:,:,0])/255 + beta*rain[:,:,0]
        #对每个通道先保留雨滴噪声图对应的黑色（透明）部分，再叠加白色的雨滴噪声部分（有比例因子）
        return rain_result



#################################################################################################################
class Augmentor_fog():
    def aug(self, image, enable = False, param = 0.0):
        if enable:
            image = self.denoise_fog(image, param)
            
        return image
    
    def denoise_fog(self, image, param):
        image = image
        res = self.CreateNewImg(image, param)
        res = res.astype(np.uint8)  #python类型转换
        return res
    
    def ComputeHist(self,img):
        h,w = img.shape
        hist, bin_edge = np.histogram(img.reshape(1,w*h), bins=list(range(257)))
        return hist
    
    def ComputeMinLevel(self,hist, rate, pnum):
        sum = 0
        for i in range(256):
            sum += hist[i]
            if (sum >= (pnum * rate * 0.01)):
                return i
                
    def ComputeMaxLevel(self,hist, rate, pnum):
        sum = 0
        for i in range(256):
            sum += hist[255-i]
            if (sum >= (pnum * rate * 0.01)):
                return 255-i
                
    def LinearMap(self,minlevel, maxlevel):
        if (minlevel >= maxlevel):
            return []
        else:
            newmap = np.zeros(256)
            for i in range(256):
                if (i < minlevel):
                    newmap[i] = 0
                elif (i > maxlevel):
                    newmap[i] = 255
                else:
                    newmap[i] = (i-minlevel)/(maxlevel-minlevel) * 255
            return newmap
            
    def CreateNewImg(self,img, param):
        h,w,d = img.shape
        newimg = np.zeros([h,w,d])
        param = param * 10
        for i in range(d):
            imgmin = np.min(img[:,:,i])
            imgmax = np.max(img[:,:,i])
            imghist = self.ComputeHist(img[:,:,i])
            minlevel = self.ComputeMinLevel(imghist, param, h*w)
            maxlevel = self.ComputeMaxLevel(imghist, 2.2, h*w)
            newmap = self.LinearMap(minlevel,maxlevel)
            # print(minlevel, maxlevel)
            if (len(newmap) ==0):
                continue
            for j in range(h):
                newimg[j,:,i] = newmap[img[j,:, i]]
        return newimg


    
#################################################################################################################
class Augmentor_dusk():
    def aug(self, image, enable = False, param = 0.0):
        if enable:
            image = self.denoise_dusk(image, param)
        return image
    
    def denoise_dusk(self, image, param):
        b,g,r = cv.split(image)
        size = int(15 * (param + 0.1)) if int(5 * (param + 0.1)) % 2 ==1 else int(15 * (param + 0.1)) % 2 + 1
        clahe = cv.createCLAHE(2.0,(size, size))
        b = clahe.apply(b)
        g = clahe.apply(g)
        r = clahe.apply(r)
        res = cv.merge([b,g,r])
        return res

#################################################################################################################
class Augmentor_night():
    def aug(self, image, enable = False, param = 0.0):
        if enable:
            image = self.denoise_night(image, param)
        return image
    
    def denoise_night(self, image, param):
        yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
        lim = param * 4
        clahe = cv.createCLAHE(clipLimit=lim, tileGridSize=(8, 8))
        yuv[:, :, 0] = clahe.apply(yuv[:, :, 0])
        result = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
        return result

    
    
   