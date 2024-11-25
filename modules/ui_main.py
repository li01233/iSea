# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QScrollBar,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

from components.clock import Clock
from components.device_pannel import DevicePannel
from components.gauge_pannel import GaugePanel
from components.process_ring import ProgressRing
from components.temperature import ThermometreDlg
import modules.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"#leftBox .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#leftBox .QPushButton:hover { background-color: #7266A7; border-style: solid; border-radius: 4px; }\n"
"#leftBox .QPushButton:pressed { background-color: #996EB1; border-style: solid; border-radius: 4px; }\n"
"\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.styleSheet)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet(u"")
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setTextFormat(Qt.TextFormat.AutoText)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMinimumSize(QSize(0, 0))
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_detect_page = QPushButton(self.topMenu)
        self.btn_detect_page.setObjectName(u"btn_detect_page")
        sizePolicy.setHeightForWidth(self.btn_detect_page.sizePolicy().hasHeightForWidth())
        self.btn_detect_page.setSizePolicy(sizePolicy)
        self.btn_detect_page.setMinimumSize(QSize(0, 45))
        self.btn_detect_page.setFont(font)
        self.btn_detect_page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_detect_page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_detect_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-credit-card.png);")

        self.verticalLayout_8.addWidget(self.btn_detect_page)

        self.btn_aug_page = QPushButton(self.topMenu)
        self.btn_aug_page.setObjectName(u"btn_aug_page")
        sizePolicy.setHeightForWidth(self.btn_aug_page.sizePolicy().hasHeightForWidth())
        self.btn_aug_page.setSizePolicy(sizePolicy)
        self.btn_aug_page.setMinimumSize(QSize(0, 45))
        self.btn_aug_page.setFont(font)
        self.btn_aug_page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_aug_page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_aug_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-image-plus.png);")

        self.verticalLayout_8.addWidget(self.btn_aug_page)

        self.btn_bev_page = QPushButton(self.topMenu)
        self.btn_bev_page.setObjectName(u"btn_bev_page")
        sizePolicy.setHeightForWidth(self.btn_bev_page.sizePolicy().hasHeightForWidth())
        self.btn_bev_page.setSizePolicy(sizePolicy)
        self.btn_bev_page.setMinimumSize(QSize(0, 45))
        self.btn_bev_page.setFont(font)
        self.btn_bev_page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_bev_page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_bev_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-pin.png);")

        self.verticalLayout_8.addWidget(self.btn_bev_page)

        self.btn_monitor_page = QPushButton(self.topMenu)
        self.btn_monitor_page.setObjectName(u"btn_monitor_page")
        sizePolicy.setHeightForWidth(self.btn_monitor_page.sizePolicy().hasHeightForWidth())
        self.btn_monitor_page.setSizePolicy(sizePolicy)
        self.btn_monitor_page.setMinimumSize(QSize(0, 45))
        self.btn_monitor_page.setFont(font)
        self.btn_monitor_page.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_monitor_page.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_monitor_page.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speedometer.png);")

        self.verticalLayout_8.addWidget(self.btn_monitor_page)

        self.verticalSpacer_2 = QSpacerItem(0, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMinimumSize(QSize(0, 150))
        self.bottomMenu.setMaximumSize(QSize(16777215, 150))
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_detect = QPushButton(self.bottomMenu)
        self.btn_detect.setObjectName(u"btn_detect")
        sizePolicy.setHeightForWidth(self.btn_detect.sizePolicy().hasHeightForWidth())
        self.btn_detect.setSizePolicy(sizePolicy)
        self.btn_detect.setMinimumSize(QSize(0, 45))
        self.btn_detect.setFont(font)
        self.btn_detect.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_detect.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_detect.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-credit-card.png);")

        self.verticalLayout_9.addWidget(self.btn_detect)

        self.btn_aug = QPushButton(self.bottomMenu)
        self.btn_aug.setObjectName(u"btn_aug")
        self.btn_aug.setMinimumSize(QSize(0, 45))
        self.btn_aug.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_aug.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-image-plus.png);\n"
