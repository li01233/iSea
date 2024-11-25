import sys
import math
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QTimer, Slot, Property,QRectF, QPoint, QSize
from PySide6.QtGui import QPainter, QColor, QPolygon, QFont

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QProgressBar, QHeaderView
from PySide6.QtGui import QColor
from PySide6.QtCore import QProcess, QTimer, Signal, Slot
import platform

class DevicePannel(QTableWidget):
    sdcardReceive = Signal(str)
    udiskReceive = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.bgColor = QColor(255, 255, 255)
        self.chunkColor1 = QColor(159, 174, 218)
        self.chunkColor2 = QColor(31, 84, 133)
        self.chunkColor3 = QColor(255, 107, 107)
        self.textColor1 = QColor(10, 10, 10)
        self.textColor2 = QColor(255, 255, 255)
        self.textColor3 = QColor(255, 255, 255)

        self.process = QProcess(self)
        self.process.readyRead.connect(self.readData)

        self.clear()
        self.setColumnCount(5)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 120)
        self.setColumnWidth(2, 120)
        self.setColumnWidth(3, 120)
        self.setColumnWidth(4, 120)
        self.setHorizontalHeaderLabels(["盘符", "已用空间", "可用空间", "总大小", "已用百分比"])
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionMode(QTableWidget.SingleSelection)
        self.verticalHeader().setVisible(True)
        self.horizontalHeader().setStretchLastSection(True)

        QTimer.singleShot(0, self.load)

    def getBgColor(self):
        return self.bgColor

    def getChunkColor1(self):
        return self.chunkColor1

    def getChunkColor2(self):
        return self.chunkColor2

    def getChunkColor3(self):
        return self.chunkColor3

    def getTextColor1(self):
        return self.textColor1

    def getTextColor2(self):
        return self.textColor2

    def getTextColor3(self):
        return self.textColor3

    @Slot()
    def load(self):
        self.setRowCount(0)
        if platform.system() == 'Windows':
            from win32api import GetLogicalDriveStrings
            drives = GetLogicalDriveStrings().split('\x00')[:-1]
            for drive in drives:
                import ctypes
                _, total, free = ctypes.c_ulonglong(), ctypes.c_ulonglong(), ctypes.c_ulonglong()
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(drive), ctypes.byref(_), ctypes.byref(total), ctypes.byref(free))
                used = total.value - free.value
                percent = int((used / total.value) * 100)
                self.insertSize(drive, f"{used / 2**30:.1f}G", f"{free.value / 2**30:.1f}G", f"{total.value / 2**30:.1f}G", percent)
        else:
            self.process.start("df -h")

    def setBgColor(self, color):
        if self.bgColor != color:
            self.bgColor = color
            self.load()

    def setChunkColor1(self, color):
        if self.chunkColor1 != color:
            self.chunkColor1 = color
            self.load()

    def setChunkColor2(self, color):
        if self.chunkColor2 != color:
            self.chunkColor2 = color
            self.load()

    def setChunkColor3(self, color):
        if self.chunkColor3 != color:
            self.chunkColor3 = color
            self.load()

    def setTextColor1(self, color):
        if self.textColor1 != color:
            self.textColor1 = color
            self.load()

    def setTextColor2(self, color):
        if self.textColor2 != color:
            self.textColor2 = color
            self.load()

    def setTextColor3(self, color):
        if self.textColor3 != color:
            self.textColor3 = color
            self.load()

    @Slot()
    def readData(self):
        while self.process.canReadLine():
            result = str(self.process.readLine(), 'utf-8').strip()
            if result.startswith('/dev/'):
                if '/mmcblk' in result:
                    self.checkSize(result, 'SD卡')
                elif '/sd' in result:
                    self.checkSize(result, 'U盘')

    def checkSize(self, result, name):
        parts = [part for part in result.split(' ') if part]
        if len(parts) >= 6:
            dev, size, used, avail, percent, mount = parts[:6]
            percent = int(percent.strip('%'))
            self.insertSize(dev if not name else name, used, avail, size, percent)

    def insertSize(self, name, used, free, all_size, percent):
        row = self.rowCount()
        self.insertRow(row)
        self.setItem(row, 0, QTableWidgetItem(name))
        self.setItem(row, 1, QTableWidgetItem(used))
        self.setItem(row, 2, QTableWidgetItem(free))
        self.setItem(row, 3, QTableWidgetItem(all_size))
        bar = QProgressBar()
        bar.setRange(0, 100)
        bar.setValue(percent)
        qss = f"QProgressBar{{background:{self.bgColor.name()};border-width:0px;border-radius:0px;text-align:center;}}"
        if percent < 50:
            qss += f"QProgressBar{{color:{self.textColor1.name()};}}QProgressBar::chunk{{background:{self.chunkColor1.name()};}}"
        elif percent < 90:
            qss += f"QProgressBar{{color:{self.textColor2.name()};}}QProgressBar::chunk{{background:{self.chunkColor2.name()};}}"
        else:
            qss += f"QProgressBar{{color:{self.textColor3.name()};}}QProgressBar::chunk{{background:{self.chunkColor3.name()};}}"
        bar.setStyleSheet(qss)
        self.setCellWidget(row, 4, bar)

    def sizeHint(self):
        return QSize(1000, 400)

    def minimumSizeHint(self):
        return QSize(1000, 400)

