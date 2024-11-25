from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QImage, QPixmap

class InferRessult(QWidget):
    def __init__(self):
        super().__init__()

        self.lb = QLabel()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.lb)
        
        self.setLayout(self.mainLayout)
        self.resize(1000,1000)

    def update_img(self, img):
        img = QImage(img.data, img.shape[1], img.shape[0], img.shape[2] * img.shape[1],
                         QImage.Format_RGB888)
        img = img.scaled(self.lb.size(),Qt.KeepAspectRatio)
        self.lb.setPixmap(QPixmap.fromImage(img))