"")

        self.verticalLayout_9.addWidget(self.btn_aug)


        self.verticalMenuLayout.addWidget(self.bottomMenu)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox_aug = QFrame(self.bgApp)
        self.extraLeftBox_aug.setObjectName(u"extraLeftBox_aug")
        self.extraLeftBox_aug.setMinimumSize(QSize(0, 0))
        self.extraLeftBox_aug.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox_aug.setFrameShape(QFrame.Shape.NoFrame)
        self.extraColumLayout_2 = QVBoxLayout(self.extraLeftBox_aug)
        self.extraColumLayout_2.setSpacing(0)
        self.extraColumLayout_2.setObjectName(u"extraColumLayout_2")
        self.extraColumLayout_2.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg_2 = QFrame(self.extraLeftBox_aug)
        self.extraTopBg_2.setObjectName(u"extraTopBg_2")
        self.extraTopBg_2.setMinimumSize(QSize(0, 50))
        self.extraTopBg_2.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg_2.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_21 = QVBoxLayout(self.extraTopBg_2)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout_2 = QGridLayout()
        self.extraTopLayout_2.setObjectName(u"extraTopLayout_2")
        self.extraTopLayout_2.setHorizontalSpacing(10)
        self.extraTopLayout_2.setVerticalSpacing(0)
        self.extraTopLayout_2.setContentsMargins(10, -1, 10, -1)
        self.extraIcon_2 = QFrame(self.extraTopBg_2)
        self.extraIcon_2.setObjectName(u"extraIcon_2")
        self.extraIcon_2.setMinimumSize(QSize(20, 0))
        self.extraIcon_2.setMaximumSize(QSize(20, 20))
        self.extraIcon_2.setFrameShape(QFrame.Shape.NoFrame)

        self.extraTopLayout_2.addWidget(self.extraIcon_2, 0, 0, 1, 1)

        self.extraLabel_2 = QLabel(self.extraTopBg_2)
        self.extraLabel_2.setObjectName(u"extraLabel_2")
        self.extraLabel_2.setMinimumSize(QSize(150, 0))
        self.extraLabel_2.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")

        self.extraTopLayout_2.addWidget(self.extraLabel_2, 0, 1, 1, 1)

        self.extraCloseColumnBtn_2 = QPushButton(self.extraTopBg_2)
        self.extraCloseColumnBtn_2.setObjectName(u"extraCloseColumnBtn_2")
        self.extraCloseColumnBtn_2.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn_2.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.extraCloseColumnBtn_2.setStyleSheet(u"background: transparent;")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn_2.setIcon(icon)
        self.extraCloseColumnBtn_2.setIconSize(QSize(20, 20))

        self.extraTopLayout_2.addWidget(self.extraCloseColumnBtn_2, 0, 2, 1, 1)


        self.verticalLayout_21.addLayout(self.extraTopLayout_2)


        self.extraColumLayout_2.addWidget(self.extraTopBg_2)

        self.extraContent_2 = QFrame(self.extraLeftBox_aug)
        self.extraContent_2.setObjectName(u"extraContent_2")
        self.extraContent_2.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_22 = QVBoxLayout(self.extraContent_2)
        self.verticalLayout_22.setSpacing(15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(25, 20, 0, 20)
        self.RAIN = QFrame(self.extraContent_2)
        self.RAIN.setObjectName(u"RAIN")
        self.RAIN.setMinimumSize(QSize(190, 90))
        self.RAIN.setMaximumSize(QSize(190, 16777215))
        self.RAIN.setStyleSheet(u"QFrame#RAIN{\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.RAIN.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_37 = QVBoxLayout(self.RAIN)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 3, -1, 3)
        self.check_rain = QCheckBox(self.RAIN)
        self.check_rain.setObjectName(u"check_rain")
        self.check_rain.setMinimumSize(QSize(0, 30))
        self.check_rain.setMaximumSize(QSize(16777215, 30))
        self.check_rain.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_rain.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.check_rain.setAutoFillBackground(False)
        self.check_rain.setStyleSheet(u"color: rgb(255,255,255);\n"
"font: 700 13pt \"Nirmala UI\";")

        self.verticalLayout_37.addWidget(self.check_rain)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.spin_rain = QDoubleSpinBox(self.RAIN)
        self.spin_rain.setObjectName(u"spin_rain")
        self.spin_rain.setMinimumSize(QSize(0, 20))
        self.spin_rain.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color:rgba(114, 102, 167,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255)\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.spin_rain.setMaximum(1.000000000000000)
        self.spin_rain.setSingleStep(0.010000000000000)
        self.spin_rain.setValue(0.700000000000000)

        self.horizontalLayout_30.addWidget(self.spin_rain)

        self.slider_rain = QSlider(self.RAIN)
        self.slider_rain.setObjectName(u"slider_rain")
        self.slider_rain.setMaximum(100)
        self.slider_rain.setOrientation(Qt.Orientation.Horizontal)
        self.slider_rain.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.horizontalLayout_30.addWidget(self.slider_rain)


        self.verticalLayout_37.addLayout(self.horizontalLayout_30)


        self.verticalLayout_22.addWidget(self.RAIN)

        self.FOG = QFrame(self.extraContent_2)
        self.FOG.setObjectName(u"FOG")
        self.FOG.setMinimumSize(QSize(190, 90))
        self.FOG.setMaximumSize(QSize(190, 16777215))
        self.FOG.setStyleSheet(u"QFrame#FOG{\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.FOG.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_36 = QVBoxLayout(self.FOG)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, 3, -1, 3)
        self.check_fog = QCheckBox(self.FOG)
        self.check_fog.setObjectName(u"check_fog")
        self.check_fog.setMinimumSize(QSize(0, 30))
        self.check_fog.setMaximumSize(QSize(16777215, 30))
        self.check_fog.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_fog.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.check_fog.setAutoFillBackground(False)
        self.check_fog.setStyleSheet(u"color: rgb(255,255,255);\n"
"font: 700 13pt \"Nirmala UI\";")

        self.verticalLayout_36.addWidget(self.check_fog)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.spin_fog = QDoubleSpinBox(self.FOG)
        self.spin_fog.setObjectName(u"spin_fog")
        self.spin_fog.setMinimumSize(QSize(0, 20))
        self.spin_fog.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color:rgba(114, 102, 167,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255)\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.spin_fog.setMaximum(1.000000000000000)
        self.spin_fog.setSingleStep(0.010000000000000)
        self.spin_fog.setValue(0.700000000000000)

        self.horizontalLayout_29.addWidget(self.spin_fog)

        self.slider_fog = QSlider(self.FOG)
        self.slider_fog.setObjectName(u"slider_fog")
        self.slider_fog.setMaximum(100)
        self.slider_fog.setOrientation(Qt.Orientation.Horizontal)
        self.slider_fog.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.horizontalLayout_29.addWidget(self.slider_fog)


        self.verticalLayout_36.addLayout(self.horizontalLayout_29)


        self.verticalLayout_22.addWidget(self.FOG)

        self.DUSK = QFrame(self.extraContent_2)
        self.DUSK.setObjectName(u"DUSK")
        self.DUSK.setMinimumSize(QSize(190, 90))
        self.DUSK.setMaximumSize(QSize(190, 16777215))
        self.DUSK.setStyleSheet(u"QFrame#DUSK{\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.DUSK.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_33 = QVBoxLayout(self.DUSK)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(-1, 3, -1, 3)
        self.check_dusk = QCheckBox(self.DUSK)
        self.check_dusk.setObjectName(u"check_dusk")
        self.check_dusk.setMinimumSize(QSize(0, 30))
        self.check_dusk.setMaximumSize(QSize(16777215, 30))
        self.check_dusk.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_dusk.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.check_dusk.setAutoFillBackground(False)
        self.check_dusk.setStyleSheet(u"color: rgb(255,255,255);\n"
"font: 700 13pt \"Nirmala UI\";")

        self.verticalLayout_33.addWidget(self.check_dusk)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.spin_dusk = QDoubleSpinBox(self.DUSK)
        self.spin_dusk.setObjectName(u"spin_dusk")
        self.spin_dusk.setMinimumSize(QSize(0, 20))
        self.spin_dusk.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color:rgba(114, 102, 167,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255)\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.spin_dusk.setMaximum(1.000000000000000)
        self.spin_dusk.setSingleStep(0.010000000000000)
        self.spin_dusk.setValue(0.700000000000000)

        self.horizontalLayout_28.addWidget(self.spin_dusk)

        self.slider_dusk = QSlider(self.DUSK)
        self.slider_dusk.setObjectName(u"slider_dusk")
        self.slider_dusk.setMaximum(100)
        self.slider_dusk.setOrientation(Qt.Orientation.Horizontal)
        self.slider_dusk.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.horizontalLayout_28.addWidget(self.slider_dusk)


        self.verticalLayout_33.addLayout(self.horizontalLayout_28)


        self.verticalLayout_22.addWidget(self.DUSK)

        self.night = QFrame(self.extraContent_2)
        self.night.setObjectName(u"night")
        self.night.setMinimumSize(QSize(190, 90))
        self.night.setMaximumSize(QSize(190, 16777215))
        self.night.setStyleSheet(u"QFrame#night{\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.night.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_39 = QVBoxLayout(self.night)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 3, -1, 3)
        self.check_night = QCheckBox(self.night)
        self.check_night.setObjectName(u"check_night")
        self.check_night.setMinimumSize(QSize(0, 30))
        self.check_night.setMaximumSize(QSize(16777215, 30))
        self.check_night.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_night.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.check_night.setAutoFillBackground(False)
        self.check_night.setStyleSheet(u"color: rgb(255,255,255);\n"
"font: 700 13pt \"Nirmala UI\";")

        self.verticalLayout_39.addWidget(self.check_night)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.spin_night = QDoubleSpinBox(self.night)
        self.spin_night.setObjectName(u"spin_night")
        self.spin_night.setMinimumSize(QSize(0, 20))
        self.spin_night.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color:rgba(114, 102, 167,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255)\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.spin_night.setMaximum(1.000000000000000)
        self.spin_night.setSingleStep(0.010000000000000)
        self.spin_night.setValue(0.700000000000000)

        self.horizontalLayout_32.addWidget(self.spin_night)

        self.slider_night = QSlider(self.night)
        self.slider_night.setObjectName(u"slider_night")
        self.slider_night.setMaximum(100)
        self.slider_night.setOrientation(Qt.Orientation.Horizontal)
        self.slider_night.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.horizontalLayout_32.addWidget(self.slider_night)


        self.verticalLayout_39.addLayout(self.horizontalLayout_32)


        self.verticalLayout_22.addWidget(self.night)


        self.extraColumLayout_2.addWidget(self.extraContent_2)


        self.appLayout.addWidget(self.extraLeftBox_aug)

        self.extraLeftBox_detect = QFrame(self.bgApp)
        self.extraLeftBox_detect.setObjectName(u"extraLeftBox_detect")
        self.extraLeftBox_detect.setMinimumSize(QSize(0, 0))
        self.extraLeftBox_detect.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox_detect.setFrameShape(QFrame.Shape.NoFrame)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox_detect)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox_detect)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        self.extraLabel.setFont(font3)
        self.extraLabel.setStyleSheet(u"font: 700 14pt \"Segoe UI\";")

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox_detect)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(25, 20, 0, 50)
        self.Model = QFrame(self.extraContent)
        self.Model.setObjectName(u"Model")
        self.Model.setMinimumSize(QSize(190, 90))
        self.Model.setMaximumSize(QSize(190, 16777215))
        self.Model.setStyleSheet(u"QFrame#Model{\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.Model.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.Model)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_2 = QPushButton(self.Model)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setMaximumSize(QSize(16777215, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/images/icons/cil-layers.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")

        self.verticalLayout_10.addWidget(self.pushButton_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_model_choose = QPushButton(self.Model)
        self.btn_model_choose.setObjectName(u"btn_model_choose")
        self.btn_model_choose.setMinimumSize(QSize(20, 30))
        self.btn_model_choose.setMaximumSize(QSize(70, 30))
        self.btn_model_choose.setFont(font)
        self.btn_model_choose.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_model_choose.setMouseTracking(True)
        self.btn_model_choose.setStyleSheet(u"background-color: rgb(114, 102, 167);\n"
"color: rgb(255,255,255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_model_choose.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.btn_model_choose)

        self.combo_model_choose = QComboBox(self.Model)
        self.combo_model_choose.setObjectName(u"combo_model_choose")

        self.horizontalLayout_7.addWidget(self.combo_model_choose)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)


        self.verticalLayout_12.addWidget(self.Model)

        self.IoU = QFrame(self.extraContent)
        self.IoU.setObjectName(u"IoU")
        self.IoU.setMinimumSize(QSize(190, 90))
        self.IoU.setMaximumSize(QSize(190, 16777215))
        self.IoU.setStyleSheet(u"QFrame#IoU{\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.IoU.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_11 = QVBoxLayout(self.IoU)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.pushButton_3 = QPushButton(self.IoU)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setMaximumSize(QSize(16777215, 30))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/images/icons/cil-clone.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")

        self.verticalLayout_11.addWidget(self.pushButton_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.spin_iou = QDoubleSpinBox(self.IoU)
        self.spin_iou.setObjectName(u"spin_iou")
        self.spin_iou.setMinimumSize(QSize(0, 20))
        self.spin_iou.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color:rgba(114, 102, 167,90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255)\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.spin_iou.setMaximum(1.000000000000000)
        self.spin_iou.setSingleStep(0.010000000000000)
        self.spin_iou.setValue(0.700000000000000)

        self.horizontalLayout_8.addWidget(self.spin_iou)

        self.slider_iou = QSlider(self.IoU)
        self.slider_iou.setObjectName(u"slider_iou")
        self.slider_iou.setMaximum(100)
        self.slider_iou.setOrientation(Qt.Orientation.Horizontal)
        self.slider_iou.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.horizontalLayout_8.addWidget(self.slider_iou)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)


        self.verticalLayout_12.addWidget(self.IoU)

        self.Conf = QFrame(self.extraContent)
        self.Conf.setObjectName(u"Conf")
        self.Conf.setMinimumSize(QSize(190, 90))
        self.Conf.setMaximumSize(QSize(190, 16777215))
        self.Conf.setStyleSheet(u"QFrame#Conf\n"
"{\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.Conf.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_23 = QVBoxLayout(self.Conf)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_5 = QPushButton(self.Conf)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setMinimumSize(QSize(0, 30))
        self.pushButton_5.setMaximumSize(QSize(16777215, 30))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")

        self.verticalLayout_23.addWidget(self.pushButton_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.spin_conf = QDoubleSpinBox(self.Conf)
        self.spin_conf.setObjectName(u"spin_conf")
        self.spin_conf.setMinimumSize(QSize(0, 20))
        self.spin_conf.setStyleSheet(u"QDoubleSpinBox {\n"
"border: 0px solid lightgray;\n"
"border-radius: 2px;\n"
"background-color:rgba(114, 102, 167, 90);\n"
"font: 600 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255)\n"
"}\n"
"        \n"
"QDoubleSpinBox::up-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_up.png);\n"
"}\n"
"QDoubleSpinBox::up-button:pressed {\n"
"margin-top: 1px;\n"
"}\n"
"            \n"
"QDoubleSpinBox::down-button {\n"
"width: 10px;\n"
"height: 9px;\n"
"margin: 0px 3px 0px 0px;\n"
"border-image: url(:/all/img/box_down.png);\n"
"}\n"
"QDoubleSpinBox::down-button:pressed {\n"
"margin-bottom: 1px;\n"
"}")
        self.spin_conf.setMinimum(0.000000000000000)
        self.spin_conf.setMaximum(1.000000000000000)
        self.spin_conf.setSingleStep(0.010000000000000)
        self.spin_conf.setValue(0.250000000000000)

        self.horizontalLayout_13.addWidget(self.spin_conf)

        self.slider_conf = QSlider(self.Conf)
        self.slider_conf.setObjectName(u"slider_conf")
        self.slider_conf.setMaximum(100)
        self.slider_conf.setPageStep(10)
        self.slider_conf.setOrientation(Qt.Orientation.Horizontal)
        self.slider_conf.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider_conf.setTickInterval(0)

        self.horizontalLayout_13.addWidget(self.slider_conf)


        self.verticalLayout_23.addLayout(self.horizontalLayout_13)


        self.verticalLayout_12.addWidget(self.Conf)

        self.Save = QFrame(self.extraContent)
        self.Save.setObjectName(u"Save")
        self.Save.setMinimumSize(QSize(190, 130))
        self.Save.setMaximumSize(QSize(190, 16777215))
        self.Save.setStyleSheet(u"QFrame#Save{\n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}")
        self.Save.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_26 = QVBoxLayout(self.Save)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.pushButton_6 = QPushButton(self.Save)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setMaximumSize(QSize(16777215, 30))
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/images/icons/cil-save.png);\n"
"background-repeat: no-repeat;\n"
"background-position: left center;\n"
"border: none;\n"
"border-left: 20px solid transparent;\n"
"\n"
"text-align: left;\n"
"padding-left: 40px;\n"
"padding-bottom: 2px;\n"
"color: rgba(255, 255, 255, 199);\n"
"font: 700 13pt \"Nirmala UI\";\n"
"}")

        self.verticalLayout_26.addWidget(self.pushButton_6)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.check_save_img = QCheckBox(self.Save)
        self.check_save_img.setObjectName(u"check_save_img")
        self.check_save_img.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_save_img.setAutoFillBackground(False)
        self.check_save_img.setStyleSheet(u"color: rgb(255,255,255)")

        self.verticalLayout_28.addWidget(self.check_save_img)

        self.check_save_label = QCheckBox(self.Save)
        self.check_save_label.setObjectName(u"check_save_label")
        self.check_save_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.check_save_label.setAutoFillBackground(False)
        self.check_save_label.setStyleSheet(u"color: rgb(255,255,255)")

        self.verticalLayout_28.addWidget(self.check_save_label)


        self.verticalLayout_26.addLayout(self.verticalLayout_28)


        self.verticalLayout_12.addWidget(self.Save)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox_detect)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.btn_file = QPushButton(self.leftBox)
        self.btn_file.setObjectName(u"btn_file")
        self.btn_file.setMinimumSize(QSize(30, 30))
        self.btn_file.setMaximumSize(QSize(30, 30))
        self.btn_file.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_file.setIcon(icon1)
        self.btn_file.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_file)

        self.btn_help = QPushButton(self.leftBox)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(30, 30))
        self.btn_help.setMaximumSize(QSize(30, 30))
        self.btn_help.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/images/\u95ee\u53f7.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_help.setIcon(icon2)
        self.btn_help.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_help)

        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon3)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon4)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon5)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.monitor_page = QWidget()
        self.monitor_page.setObjectName(u"monitor_page")
        self.horizontalLayout_10 = QHBoxLayout(self.monitor_page)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_26 = QFrame(self.monitor_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(1300, 0))
        self.verticalLayout_30 = QVBoxLayout(self.frame_26)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_23 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_23.setSpacing(20)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(1, 1, 1, 1)
        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMaximumSize(QSize(630, 16777215))
        self.monitor_layout_cpu = QVBoxLayout(self.frame_30)
        self.monitor_layout_cpu.setObjectName(u"monitor_layout_cpu")
        self.frame_27 = QFrame(self.frame_30)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 200))
        self.frame_27.setStyleSheet(u"QFrame#frame_27{\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
" }")
        self.horizontalLayout_21 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_4 = QPushButton(self.frame_27)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u":/images/images/images/computer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon6)
        self.pushButton_4.setIconSize(QSize(100, 100))

        self.horizontalLayout_21.addWidget(self.pushButton_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_4)

        self.lb_cpu_info = QLabel(self.frame_27)
        self.lb_cpu_info.setObjectName(u"lb_cpu_info")
        self.lb_cpu_info.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.lb_cpu_info.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.lb_cpu_info)


        self.monitor_layout_cpu.addWidget(self.frame_27)

        self.frame = QFrame(self.frame_30)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.layout_cpu_monitor = QVBoxLayout(self.frame)
        self.layout_cpu_monitor.setObjectName(u"layout_cpu_monitor")

        self.monitor_layout_cpu.addWidget(self.frame)


        self.horizontalLayout_23.addWidget(self.frame_30)

        self.monitor_layout_cpu_pannel_2 = QFrame(self.frame_28)
        self.monitor_layout_cpu_pannel_2.setObjectName(u"monitor_layout_cpu_pannel_2")
        self.monitor_layout_cpu_pannel_2.setMinimumSize(QSize(0, 0))
        self.monitor_layout_cpu_pannel_2.setMaximumSize(QSize(16777215, 500))
        self.horizontalLayout_50 = QHBoxLayout(self.monitor_layout_cpu_pannel_2)
        self.horizontalLayout_50.setSpacing(30)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.monitor_layout_gpu_pannel_2 = QFrame(self.monitor_layout_cpu_pannel_2)
        self.monitor_layout_gpu_pannel_2.setObjectName(u"monitor_layout_gpu_pannel_2")
        self.monitor_layout_gpu_pannel_2.setMinimumSize(QSize(200, 200))
        self.monitor_layout_gpu_pannel = QVBoxLayout(self.monitor_layout_gpu_pannel_2)
        self.monitor_layout_gpu_pannel.setSpacing(30)
        self.monitor_layout_gpu_pannel.setObjectName(u"monitor_layout_gpu_pannel")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setSpacing(30)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.frame_34 = QFrame(self.monitor_layout_gpu_pannel_2)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"QFrame#frame_34{\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
