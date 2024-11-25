from PySide6.QtCore import Qt, QTimer, Slot, Property, QSize, QRectF
from PySide6.QtGui import QColor, QPainter, QFont
from PySide6.QtWidgets import QWidget

class ProgressRing(QWidget):
    def __init__(self, parent=None, device = "CPU"):
        super().__init__(parent)
        self.device = device
        self._minValue = 0.0
        self._maxValue = 100.0
        self._value = 0.0
        self._precision = 0
        self._clockWise = True
        self._showPercent = True
        self._alarmMode = 0
        self._startAngle = 90
        self._ringPadding = 10
        self._ringWidth = 20
        self._animation = False
        self._animationStep = 1.0
        self._bgColor = QColor(31, 84, 133)
        self._textColor = QColor(50, 50, 50)
        self._ringColor = QColor(255, 255, 255)
        self._ringBgColor = QColor(31, 84, 133)
        self._circleColor = QColor(31, 84, 133)
        self._ringValue1 = 30
        self._ringValue2 = 70
        self._ringValue3 = 100
        self._ringColor1 = QColor(255, 107, 107)
        self._ringColor2 = QColor(255, 255, 0)
        self._ringColor3 = QColor(0, 255, 0)
        self._reverse = False
        self._currentValue = 0.0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.updateValue)
        self._timer.start(100)
    
    def setDevice(self, device):
        self.device = device

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        side = min(width, height)

        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        painter.translate(width / 2, height / 2)
        painter.scale(side / 200.0, side / 200.0)

        # self.drawBg(painter)
        self.drawRing(painter)
        if self._ringPadding > 0:
            self.drawPadding(painter)
        # self.drawCircle(painter)
        self.drawValue(painter)

    def drawBg(self, painter):
        radius = 99
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._ringPadding == 0 and self._ringBgColor or self._bgColor)
        painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.restore()

    def drawRing(self, painter):
        radius = 99 - self._ringPadding
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._ringColor)

        rect = QRectF(-radius, -radius, radius * 2, radius * 2)
        angleAll = 360.0
        angleCurrent = angleAll * ((self._currentValue - self._minValue) / (self._maxValue - self._minValue))
        angleOther = angleAll - angleCurrent

        if not self._clockWise:
            angleCurrent = -angleCurrent
            angleOther = -angleOther

        color = self._ringColor
        if self._alarmMode == 1:
            if self._currentValue >= self._ringValue3:
                color = self._ringColor3
            elif self._currentValue >= self._ringValue2:
                color = self._ringColor2
            else:
                color = self._ringColor1
        elif self._alarmMode == 2:
            if self._currentValue <= self._ringValue1:
                color = self._ringColor1
            elif self._currentValue <= self._ringValue2:
                color = self._ringColor2
            else:
                color = self._ringColor3

        painter.setBrush(color)
        painter.drawPie(rect, (self._startAngle - angleCurrent) * 16, angleCurrent * 16)
        painter.setBrush(self._ringBgColor)
        painter.drawPie(rect, (self._startAngle - angleCurrent - angleOther) * 16, angleOther * 16)
        painter.restore()

    def drawPadding(self, painter):
        radius = 99 - self._ringWidth - self._ringPadding
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._bgColor)
        painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.restore()

    def drawCircle(self, painter):
        radius = 99 - self._ringWidth - (self._ringPadding * 2)
        painter.save()
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._circleColor)
        painter.drawEllipse(-radius, -radius, radius * 2, radius * 2)
        painter.restore()

    def drawValue(self, painter):
        radius = 99 - self._ringWidth - (self._ringPadding * 2)
        painter.save()
        painter.setPen(self._textColor)

        font = QFont()
        fontSize = radius - (self._showPercent and 25 or 6)
        font.setPixelSize(fontSize)
        painter.setFont(font)

        if self.device == "CPU":
            strValue = "CPU \n"
        elif self.device == "GPU":
            strValue = "GPU \n"

        textRect = QRectF(-radius, -radius, radius * 2, radius * 2)
        if self._showPercent:
            percent = (self._currentValue * 100) / (self._maxValue - self._minValue)
            strValue += f"{percent:.{self._precision}f}%"
        else:
            strValue += f"{self._currentValue:.{self._precision}f}"
        
        painter.setPen(QColor(255, 255, 255))
        painter.drawText(textRect, Qt.AlignCenter, strValue)
        painter.restore()

    @Slot()
    def updateValue(self):
        if self._animation:
            if self._reverse:
                self._currentValue -= self._animationStep
                if self._currentValue <= self._minValue:
                    self._currentValue = self._minValue
                    self._reverse = False
            else:
                self._currentValue += self._animationStep
                if self._currentValue >= self._maxValue:
                    self._currentValue = self._maxValue
                    self._reverse = True
            self.update()

    # Define getters and setters for properties
    # minValue
    def getMinValue(self):
        return self._minValue

    def setMinValue(self, value):
        self._minValue = value
        self.update()

    minValue = Property(float, getMinValue, setMinValue)

    # maxValue
    def getMaxValue(self):
        return self._maxValue

    def setMaxValue(self, value):
        self._maxValue = value
        self.update()

    maxValue = Property(float, getMaxValue, setMaxValue)

    # value
    def getValue(self):
        return self._value

    def setValue(self, value):
        self._currentValue = value
        self.update()

    value = Property(float, getValue, setValue)

    # precision
    def getPrecision(self):
        return self._precision

    def setPrecision(self, value):
        self._precision = value
        self.update()

    precision = Property(int, getPrecision, setPrecision)

    # Other properties follow the same pattern...

    # Property definitions for colors and other attributes are omitted for brevity

    # sizeHint and minimumSizeHint
    def sizeHint(self):
        return QSize(200, 200)

    def minimumSizeHint(self):
        return QSize(100, 100)
    
