import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QRectF, QTimer, Property, QEasingCurve, QRect
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QPointF, QPoint
from PySide6.QtCore import QPropertyAnimation

class ThermometreDlg(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.m_width = 20
        self.maxValue = 100
        self.minValue = 0
        self.m_radius = 1.05
        self.m_value = 2
        self.curValue = self.m_value
        self.m_rect = QRectF()
        self.m_valueAnimation = QPropertyAnimation(self, b"m_value")
        self.m_valueAnimation.setDuration(1000)
        self.m_valueAnimation.setEasingCurve(QEasingCurve.OutCubic)
        self.m_valueAnimation.setLoopCount(1)

        at = QTimer(self)
        at.timeout.connect(self.startAnimation)
        at.start(100)

    def updateRect(self):
        self.m_rect.setX(0)
        self.m_rect.setY(25 - (self.height()-20) / 2)
        self.m_rect.setWidth(self.m_width)
        self.m_rect.setHeight((self.height()-20) - 40 - self.m_width * self.m_radius)

    def setValue(self, value):
        self.m_value = value
        self.update()

    def changeValue(self, value):
        if value > self.maxValue:
            value = self.maxValue
        if value < self.minValue:
            value = self.minValue
        self.curValue = value

    def getValue(self):
        return self.m_value

    def paintEvent(self, event):
        self.updateRect()
        painter = QPainter(self)
        painter.translate(self.width() / 2, (self.height()-20) / 2)
        painter.setRenderHints(QPainter.TextAntialiasing | QPainter.Antialiasing)
        painter.fillRect(self.m_rect, QColor(31, 84, 133))
        
        tmpRect = QRectF(self.m_rect.bottomLeft(), QPointF(self.m_width, (self.height()-20) / 2 - self.m_width * self.m_radius))
        # painter.fillRect(tmpRect, QColor(255, 0, 0))
        
        painter.setPen(QPen(Qt.white,5))
        painter.drawRect(QRect(QPoint(self.m_rect.topLeft().x(),self.m_rect.topLeft().y()),
                               QPoint(self.m_rect.bottomRight().x(),self.m_rect.bottomRight().y())))
        painter.drawRect(QRect(QPoint(tmpRect.topLeft().x(),tmpRect.topLeft().y()),
                               QPoint(tmpRect.bottomRight().x(),tmpRect.bottomRight().y())))

        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 0, 0))
        painter.drawEllipse(tmpRect.bottomLeft() + QPointF(tmpRect.width() / 2, 0), self.m_width * self.m_radius, self.m_width * self.m_radius)
        painter.setPen(QPen(Qt.white,5))
        painter.drawEllipse(tmpRect.bottomLeft() + QPointF(tmpRect.width() / 2, 0), self.m_width * self.m_radius, self.m_width * self.m_radius)
        painter.setPen(QColor(Qt.white))
        painter.drawText(tmpRect.bottomLeft() + QPointF(tmpRect.width() / 2 - 11.5, 4.5), str(self.m_value))

        nYCount = (self.maxValue - self.minValue) // 10 + 1
        perHeight = self.m_rect.height() / nYCount
        for i in range(nYCount):
            basePoint = self.m_rect.bottomLeft() - QPointF(0, perHeight / 2) - QPointF(0, perHeight * i)
            painter.drawLine(basePoint+ QPointF(0, 0), basePoint + QPointF(-15, 0))
            for j in range(1, 10):
                if i == nYCount - 1:
                    continue
                painter.drawLine(basePoint - QPointF(5, perHeight / 10 * j), basePoint - QPointF(10, perHeight / 10 * j))
            painter.drawText(basePoint + QPointF(-40, 4), str(self.minValue + i * 10))

        h = (self.m_value - self.minValue) / (self.maxValue - self.minValue) * (self.m_rect.height() - perHeight)
        h = max(0, min(h, self.m_rect.height()))

        tmpRect = self.m_rect.adjusted(2, self.m_rect.height() - h - perHeight / 2 - 1, -2, 0)
        painter.fillRect(tmpRect, QColor(255, 0, 0))


    def startAnimation(self):
        startValue = self.getValue()
        self.m_valueAnimation.setKeyValueAt(0, startValue - 1)
        self.m_valueAnimation.setKeyValueAt(0.5, self.curValue + 1)
        self.m_valueAnimation.setKeyValueAt(1, self.curValue)
        self.m_valueAnimation.setStartValue(startValue - 2)
        self.m_valueAnimation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ThermometreDlg()
    widget.show()
    sys.exit(app.exec())