" }")
        self.verticalLayout_32 = QVBoxLayout(self.frame_34)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.monitor_cpu_lb_2 = QFrame(self.frame_34)
        self.monitor_cpu_lb_2.setObjectName(u"monitor_cpu_lb_2")
        self.monitor_cpu_lb_2.setMaximumSize(QSize(16777215, 50))
        self.monitor_cpu_lb_2.setStyleSheet(u"")
        self.monitor_cpu_lb = QHBoxLayout(self.monitor_cpu_lb_2)
        self.monitor_cpu_lb.setObjectName(u"monitor_cpu_lb")
        self.label_14 = QLabel(self.monitor_cpu_lb_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.monitor_cpu_lb.addWidget(self.label_14)

        self.detect_lb_cpu_monitor = QLabel(self.monitor_cpu_lb_2)
        self.detect_lb_cpu_monitor.setObjectName(u"detect_lb_cpu_monitor")
        self.detect_lb_cpu_monitor.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.detect_lb_cpu_monitor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.monitor_cpu_lb.addWidget(self.detect_lb_cpu_monitor)


        self.verticalLayout_32.addWidget(self.monitor_cpu_lb_2)

        self.cpu_gauge = ProgressRing(self.frame_34)
        self.cpu_gauge.setObjectName(u"cpu_gauge")

        self.verticalLayout_32.addWidget(self.cpu_gauge)


        self.horizontalLayout_52.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.monitor_layout_gpu_pannel_2)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"QFrame#frame_35{\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
