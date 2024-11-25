from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen, QPolygon, QLinearGradient, QConicalGradient, QAction
from PySide6.QtCore import QTimer, Qt, QSize, Signal, QTime, QPoint
import math

class Clock(QWidget):
    class SecondStyle:
        Normal = 0
        Spring = 1
        Continue = 2
        Hide = 3

    def __init__(self, parent=None):
        super().__init__(parent)

        self.crownColorStart = QColor(31, 84, 133)
        self.crownColorEnd = QColor(255, 255, 255)
        self.foreground = QColor(255, 255, 255)
        self.background = QColor(31, 84, 133)
        self.pointerHourColor = QColor(255, 255, 255)
        self.pointerMinColor = QColor(255, 255, 255)
        self.pointerSecColor = QColor(255, 255, 255)
        self.secondStyle = Clock.SecondStyle.Normal

        self.hour = 0
        self.min = 0
        self.sec = 0
        self.msec = 0

        self.action_secondstyle = QAction(self)
        self.action_secondstyle.triggered.connect(self.doAction)

        self.timer = QTimer(self, interval=100)  # 设置定时器更新间隔为500毫秒
        self.timer.timeout.connect(self.updateTime)  # 定时器超时触发update_cpu_usage函数
        self.timer.start()  # 启动定时器

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        side = min(width, height)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        painter.translate(width / 2, height / 2)
        painter.scale(side / 200.0, side / 200.0)

        self.drawCrown(painter)
        self.drawBg(painter)
        self.drawScale(painter)
        self.drawScaleNum(painter)
        self.drawHour(painter)
        self.drawMin(painter)
        self.drawSec(painter)
        self.drawDot(painter)

    def drawCrown(self, painter):
        radius = 99
        painter.save()
        painter.setPen(Qt.NoPen)
        crownGradient = QLinearGradient(0, -radius, 0, radius)
        crownGradient.setColorAt(0, self.crownColorStart)
        crownGradient.setColorAt(1, self.crownColorEnd)
        painter.setBrush(Qt.white)
        painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.restore()

    def drawBg(self, painter):
        radius = 92
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.background)
        painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.restore()

    def drawScale(self, painter):
        radius = 90
        painter.save()
        pen = QPen()
        pen.setColor(self.foreground)
        pen.setCapStyle(Qt.RoundCap)

        for i in range(61):
            if i % 5 == 0:
                pen.setWidthF(1.5)
                painter.setPen(pen)
                painter.drawLine(0, radius - 10, 0, radius)
            else:
                pen.setWidthF(0.5)
                painter.setPen(pen)
                painter.drawLine(0, radius - 5, 0, radius)
            painter.rotate(6)

        painter.restore()

    def drawScaleNum(self, painter):
        radius = 70
        painter.save()
        painter.setPen(self.foreground)

        startRad = 60 * (math.pi / 180)
        deltaRad = 30 * (math.pi / 180)

        for i in range(12):
            sina = math.sin(startRad - i * deltaRad)
            cosa = math.cos(startRad - i * deltaRad)
            strValue = str(i + 1)

            textWidth = 20
            textHeight = 20
            x = radius * cosa - textWidth / 2
            y = -radius * sina + textHeight / 4
            painter.drawText(x, y, strValue)

        painter.restore()

    def drawHour(self, painter):
        painter.save()
        pen = QPen()
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(self.pointerHourColor)
        painter.setBrush(self.pointerHourColor)

        pts = QPolygon()
        pts.append(QPoint(-3, 8))
        pts.append(QPoint(3, 8))
        pts.append(QPoint(2, -40))
        pts.append(QPoint(-2, -40))

        # pts.setPoints([-3, 8, 3, 8, 2, -40, -2, -40])

        painter.rotate(30.0 * (self.hour + self.min / 60.0))
        painter.drawConvexPolygon(pts)
        painter.restore()

    def drawMin(self, painter):
        painter.save()
        pen = QPen()
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(self.pointerMinColor)
        painter.setBrush(self.pointerMinColor)

        pts = QPolygon()
        pts.append(QPoint(-2, 8))
        pts.append(QPoint(2, 8))
        pts.append(QPoint(1, -60))
        pts.append(QPoint(-1, -60))
        # pts.setPoints([-2, 8, 2, 8, 1, -60, -1, -60])

        painter.rotate(6.0 * (self.min + self.sec / 60.0))
        painter.drawConvexPolygon(pts)
        painter.restore()

    def drawSec(self, painter):
        if self.secondStyle == Clock.SecondStyle.Hide:
            return

        painter.save()
        pen = QPen()
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(self.pointerSecColor)
        painter.setBrush(self.pointerSecColor)

        pts = QPolygon()
        pts.append(QPoint(-1, 0))
        pts.append(QPoint(1, 0))
        pts.append(QPoint(0, 70))

        # pts.setPoints([-1, 10, 1, 10, 0, -70])

        painter.rotate(self.angleSpring if self.secondStyle == Clock.SecondStyle.Spring else 6.0 * self.sec)
        painter.drawConvexPolygon(pts)
        painter.restore()

    def drawDot(self, painter):
        painter.save()
        coneGradient = QConicalGradient(0, 0, -90.0)
        coneGradient.setColorAt(0.0, self.background)
        coneGradient.setColorAt(0.5, self.foreground)
        coneGradient.setColorAt(1.0, self.background)
        painter.setOpacity(0.9)
        painter.setPen(Qt.NoPen)
        painter.setBrush(coneGradient)
        painter.drawEllipse(-5, -5, 10, 10)
        painter.restore()

    def doAction(self):
        action = self.sender()
        if action:
            text = action.text()
            if text == "弹簧效果":
                action.setText("连续效果")
                self.setSecondStyle(Clock.SecondStyle.Spring)
            elif text == "连续效果":
                action.setText("隐藏效果")
                self.setSecondStyle(Clock.SecondStyle.Continue)
            elif text == "隐藏效果":
                action.setText("普通效果")
                self.setSecondStyle(Clock.SecondStyle.Hide)
            elif text == "普通效果":
                action.setText("弹簧效果")
                self.setSecondStyle(Clock.SecondStyle.Normal)

    def updateTime(self):
        current_time = QTime.currentTime()
        self.hour = current_time.hour()
        self.min = current_time.minute()
        self.sec = current_time.second()
        self.update()

    def updateSpring(self):
        # Implement the spring effect logic here
        self.angleSpring = (self.angleSpring + 0.1) % 360
        self.update()

    def setSecondStyle(self, secondStyle):
        self.secondStyle = secondStyle
        self.update()

    def setSystemDateTime(self, year, month, day, hour, minute, second):
        # Python does not allow setting system time without elevated permissions and platform-specific code
        # This is a placeholder method
        pass

    def setCrownColorStart(self, crownColorStart):
        self.crownColorStart = crownColorStart
        self.update()

    def setCrownColorEnd(self, crownColorEnd):
        self.crownColorEnd = crownColorEnd
        self.update()

    def setForeground(self, foreground):
        self.foreground = foreground
        self.update()

    def setBackground(self, background):
        self.background = background
        self.update()

    def setPointerHourColor(self, pointerHourColor):
        self.pointerHourColor = pointerHourColor
        self.update()

    def setPointerMinColor(self, pointerMinColor):
        self.pointerMinColor = pointerMinColor
        self.update()

    def setPointerSecColor(self, pointerSecColor):
        self.pointerSecColor = pointerSecColor
        self.update()

    def sizeHint(self):
        return QSize(200, 200)

    def minimumSizeHint(self):
        return QSize(100, 100)