" }")
        self.verticalLayout_48 = QVBoxLayout(self.frame_35)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.monitor_gpu_lb_2 = QFrame(self.frame_35)
        self.monitor_gpu_lb_2.setObjectName(u"monitor_gpu_lb_2")
        self.monitor_gpu_lb_2.setMaximumSize(QSize(16777215, 50))
        self.monitor_gpu_lb = QHBoxLayout(self.monitor_gpu_lb_2)
        self.monitor_gpu_lb.setObjectName(u"monitor_gpu_lb")
        self.label_15 = QLabel(self.monitor_gpu_lb_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.monitor_gpu_lb.addWidget(self.label_15)

        self.detect_lb_gpu_monitor = QLabel(self.monitor_gpu_lb_2)
        self.detect_lb_gpu_monitor.setObjectName(u"detect_lb_gpu_monitor")
        self.detect_lb_gpu_monitor.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.detect_lb_gpu_monitor.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.monitor_gpu_lb.addWidget(self.detect_lb_gpu_monitor)


        self.verticalLayout_48.addWidget(self.monitor_gpu_lb_2)

        self.gpu_gauge = ProgressRing(self.frame_35)
        self.gpu_gauge.setObjectName(u"gpu_gauge")

        self.verticalLayout_48.addWidget(self.gpu_gauge)


        self.horizontalLayout_52.addWidget(self.frame_35)


        self.monitor_layout_gpu_pannel.addLayout(self.horizontalLayout_52)


        self.horizontalLayout_51.addWidget(self.monitor_layout_gpu_pannel_2)


        self.horizontalLayout_50.addLayout(self.horizontalLayout_51)

        self.frame_21 = QFrame(self.monitor_layout_cpu_pannel_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 16777215))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_21)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(500, 500))
        self.frame_24.setStyleSheet(u"QFrame#frame_24{\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
" }")
        self.verticalLayout_49 = QVBoxLayout(self.frame_24)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_23 = QFrame(self.frame_24)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(500, 100))
        self.horizontalLayout_54 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_21 = QLabel(self.frame_23)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(200, 50))
        self.label_21.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_54.addWidget(self.label_21)

        self.label_20 = QLabel(self.frame_23)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 50))
        self.label_20.setMaximumSize(QSize(200, 50))
        self.label_20.setStyleSheet(u"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_54.addWidget(self.label_20)


        self.verticalLayout_49.addWidget(self.frame_23)

        self.frame_31 = QFrame(self.frame_24)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(16777215, 400))
        self.horizontalLayout_53 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.cpu_temperature = ThermometreDlg(self.frame_31)
        self.cpu_temperature.setObjectName(u"cpu_temperature")
        self.cpu_temperature.setMinimumSize(QSize(0, 300))
        self.cpu_temperature.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_53.addWidget(self.cpu_temperature)

        self.gpu_temperature = ThermometreDlg(self.frame_31)
        self.gpu_temperature.setObjectName(u"gpu_temperature")
        self.gpu_temperature.setMinimumSize(QSize(0, 0))
        self.gpu_temperature.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_53.addWidget(self.gpu_temperature)


        self.verticalLayout_49.addWidget(self.frame_31)


        self.verticalLayout_52.addWidget(self.frame_24)


        self.horizontalLayout_50.addWidget(self.frame_21)


        self.horizontalLayout_23.addWidget(self.monitor_layout_cpu_pannel_2)


        self.verticalLayout_30.addWidget(self.frame_28)

        self.frame_25 = QFrame(self.frame_26)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(1800, 16777215))
        self.horizontalLayout_24 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, -1, -1)
        self.frame_32 = QFrame(self.frame_25)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(630, 0))
        self.frame_32.setMaximumSize(QSize(630, 16777215))
        self.monitor_layout_gpu = QVBoxLayout(self.frame_32)
        self.monitor_layout_gpu.setSpacing(6)
        self.monitor_layout_gpu.setObjectName(u"monitor_layout_gpu")
        self.monitor_layout_gpu.setContentsMargins(-1, -1, 20, -1)
        self.frame_29 = QFrame(self.frame_32)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setMaximumSize(QSize(630, 16777215))
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_29)
        self.verticalLayout_53.setSpacing(6)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_3 = QFrame(self.frame_29)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 200))
        self.frame_3.setStyleSheet(u"QFrame#frame_3{\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
" }")
        self.horizontalLayout_44 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"font: 700 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(100, 100))

        self.horizontalLayout_44.addWidget(self.pushButton_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_5)

        self.lb_gpu_info = QLabel(self.frame_3)
        self.lb_gpu_info.setObjectName(u"lb_gpu_info")
        self.lb_gpu_info.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.lb_gpu_info.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.lb_gpu_info)


        self.verticalLayout_53.addWidget(self.frame_3)


        self.monitor_layout_gpu.addWidget(self.frame_29)

        self.frame1 = QFrame(self.frame_32)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setMaximumSize(QSize(16777215, 16777215))
        self.layout_gpu_monitor = QVBoxLayout(self.frame1)
        self.layout_gpu_monitor.setObjectName(u"layout_gpu_monitor")

        self.monitor_layout_gpu.addWidget(self.frame1)


        self.horizontalLayout_24.addWidget(self.frame_32)

        self.device_memory = DevicePannel(self.frame_25)
        self.device_memory.setObjectName(u"device_memory")
        self.device_memory.setMinimumSize(QSize(0, 0))
        self.device_memory.setMaximumSize(QSize(1500, 500))

        self.horizontalLayout_24.addWidget(self.device_memory)


        self.verticalLayout_30.addWidget(self.frame_25)


        self.horizontalLayout_10.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.monitor_page)
        self.aug_page = QWidget()
        self.aug_page.setObjectName(u"aug_page")
        self.aug_page.setStyleSheet(u"")
        self.horizontalLayout_25 = QHBoxLayout(self.aug_page)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.aug_page)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_14 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.rain = QFrame(self.frame_20)
        self.rain.setObjectName(u"rain")
        self.rain.setMinimumSize(QSize(150, 50))
        self.rain.setMaximumSize(QSize(16777215, 100))
        self.rain.setAutoFillBackground(False)
        self.rain.setStyleSheet(u"QFrame#rain\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.rain.setFrameShape(QFrame.Shape.StyledPanel)
        self.rain.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.rain)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_2 = QLabel(self.rain)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)


        self.horizontalLayout_14.addWidget(self.rain)

        self.fog = QFrame(self.frame_20)
        self.fog.setObjectName(u"fog")
        self.fog.setMinimumSize(QSize(150, 50))
        self.fog.setMaximumSize(QSize(16777215, 100))
        self.fog.setAutoFillBackground(False)
        self.fog.setStyleSheet(u"QFrame#fog\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.fog.setFrameShape(QFrame.Shape.StyledPanel)
        self.fog.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.fog)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_8 = QLabel(self.fog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_49.addWidget(self.label_8)


        self.horizontalLayout_14.addWidget(self.fog)

        self.dusk = QFrame(self.frame_20)
        self.dusk.setObjectName(u"dusk")
        self.dusk.setMinimumSize(QSize(150, 50))
        self.dusk.setMaximumSize(QSize(16777215, 100))
        self.dusk.setStyleSheet(u"QFrame#dusk\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.dusk.setFrameShape(QFrame.Shape.StyledPanel)
        self.dusk.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.dusk)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_5 = QLabel(self.dusk)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_5)


        self.horizontalLayout_14.addWidget(self.dusk)

        self.night_2 = QFrame(self.frame_20)
        self.night_2.setObjectName(u"night_2")
        self.night_2.setMinimumSize(QSize(150, 50))
        self.night_2.setMaximumSize(QSize(16777215, 100))
        self.night_2.setStyleSheet(u"QFrame#night_2\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.night_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.night_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.night_2)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_6 = QLabel(self.night_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_6)


        self.horizontalLayout_14.addWidget(self.night_2)


        self.verticalLayout_24.addWidget(self.frame_20)

        self.frame2 = QFrame(self.aug_page)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setMinimumSize(QSize(0, 350))
        self.frame2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame2)
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(10)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.lb_pre_rain = QLabel(self.frame2)
        self.lb_pre_rain.setObjectName(u"lb_pre_rain")

        self.verticalLayout_40.addWidget(self.lb_pre_rain)

        self.lb_aug_rain = QLabel(self.frame2)
        self.lb_aug_rain.setObjectName(u"lb_aug_rain")

        self.verticalLayout_40.addWidget(self.lb_aug_rain)


        self.horizontalLayout_15.addLayout(self.verticalLayout_40)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.lb_pre_fog = QLabel(self.frame2)
        self.lb_pre_fog.setObjectName(u"lb_pre_fog")

        self.verticalLayout_27.addWidget(self.lb_pre_fog)

        self.lb_aug_fog = QLabel(self.frame2)
        self.lb_aug_fog.setObjectName(u"lb_aug_fog")

        self.verticalLayout_27.addWidget(self.lb_aug_fog)


        self.horizontalLayout_15.addLayout(self.verticalLayout_27)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.lb_pre_dusk = QLabel(self.frame2)
        self.lb_pre_dusk.setObjectName(u"lb_pre_dusk")

        self.verticalLayout_38.addWidget(self.lb_pre_dusk)

        self.lb_aug_dusk = QLabel(self.frame2)
        self.lb_aug_dusk.setObjectName(u"lb_aug_dusk")

        self.verticalLayout_38.addWidget(self.lb_aug_dusk)


        self.horizontalLayout_15.addLayout(self.verticalLayout_38)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.lb_pre_night = QLabel(self.frame2)
        self.lb_pre_night.setObjectName(u"lb_pre_night")

        self.verticalLayout_41.addWidget(self.lb_pre_night)

        self.lb_aug_night = QLabel(self.frame2)
        self.lb_aug_night.setObjectName(u"lb_aug_night")

        self.verticalLayout_41.addWidget(self.lb_aug_night)


        self.horizontalLayout_15.addLayout(self.verticalLayout_41)


        self.verticalLayout_25.addLayout(self.horizontalLayout_15)

        self.horizontalFrame = QFrame(self.frame2)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 50))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 150))
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.aug_Start = QPushButton(self.horizontalFrame)
        self.aug_Start.setObjectName(u"aug_Start")
        self.aug_Start.setMinimumSize(QSize(30, 30))
        self.aug_Start.setMaximumSize(QSize(30, 30))
        self.aug_Start.setStyleSheet(u"QPushButton {\n"
"	background-color: #586796;\n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #996EB1;\n"
"	border: 2px solid #996EB1;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aug_Start.setIcon(icon7)

        self.horizontalLayout_27.addWidget(self.aug_Start)

        self.aug_Pause = QPushButton(self.horizontalFrame)
        self.aug_Pause.setObjectName(u"aug_Pause")
        self.aug_Pause.setMinimumSize(QSize(30, 30))
        self.aug_Pause.setMaximumSize(QSize(30, 30))
        self.aug_Pause.setStyleSheet(u"QPushButton {\n"
"	background-color: #586796;\n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #996EB1;\n"
"	border: 2px solid #996EB1;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-media-pause.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aug_Pause.setIcon(icon8)

        self.horizontalLayout_27.addWidget(self.aug_Pause)

        self.aug_infer_progress = QProgressBar(self.horizontalFrame)
        self.aug_infer_progress.setObjectName(u"aug_infer_progress")
        self.aug_infer_progress.setMinimumSize(QSize(0, 30))
        self.aug_infer_progress.setMaximumSize(QSize(16777215, 30))
        self.aug_infer_progress.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(153, 110, 177);\n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(31, 84, 133, 200);\n"
"border-radius: 7px;\n"
"}")
        self.aug_infer_progress.setValue(0)

        self.horizontalLayout_27.addWidget(self.aug_infer_progress)

        self.aug_Close = QPushButton(self.horizontalFrame)
        self.aug_Close.setObjectName(u"aug_Close")
        self.aug_Close.setMinimumSize(QSize(30, 30))
        self.aug_Close.setMaximumSize(QSize(30, 30))
        self.aug_Close.setStyleSheet(u"QPushButton {\n"
"	background-color: #586796;\n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #996EB1;\n"
"	border: 2px solid #996EB1;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-media-stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.aug_Close.setIcon(icon9)

        self.horizontalLayout_27.addWidget(self.aug_Close)


        self.verticalLayout_25.addWidget(self.horizontalFrame)


        self.verticalLayout_24.addWidget(self.frame2)


        self.horizontalLayout_25.addLayout(self.verticalLayout_24)

        self.stackedWidget.addWidget(self.aug_page)
        self.detect_page = QWidget()
        self.detect_page.setObjectName(u"detect_page")
        self.horizontalLayout_34 = QHBoxLayout(self.detect_page)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.gridFrame = QFrame(self.detect_page)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setStyleSheet(u"QFrame#gridFrame{\n"
"border-image: url(:/images/images/images/detect_bg.png);\n"
"}")
        self.verticalLayout_42 = QVBoxLayout(self.gridFrame)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.gridFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_31.addWidget(self.label_9)

        self.lb_front_img = QLabel(self.frame_5)
        self.lb_front_img.setObjectName(u"lb_front_img")
        self.lb_front_img.setMinimumSize(QSize(300, 129))
        self.lb_front_img.setMaximumSize(QSize(600, 260))
        self.lb_front_img.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_31.addWidget(self.lb_front_img)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_31.addWidget(self.label_10)


        self.verticalLayout_42.addWidget(self.frame_5)

        self.frame_16 = QFrame(self.gridFrame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 40))
        self.frame_16.setMaximumSize(QSize(16777215, 80))
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.line_3 = QFrame(self.frame_16)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(0, 0))
        self.line_3.setMaximumSize(QSize(16777215, 16777215))
        self.line_3.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.line_3.setLineWidth(5000)
        self.line_3.setMidLineWidth(5000)
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_41.addWidget(self.line_3)


        self.verticalLayout_42.addWidget(self.frame_16)

        self.frame_7 = QFrame(self.gridFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.lb_left_img = QLabel(self.frame_7)
        self.lb_left_img.setObjectName(u"lb_left_img")
        self.lb_left_img.setMinimumSize(QSize(300, 129))
        self.lb_left_img.setMaximumSize(QSize(600, 260))
        self.lb_left_img.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.lb_left_img)

        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(40, 0))
        self.line.setMaximumSize(QSize(80, 16777215))
        self.line.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.line.setLineWidth(5000)
        self.line.setMidLineWidth(700)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_36.addWidget(self.line)

        self.frame3 = QFrame(self.frame_7)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setMaximumSize(QSize(100, 16777215))
        self.gridLayout_4 = QGridLayout(self.frame3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(1, 1, -1, -1)
        self.btn_front_img = QPushButton(self.frame3)
        self.btn_front_img.setObjectName(u"btn_front_img")
        self.btn_front_img.setMinimumSize(QSize(0, 0))
        self.btn_front_img.setMaximumSize(QSize(15, 15))
        self.btn_front_img.setFont(font4)
        self.btn_front_img.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/images/images/images/cil-hover.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-image: url(:/images/images/images/cil-default.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border-image: url(:/images/images/images/cil-press.png);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_front_img, 0, 3, 1, 1)

        self.btn_back_img = QPushButton(self.frame3)
        self.btn_back_img.setObjectName(u"btn_back_img")
        self.btn_back_img.setMinimumSize(QSize(0, 0))
        self.btn_back_img.setMaximumSize(QSize(15, 15))
        self.btn_back_img.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/images/images/images/cil-hover.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-image: url(:/images/images/images/cil-default.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border-image: url(:/images/images/images/cil-press.png);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_back_img, 2, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.btn_left_img = QPushButton(self.frame3)
        self.btn_left_img.setObjectName(u"btn_left_img")
        self.btn_left_img.setMinimumSize(QSize(0, 0))
        self.btn_left_img.setMaximumSize(QSize(15, 15))
        self.btn_left_img.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/images/images/images/cil-hover.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-image: url(:/images/images/images/cil-default.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border-image: url(:/images/images/images/cil-press.png);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_left_img, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.btn_right_img = QPushButton(self.frame3)
        self.btn_right_img.setObjectName(u"btn_right_img")
        self.btn_right_img.setMinimumSize(QSize(0, 0))
        self.btn_right_img.setMaximumSize(QSize(15, 15))
        self.btn_right_img.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/images/images/images/cil-hover.png);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border-image: url(:/images/images/images/cil-default.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	border-image: url(:/images/images/images/cil-press.png);\n"
"}")

        self.gridLayout_4.addWidget(self.btn_right_img, 1, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(0, 170, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 3, 1, 1)


        self.horizontalLayout_36.addWidget(self.frame3)

        self.line_2 = QFrame(self.frame_7)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(40, 0))
        self.line_2.setMaximumSize(QSize(80, 16777215))
        self.line_2.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.line_2.setLineWidth(5000)
        self.line_2.setMidLineWidth(700)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_36.addWidget(self.line_2)

        self.lb_right_img = QLabel(self.frame_7)
        self.lb_right_img.setObjectName(u"lb_right_img")
        self.lb_right_img.setMinimumSize(QSize(300, 129))
        self.lb_right_img.setMaximumSize(QSize(600, 260))

        self.horizontalLayout_36.addWidget(self.lb_right_img)


        self.verticalLayout_42.addWidget(self.frame_7)

        self.frame_17 = QFrame(self.gridFrame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 40))
        self.frame_17.setMaximumSize(QSize(16777215, 80))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.line_4 = QFrame(self.frame_17)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setMinimumSize(QSize(0, 0))
        self.line_4.setMaximumSize(QSize(16777215, 16777215))
        self.line_4.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.line_4.setLineWidth(5000)
        self.line_4.setMidLineWidth(5000)
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_42.addWidget(self.line_4)


        self.verticalLayout_42.addWidget(self.frame_17)

        self.frame_6 = QFrame(self.gridFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_35.addWidget(self.label_11)

        self.lb_back_img = QLabel(self.frame_6)
        self.lb_back_img.setObjectName(u"lb_back_img")
        self.lb_back_img.setMinimumSize(QSize(300, 129))
        self.lb_back_img.setMaximumSize(QSize(600, 260))
        self.lb_back_img.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_35.addWidget(self.lb_back_img)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_35.addWidget(self.label_12)


        self.verticalLayout_42.addWidget(self.frame_6)


        self.verticalLayout_34.addWidget(self.gridFrame)

        self.horizontalFrame_2 = QFrame(self.detect_page)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setMinimumSize(QSize(0, 50))
        self.horizontalFrame_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_33 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.detect_Start = QPushButton(self.horizontalFrame_2)
        self.detect_Start.setObjectName(u"detect_Start")
        self.detect_Start.setMinimumSize(QSize(30, 30))
        self.detect_Start.setMaximumSize(QSize(30, 30))
        self.detect_Start.setStyleSheet(u"QPushButton {\n"
"	background-color: #586796;\n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #996EB1;\n"
"	border: 2px solid #996EB1;\n"
"}")
        self.detect_Start.setIcon(icon7)

        self.horizontalLayout_33.addWidget(self.detect_Start)

        self.detect_Pause = QPushButton(self.horizontalFrame_2)
        self.detect_Pause.setObjectName(u"detect_Pause")
        self.detect_Pause.setMinimumSize(QSize(30, 30))
        self.detect_Pause.setMaximumSize(QSize(30, 30))
        self.detect_Pause.setStyleSheet(u"QPushButton {\n"
"	background-color: #586796;\n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #996EB1;\n"
"	border: 2px solid #996EB1;\n"
"}")
        self.detect_Pause.setIcon(icon8)

        self.horizontalLayout_33.addWidget(self.detect_Pause)

        self.detect_infer_progress = QProgressBar(self.horizontalFrame_2)
        self.detect_infer_progress.setObjectName(u"detect_infer_progress")
        self.detect_infer_progress.setMinimumSize(QSize(0, 30))
        self.detect_infer_progress.setMaximumSize(QSize(16777215, 30))
        self.detect_infer_progress.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(153, 110, 177);\n"
"text-align:center; \n"
"border:3px solid rgb(255, 255, 255);\n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(31, 84, 133, 200);\n"
"border-radius: 7px;\n"
"}")
        self.detect_infer_progress.setValue(0)

        self.horizontalLayout_33.addWidget(self.detect_infer_progress)

        self.detect_Close = QPushButton(self.horizontalFrame_2)
        self.detect_Close.setObjectName(u"detect_Close")
        self.detect_Close.setMinimumSize(QSize(30, 30))
        self.detect_Close.setMaximumSize(QSize(30, 30))
        self.detect_Close.setStyleSheet(u"QPushButton {\n"
"	background-color: #586796;\n"
"	border: none;  \n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #7082b6;\n"
"	border: 2px solid #7082b6;\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: #996EB1;\n"
"	border: 2px solid #996EB1;\n"
"}")
        self.detect_Close.setIcon(icon9)

        self.horizontalLayout_33.addWidget(self.detect_Close)


        self.verticalLayout_34.addWidget(self.horizontalFrame_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_34)

        self.verticalFrame_2 = QFrame(self.detect_page)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setMinimumSize(QSize(250, 0))
        self.verticalFrame_2.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_35 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.verticalFrame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 200))
        self.frame_8.setStyleSheet(u"QFrame#frame_8{\n"
"background-color: rgb(31, 84, 133);\n"
"border-radius:15px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_8)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(6, 6, 6, 6)
        self.frame_19 = QFrame(self.frame_8)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.lb_nowtime = QLabel(self.frame_19)
        self.lb_nowtime.setObjectName(u"lb_nowtime")
        self.lb_nowtime.setMaximumSize(QSize(16777215, 20))
        self.lb_nowtime.setFont(font3)
        self.lb_nowtime.setStyleSheet(u"font: 700 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_43.addWidget(self.lb_nowtime)

        self.lb_city = QLabel(self.frame_19)
        self.lb_city.setObjectName(u"lb_city")
        self.lb_city.setStyleSheet(u"font: 14pt \"\u9ed1\u4f53\";\n"
"color: rgb(255, 255, 255);")
        self.lb_city.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.lb_city)


        self.verticalLayout_43.addWidget(self.frame_19)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_39.setSpacing(9)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(20, 0, 0, 0)
        self.btn_weather = QPushButton(self.frame_11)
        self.btn_weather.setObjectName(u"btn_weather")
        self.btn_weather.setMinimumSize(QSize(40, 40))
        self.btn_weather.setMaximumSize(QSize(40, 40))
        self.btn_weather.setStyleSheet(u"border-image: url(:/weather/images/weather/\u4e2d\u96e8.png);")

        self.horizontalLayout_39.addWidget(self.btn_weather)

        self.lb_temp = QLabel(self.frame_11)
        self.lb_temp.setObjectName(u"lb_temp")
        self.lb_temp.setMaximumSize(QSize(80, 40))
        self.lb_temp.setStyleSheet(u"font: 700 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_39.addWidget(self.lb_temp)

        self.lb_weather = QLabel(self.frame_11)
        self.lb_weather.setObjectName(u"lb_weather")
        self.lb_weather.setMaximumSize(QSize(80, 40))
        self.lb_weather.setStyleSheet(u"font: 16pt \"\u9ed1\u4f53\";\n"
"color: rgb(255, 255, 255);")
        self.lb_weather.setTextFormat(Qt.TextFormat.AutoText)
        self.lb_weather.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.lb_weather)


        self.verticalLayout_43.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_13)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.pushButton_10 = QPushButton(self.frame_13)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 0))
        self.pushButton_10.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_10.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";\n"
"color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u":/weather/images/weather/\u98ce\u901f.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon10)

        self.verticalLayout_44.addWidget(self.pushButton_10)

        self.lb_windpower = QLabel(self.frame_13)
        self.lb_windpower.setObjectName(u"lb_windpower")
        self.lb_windpower.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.lb_windpower.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_44.addWidget(self.lb_windpower)


        self.horizontalLayout_40.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_14)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.pushButton_11 = QPushButton(self.frame_14)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 0))
        self.pushButton_11.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_11.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";\n"
"color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u":/weather/images/weather/\u98ce\u5411.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon11)

        self.verticalLayout_45.addWidget(self.pushButton_11)

        self.lb_winddirection = QLabel(self.frame_14)
        self.lb_winddirection.setObjectName(u"lb_winddirection")
        self.lb_winddirection.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.lb_winddirection.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_45.addWidget(self.lb_winddirection)


        self.horizontalLayout_40.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_15)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.pushButton_12 = QPushButton(self.frame_15)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 0))
        self.pushButton_12.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_12.setStyleSheet(u"font: 12pt \"\u9ed1\u4f53\";\n"
"color: rgb(255, 255, 255);")
        icon12 = QIcon()
        icon12.addFile(u":/weather/images/weather/\u6e7f\u5ea6.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon12)

        self.verticalLayout_46.addWidget(self.pushButton_12)

        self.lb_humidity = QLabel(self.frame_15)
        self.lb_humidity.setObjectName(u"lb_humidity")
        self.lb_humidity.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.lb_humidity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_46.addWidget(self.lb_humidity)


        self.horizontalLayout_40.addWidget(self.frame_15)


        self.verticalLayout_43.addWidget(self.frame_12)


        self.verticalLayout_35.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.verticalFrame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border-radius:15px;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.lb_map = QWebEngineView(self.frame_9)
        self.lb_map.setObjectName(u"lb_map")
        self.lb_map.setMinimumSize(QSize(0, 200))
        self.lb_map.setStyleSheet(u"")
        self.lb_map.setUrl(QUrl(u"qrc:/html/images/map.html"))

        self.horizontalLayout_37.addWidget(self.lb_map)


        self.verticalLayout_35.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.verticalFrame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 300))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_38.setSpacing(6)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 3, 0)
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.FPS = QFrame(self.frame_10)
        self.FPS.setObjectName(u"FPS")
        self.FPS.setStyleSheet(u"QFrame#FPS{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.FPS.setFrameShape(QFrame.Shape.StyledPanel)
        self.FPS.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.FPS)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(3, 3, 3, 3)
        self.label_13 = QLabel(self.FPS)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 700 italic 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_45.addWidget(self.label_13)

        self.lb_fps = QLabel(self.FPS)
        self.lb_fps.setObjectName(u"lb_fps")
        self.lb_fps.setStyleSheet(u"font: 8pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.lb_fps.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.lb_fps)


        self.verticalLayout_31.addWidget(self.FPS)

        self.num_object = QFrame(self.frame_10)
        self.num_object.setObjectName(u"num_object")
        self.num_object.setStyleSheet(u"QFrame#num_object{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.num_object.setFrameShape(QFrame.Shape.StyledPanel)
        self.num_object.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.num_object)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(3, 3, 3, 3)
        self.label_16 = QLabel(self.num_object)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"font: 700 italic 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_47.addWidget(self.label_16)

        self.lb_object = QLabel(self.num_object)
        self.lb_object.setObjectName(u"lb_object")
        self.lb_object.setStyleSheet(u"font: 8pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.lb_object.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.lb_object)


        self.verticalLayout_31.addWidget(self.num_object)

        self.num_category = QFrame(self.frame_10)
        self.num_category.setObjectName(u"num_category")
        self.num_category.setStyleSheet(u"QFrame#num_category{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.num_category.setFrameShape(QFrame.Shape.StyledPanel)
        self.num_category.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.num_category)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(3, 3, 3, 3)
        self.label_17 = QLabel(self.num_category)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 700 italic 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_46.addWidget(self.label_17)

        self.lb_category = QLabel(self.num_category)
        self.lb_category.setObjectName(u"lb_category")
        self.lb_category.setStyleSheet(u"font: 8pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.lb_category.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.lb_category)


        self.verticalLayout_31.addWidget(self.num_category)


        self.horizontalLayout_38.addLayout(self.verticalLayout_31)

        self.Information_frame = QFrame(self.frame_10)
        self.Information_frame.setObjectName(u"Information_frame")
        self.Information_frame.setMaximumSize(QSize(150, 16777215))
        self.Information_frame.setStyleSheet(u"QFrame#Information_frame{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.Information_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.Information_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.Information_frame)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_22 = QLabel(self.Information_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 700 italic 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_50.addWidget(self.label_22)

        self.lb_information = QTextEdit(self.Information_frame)
        self.lb_information.setObjectName(u"lb_information")
        self.lb_information.setMaximumSize(QSize(150, 16777215))
        self.lb_information.setStyleSheet(u"font: 8pt \"Segoe UI\";\n"
"color: rgb(33, 75, 115);\n"
"")

        self.verticalLayout_50.addWidget(self.lb_information)


        self.horizontalLayout_38.addWidget(self.Information_frame)


        self.verticalLayout_35.addWidget(self.frame_10)


        self.horizontalLayout_6.addWidget(self.verticalFrame_2)


        self.horizontalLayout_34.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.detect_page)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton.setIcon(icon1)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 3, 1, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 6, 4, 1)

        self.radioButton_4 = QRadioButton(self.row_2)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton_4, 0, 1, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.horizontalSlider, 3, 0, 1, 4)

        self.radioButton_3 = QRadioButton(self.row_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton_3, 0, 2, 1, 1)

        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon13)

        self.gridLayout_2.addWidget(self.commandLinkButton, 2, 8, 1, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 2, 0, 1, 4)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 224, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")

        self.horizontalLayout_11.addWidget(self.horizontalScrollBar)

        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 7, 4, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 4, 4, 1)

        self.checkBox_6 = QCheckBox(self.row_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setAutoFillBackground(False)
        self.checkBox_6.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox_6, 1, 0, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.NoPen)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.welcome_page.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.welcome_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_4 = QFrame(self.welcome_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 380))
        self.frame_4.setStyleSheet(u"background-image:url(:/images/images/images/iSea.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_20.addWidget(self.frame_4)

        self.label = QLabel(self.welcome_page)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 100))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"font: 700 20pt \"Segoe UI\";\n"
"color: rgb(90, 133, 186);")
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setMargin(0)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.welcome_page)
        self.bev_page = QWidget()
        self.bev_page.setObjectName(u"bev_page")
        self.horizontalLayout_26 = QHBoxLayout(self.bev_page)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_18 = QFrame(self.bev_page)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(300, 16777215))
        self.frame_18.setStyleSheet(u"QFrame#frame_18{\n"
"border-radius: 10px;\n"
"background-color: rgb(31, 84, 133);\n"
"}")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_18)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.clock = Clock(self.frame_18)
        self.clock.setObjectName(u"clock")

        self.verticalLayout_47.addWidget(self.clock)

        self.fps_gauge = GaugePanel(self.frame_18)
        self.fps_gauge.setObjectName(u"fps_gauge")

        self.verticalLayout_47.addWidget(self.fps_gauge)

        self.cpu_usage = ProgressRing(self.frame_18)
        self.cpu_usage.setObjectName(u"cpu_usage")

        self.verticalLayout_47.addWidget(self.cpu_usage)

        self.gpu_usage = ProgressRing(self.frame_18)
        self.gpu_usage.setObjectName(u"gpu_usage")

        self.verticalLayout_47.addWidget(self.gpu_usage)


        self.horizontalLayout_20.addWidget(self.frame_18)

        self.frame_2 = QFrame(self.bev_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(900, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lb_proj = QLabel(self.frame_2)
        self.lb_proj.setObjectName(u"lb_proj")
        self.lb_proj.setMinimumSize(QSize(0, 0))
        self.lb_proj.setStyleSheet(u"background-color: rgba(232, 232, 232,120);\n"
"border-image: url(:/images/images/images/\u6295\u5f71\u80cc\u666f.png);")

        self.horizontalLayout_22.addWidget(self.lb_proj)


        self.horizontalLayout_20.addWidget(self.frame_2)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_22 = QFrame(self.bev_page)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_51 = QVBoxLayout(self.frame_22)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.lb_infer_front1 = QLabel(self.frame_22)
        self.lb_infer_front1.setObjectName(u"lb_infer_front1")
        self.lb_infer_front1.setMinimumSize(QSize(0, 300))
        self.lb_infer_front1.setMaximumSize(QSize(16777215, 16777215))
        self.lb_infer_front1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_51.addWidget(self.lb_infer_front1)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setSpacing(20)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_33 = QFrame(self.frame_22)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(0, 300))
        self.layout_scatter = QVBoxLayout(self.frame_33)
        self.layout_scatter.setObjectName(u"layout_scatter")

        self.horizontalLayout_48.addWidget(self.frame_33)

        self.layout_pie = QVBoxLayout()
        self.layout_pie.setObjectName(u"layout_pie")

        self.horizontalLayout_48.addLayout(self.layout_pie)


        self.verticalLayout_51.addLayout(self.horizontalLayout_48)


        self.verticalLayout_29.addWidget(self.frame_22)

        self.layout_chart = QVBoxLayout()
        self.layout_chart.setObjectName(u"layout_chart")

        self.verticalLayout_29.addLayout(self.layout_chart)


        self.horizontalLayout_20.addLayout(self.verticalLayout_29)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_20)

        self.stackedWidget.addWidget(self.bev_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_saveScreen = QPushButton(self.topMenus)
        self.btn_saveScreen.setObjectName(u"btn_saveScreen")
        sizePolicy.setHeightForWidth(self.btn_saveScreen.sizePolicy().hasHeightForWidth())
        self.btn_saveScreen.setSizePolicy(sizePolicy)
        self.btn_saveScreen.setMinimumSize(QSize(0, 45))
        self.btn_saveScreen.setFont(font)
        self.btn_saveScreen.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_saveScreen.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_saveScreen.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-arrow-circle-bottom.png);")

        self.verticalLayout_14.addWidget(self.btn_saveScreen)

        self.btn_theme = QPushButton(self.topMenus)
        self.btn_theme.setObjectName(u"btn_theme")
        sizePolicy.setHeightForWidth(self.btn_theme.sizePolicy().hasHeightForWidth())
        self.btn_theme.setSizePolicy(sizePolicy)
        self.btn_theme.setMinimumSize(QSize(0, 45))
        self.btn_theme.setFont(font)
        self.btn_theme.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_theme.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_theme.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_14.addWidget(self.btn_theme)

        self.btn_contact = QPushButton(self.topMenus)
        self.btn_contact.setObjectName(u"btn_contact")
        sizePolicy.setHeightForWidth(self.btn_contact.sizePolicy().hasHeightForWidth())
        self.btn_contact.setSizePolicy(sizePolicy)
        self.btn_contact.setMinimumSize(QSize(0, 45))
        self.btn_contact.setFont(font)
        self.btn_contact.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_contact.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_contact.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speech.png);")

        self.verticalLayout_14.addWidget(self.btn_contact)

        self.btn_github = QPushButton(self.topMenus)
        self.btn_github.setObjectName(u"btn_github")
        sizePolicy.setHeightForWidth(self.btn_github.sizePolicy().hasHeightForWidth())
        self.btn_github.setSizePolicy(sizePolicy)
        self.btn_github.setMinimumSize(QSize(0, 45))
        self.btn_github.setFont(font)
        self.btn_github.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_github.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_github.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_github)


        self.verticalLayout_13.addWidget(self.topMenus)

        self.textEdit = QTextEdit(self.contentSettings)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_13.addWidget(self.textEdit)

        self.link_btn = QCommandLinkButton(self.contentSettings)
        self.link_btn.setObjectName(u"link_btn")
        self.link_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.link_btn.setStyleSheet(u"")
        self.link_btn.setIcon(icon13)

        self.verticalLayout_13.addWidget(self.link_btn)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.horizontalLayout_19.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"iSea", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Create by Li012", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a", None))
        self.btn_detect_page.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5272", None))
        self.btn_aug_page.setText(QCoreApplication.translate("MainWindow", u"\u589e\u5f3a", None))
        self.btn_bev_page.setText(QCoreApplication.translate("MainWindow", u"\u4fef\u89c6\u56fe", None))
        self.btn_monitor_page.setText(QCoreApplication.translate("MainWindow", u"\u4eea\u8868\u76d8", None))
        self.btn_detect.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5272\u53c2\u6570\u8bbe\u7f6e", None))
        self.btn_aug.setText(QCoreApplication.translate("MainWindow", u"\u589e\u5f3a\u53c2\u6570\u8bbe\u7f6e", None))
        self.extraLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u589e\u5f3a\u53c2\u6570", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn_2.setText("")
        self.check_rain.setText(QCoreApplication.translate("MainWindow", u"        Rain", None))
        self.check_fog.setText(QCoreApplication.translate("MainWindow", u"        Fog", None))
        self.check_dusk.setText(QCoreApplication.translate("MainWindow", u"        Dusk", None))
        self.check_night.setText(QCoreApplication.translate("MainWindow", u"        Night", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u53c2\u6570", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.btn_model_choose.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"  IoU", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u" Conf", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" Save", None))
        self.check_save_img.setText(QCoreApplication.translate("MainWindow", u"Save MP4/JPG", None))
        self.check_save_label.setText(QCoreApplication.translate("MainWindow", u"Save Labels(*.txt)", None))
#if QT_CONFIG(tooltip)
        self.btn_file.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.btn_file.setText("")
#if QT_CONFIG(tooltip)
        self.btn_help.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.btn_help.setText("")
        self.titleRightInfo.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"CPU:", None))
        self.lb_cpu_info.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CPU\u5360\u7528:", None))
        self.detect_lb_cpu_monitor.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"GPU\u5360\u7528:", None))
        self.detect_lb_gpu_monitor.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CPU \u6e29\u5ea6", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"GPU  \u6e29\u5ea6", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"GPU:", None))
        self.lb_gpu_info.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rain", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fog", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dusk", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Night", None))
        self.lb_pre_rain.setText("")
        self.lb_aug_rain.setText("")
        self.lb_pre_fog.setText("")
        self.lb_aug_fog.setText("")
        self.lb_pre_dusk.setText("")
        self.lb_aug_dusk.setText("")
        self.lb_pre_night.setText("")
        self.lb_aug_night.setText("")
        self.aug_Start.setText("")
        self.aug_Pause.setText("")
        self.aug_Close.setText("")
        self.label_9.setText("")
        self.lb_front_img.setText("")
        self.label_10.setText("")
        self.lb_left_img.setText("")
        self.btn_front_img.setText("")
        self.btn_back_img.setText("")
        self.btn_left_img.setText("")
        self.btn_right_img.setText("")
        self.lb_right_img.setText("")
        self.label_11.setText("")
        self.lb_back_img.setText("")
        self.label_12.setText("")
        self.detect_Start.setText("")
        self.detect_Pause.setText("")
        self.detect_Close.setText("")
        self.lb_nowtime.setText("")
        self.lb_city.setText(QCoreApplication.translate("MainWindow", u"\u9752\u5c9b", None))
        self.btn_weather.setText("")
        self.lb_temp.setText("")
        self.lb_weather.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u529b", None))
        self.lb_windpower.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u98ce\u5411", None))
        self.lb_winddirection.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u6e7f\u5ea6", None))
        self.lb_humidity.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.lb_fps.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.lb_object.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.lb_category.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Box Info", None))
        self.lb_information.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Wecome to iSea ^_^", None))
        self.lb_proj.setText("")
        self.lb_infer_front1.setText("")
        self.btn_saveScreen.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u622a\u56fe", None))
        self.btn_theme.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9898\u5207\u6362", None))
        self.btn_contact.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u6211\u4eec", None))
        self.btn_github.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">iSea</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Roc"
                        "ha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Lincense</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Li012</span></p></body></html>", None))
        self.link_btn.setText(QCoreApplication.translate("MainWindow", u"Github: li0123", None))
        self.link_btn.setDescription(QCoreApplication.translate("MainWindow", u"If you like this gui, please star me!", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Li012", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

