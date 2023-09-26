# Import semua library yang dibutuhkan
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, qRgb, QColor, QPixmap
from PyQt5.QtCore import QTimer
from Aritmaticalpanel import Ui_MainWindow as Ui_AritmaticalPanel

import numpy as np
import matplotlib.pyplot as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 753)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 540, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(720, 540, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pbInput = QtWidgets.QLabel(self.centralwidget)
        self.pbInput.setGeometry(QtCore.QRect(2, 22, 512, 512))
        self.pbInput.setAutoFillBackground(False)
        self.pbInput.setFrameShape(QtWidgets.QFrame.Box)
        self.pbInput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbInput.setLineWidth(1)
        self.pbInput.setText("")
        self.pbInput.setObjectName("pbInput")
        self.pbOutput = QtWidgets.QLabel(self.centralwidget)
        self.pbOutput.setGeometry(QtCore.QRect(520, 22, 512, 512))
        self.pbOutput.setFrameShape(QtWidgets.QFrame.Box)
        self.pbOutput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbOutput.setText("")
        self.pbOutput.setObjectName("pbOutput")
        self.labelInput = QtWidgets.QLabel(self.centralwidget)
        self.labelInput.setGeometry(QtCore.QRect(2, 540, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelInput.setFont(font)
        self.labelInput.setText("")
        self.labelInput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelInput.setObjectName("labelInput")
        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelOutput.setGeometry(QtCore.QRect(830, 540, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelOutput.setFont(font)
        self.labelOutput.setText("")
        self.labelOutput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelOutput.setObjectName("labelOutput")
        self.labelEfek = QtWidgets.QLabel(self.centralwidget)
        self.labelEfek.setGeometry(QtCore.QRect(12, 575, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelEfek.setFont(font)
        self.labelEfek.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelEfek.setObjectName("labelEfek")
        self.pbPreview = QtWidgets.QLabel(self.centralwidget)
        self.pbPreview.setGeometry(QtCore.QRect(415, 590, 96, 96))
        self.pbPreview.setAutoFillBackground(False)
        self.pbPreview.setFrameShape(QtWidgets.QFrame.Box)
        self.pbPreview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbPreview.setLineWidth(1)
        self.pbPreview.setText("")
        self.pbPreview.setObjectName("pbPreview")
        self.labelLoading = QtWidgets.QLabel(self.centralwidget)
        self.labelLoading.setGeometry(QtCore.QRect(520, 540, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelLoading.setFont(font)
        self.labelLoading.setText("")
        self.labelLoading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelLoading.setObjectName("labelLoading")
        self.labelWarning = QtWidgets.QLabel(self.centralwidget)
        self.labelWarning.setEnabled(True)
        self.labelWarning.setGeometry(QtCore.QRect(520, 600, 511, 105))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelWarning.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelWarning.setFont(font)
        self.labelWarning.setText("")
        self.labelWarning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelWarning.setObjectName("labelWarning")
        self.buttonImport = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImport.setGeometry(QtCore.QRect(415, 535, 101, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonImport.sizePolicy().hasHeightForWidth())
        self.buttonImport.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonImport.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonImport.setFont(font)
        self.buttonImport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonImport.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonImport.setObjectName("buttonImport")
        self.buttonUndo = QtWidgets.QPushButton(self.centralwidget)
        self.buttonUndo.setGeometry(QtCore.QRect(670, 570, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonUndo.sizePolicy().hasHeightForWidth())
        self.buttonUndo.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonUndo.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonUndo.setFont(font)
        self.buttonUndo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonUndo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonUndo.setObjectName("buttonUndo")
        self.buttonEffect1 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEffect1.setGeometry(QtCore.QRect(10, 600, 401, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEffect1.sizePolicy().hasHeightForWidth())
        self.buttonEffect1.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonEffect1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.buttonEffect1.setFont(font)
        self.buttonEffect1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEffect1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonEffect1.setStyleSheet("text-align: left;\n"
"")
        self.buttonEffect1.setObjectName("buttonEffect1")
        self.buttonEffect2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEffect2.setGeometry(QtCore.QRect(10, 630, 401, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEffect2.sizePolicy().hasHeightForWidth())
        self.buttonEffect2.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonEffect2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.buttonEffect2.setFont(font)
        self.buttonEffect2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEffect2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonEffect2.setStyleSheet("text-align: left;\n"
"")
        self.buttonEffect2.setObjectName("buttonEffect2")
        self.buttonEffect3 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEffect3.setGeometry(QtCore.QRect(10, 660, 401, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonEffect3.sizePolicy().hasHeightForWidth())
        self.buttonEffect3.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonEffect3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.buttonEffect3.setFont(font)
        self.buttonEffect3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEffect3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonEffect3.setStyleSheet("text-align: left;\n"
"")
        self.buttonEffect3.setObjectName("buttonEffect3")
        self.buttonSet = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSet.setGeometry(QtCore.QRect(790, 570, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSet.sizePolicy().hasHeightForWidth())
        self.buttonSet.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonSet.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonSet.setFont(font)
        self.buttonSet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonSet.setObjectName("buttonSet")
        self.buttonTetapImport = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTetapImport.setGeometry(QtCore.QRect(910, 680, 120, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonTetapImport.sizePolicy().hasHeightForWidth())
        self.buttonTetapImport.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.buttonTetapImport.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonTetapImport.setFont(font)
        self.buttonTetapImport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonTetapImport.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonTetapImport.setObjectName("buttonTetapImport")
        self.buttonSimpan = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSimpan.setGeometry(QtCore.QRect(910, 570, 121, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonSimpan.sizePolicy().hasHeightForWidth())
        self.buttonSimpan.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonSimpan.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonSimpan.setFont(font)
        self.buttonSimpan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonSimpan.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonSimpan.setObjectName("buttonSimpan")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(340, 0, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(770, 0, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHistogram = QtWidgets.QMenu(self.menuView)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icons8-histogram-100 (6).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuHistogram.setIcon(icon)
        self.menuHistogram.setObjectName("menuHistogram")
        self.menuColor = QtWidgets.QMenu(self.menubar)
        self.menuColor.setObjectName("menuColor")
        self.menuRGB = QtWidgets.QMenu(self.menuColor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/icons8-rgb-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRGB.setIcon(icon1)
        self.menuRGB.setObjectName("menuRGB")
        self.menuRGB_to_Grayscale = QtWidgets.QMenu(self.menuColor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/icons8-rgb-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRGB_to_Grayscale.setIcon(icon2)
        self.menuRGB_to_Grayscale.setObjectName("menuRGB_to_Grayscale")
        self.menuBit_Depth = QtWidgets.QMenu(self.menuColor)
        self.menuBit_Depth.setObjectName("menuBit_Depth")
        self.menuImage_Processing = QtWidgets.QMenu(self.menubar)
        self.menuImage_Processing.setObjectName("menuImage_Processing")
        self.menuAritmatics_Operation = QtWidgets.QMenu(self.menubar)
        self.menuAritmatics_Operation.setObjectName("menuAritmatics_Operation")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        self.menuEdge_Detection_2 = QtWidgets.QMenu(self.menuFilter)
        self.menuEdge_Detection_2.setObjectName("menuEdge_Detection_2")
        self.menuGaussian_Blur = QtWidgets.QMenu(self.menuFilter)
        self.menuGaussian_Blur.setObjectName("menuGaussian_Blur")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuMorphology = QtWidgets.QMenu(self.menubar)
        self.menuMorphology.setObjectName("menuMorphology")
        self.menuErosion = QtWidgets.QMenu(self.menuMorphology)
        self.menuErosion.setObjectName("menuErosion")
        self.menuOpening = QtWidgets.QMenu(self.menuMorphology)
        self.menuOpening.setObjectName("menuOpening")
        self.menuDilation = QtWidgets.QMenu(self.menuMorphology)
        self.menuDilation.setObjectName("menuDilation")
        self.menuClosing = QtWidgets.QMenu(self.menuMorphology)
        self.menuClosing.setObjectName("menuClosing")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuAppearance = QtWidgets.QMenu(self.menuAbout)
        self.menuAppearance.setObjectName("menuAppearance")
        self.menuType_Font = QtWidgets.QMenu(self.menuAppearance)
        self.menuType_Font.setObjectName("menuType_Font")
        self.menuAuto_Fit_Image = QtWidgets.QMenu(self.menuAppearance)
        self.menuAuto_Fit_Image.setObjectName("menuAuto_Fit_Image")
        self.menuInputBorderStyle = QtWidgets.QMenu(self.menuAppearance)
        self.menuInputBorderStyle.setObjectName("menuInputBorderStyle")
        self.menuSize_Font = QtWidgets.QMenu(self.menuAppearance)
        self.menuSize_Font.setObjectName("menuSize_Font")
        self.menuLanguage = QtWidgets.QMenu(self.menuAbout)
        self.menuLanguage.setObjectName("menuLanguage")
        self.menuThird_Apps = QtWidgets.QMenu(self.menuAbout)
        self.menuThird_Apps.setObjectName("menuThird_Apps")
        self.menuAbout_2 = QtWidgets.QMenu(self.menubar)
        self.menuAbout_2.setObjectName("menuAbout_2")
        self.menuGeometry = QtWidgets.QMenu(self.menubar)
        self.menuGeometry.setObjectName("menuGeometry")
        self.menuRotation = QtWidgets.QMenu(self.menuGeometry)
        self.menuRotation.setObjectName("menuRotation")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/icons8-open-file-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon3)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/icons8-save-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon4)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.actionInput = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/icons8-histogram-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInput.setIcon(icon6)
        self.actionInput.setObjectName("actionInput")
        self.actionOutput = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/icons8-histogram-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOutput.setIcon(icon7)
        self.actionOutput.setObjectName("actionOutput")
        self.actionInput_Output = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/icons8-histogram-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInput_Output.setIcon(icon8)
        self.actionInput_Output.setObjectName("actionInput_Output")
        self.actionBrightness = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/icons8-rgb-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrightness.setIcon(icon9)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionBrightness_Contrast = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icons/icons8-rgb-100 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrightness_Contrast.setIcon(icon10)
        self.actionBrightness_Contrast.setObjectName("actionBrightness_Contrast")
        self.actionLog_Brightness = QtWidgets.QAction(MainWindow)
        self.actionLog_Brightness.setObjectName("actionLog_Brightness")
        self.actionInvers = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Icons/icons8-rgb-100 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInvers.setIcon(icon11)
        self.actionInvers.setObjectName("actionInvers")
        self.actionGamma_Correction = QtWidgets.QAction(MainWindow)
        self.actionGamma_Correction.setObjectName("actionGamma_Correction")
        self.actionHistogram_Equalization_HE = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("Icons/icons8-histogram-100 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHistogram_Equalization_HE.setIcon(icon12)
        self.actionHistogram_Equalization_HE.setObjectName("actionHistogram_Equalization_HE")
        self.actionFuzzy_HE_RGB = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("Icons/icons8-histogram-100 (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFuzzy_HE_RGB.setIcon(icon13)
        self.actionFuzzy_HE_RGB.setObjectName("actionFuzzy_HE_RGB")
        self.actionFuzzy_to_Grayscale = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("Icons/icons8-histogram-100 (5).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFuzzy_to_Grayscale.setIcon(icon14)
        self.actionFuzzy_to_Grayscale.setObjectName("actionFuzzy_to_Grayscale")
        self.actionOpen_Aritmatics_Panel = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("Icons/icons8-math-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Aritmatics_Panel.setIcon(icon15)
        self.actionOpen_Aritmatics_Panel.setObjectName("actionOpen_Aritmatics_Panel")
        self.actionIdentity = QtWidgets.QAction(MainWindow)
        self.actionIdentity.setObjectName("actionIdentity")
        self.actionEdge_Detection_1 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_1.setObjectName("actionEdge_Detection_1")
        self.actionEdge_Detection_2 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_2.setObjectName("actionEdge_Detection_2")
        self.actionEdge_Detection_3 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_3.setObjectName("actionEdge_Detection_3")
        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionUnsharp_Masking = QtWidgets.QAction(MainWindow)
        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")
        self.actionAverage_Filter = QtWidgets.QAction(MainWindow)
        self.actionAverage_Filter.setObjectName("actionAverage_Filter")
        self.actionLow_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")
        self.actionHigh_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionHigh_Pass_Filter.setObjectName("actionHigh_Pass_Filter")
        self.actionBandstop_Filter = QtWidgets.QAction(MainWindow)
        self.actionBandstop_Filter.setObjectName("actionBandstop_Filter")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionRobert = QtWidgets.QAction(MainWindow)
        self.actionRobert.setObjectName("actionRobert")
        self.actionSquare_3 = QtWidgets.QAction(MainWindow)
        self.actionSquare_3.setObjectName("actionSquare_3")
        self.actionSquare_5 = QtWidgets.QAction(MainWindow)
        self.actionSquare_5.setObjectName("actionSquare_5")
        self.actionCross_3 = QtWidgets.QAction(MainWindow)
        self.actionCross_3.setObjectName("actionCross_3")
        self.actionSquare_4 = QtWidgets.QAction(MainWindow)
        self.actionSquare_4.setObjectName("actionSquare_4")
        self.actionSquare_6 = QtWidgets.QAction(MainWindow)
        self.actionSquare_6.setObjectName("actionSquare_6")
        self.actionCross_4 = QtWidgets.QAction(MainWindow)
        self.actionCross_4.setObjectName("actionCross_4")
        self.actionSquare_9 = QtWidgets.QAction(MainWindow)
        self.actionSquare_9.setObjectName("actionSquare_9")
        self.actionSquare_10 = QtWidgets.QAction(MainWindow)
        self.actionSquare_10.setObjectName("actionSquare_10")
        self.actionYellow = QtWidgets.QAction(MainWindow)
        self.actionYellow.setObjectName("actionYellow")
        self.actionCyan = QtWidgets.QAction(MainWindow)
        self.actionCyan.setObjectName("actionCyan")
        self.actionPurple = QtWidgets.QAction(MainWindow)
        self.actionPurple.setObjectName("actionPurple")
        self.actionRed = QtWidgets.QAction(MainWindow)
        self.actionRed.setObjectName("actionRed")
        self.actionBlue = QtWidgets.QAction(MainWindow)
        self.actionBlue.setObjectName("actionBlue")
        self.actionBlue_2 = QtWidgets.QAction(MainWindow)
        self.actionBlue_2.setObjectName("actionBlue_2")
        self.actionGray = QtWidgets.QAction(MainWindow)
        self.actionGray.setObjectName("actionGray")
        self.actionPink = QtWidgets.QAction(MainWindow)
        self.actionPink.setObjectName("actionPink")
        self.actionGray_2 = QtWidgets.QAction(MainWindow)
        self.actionGray_2.setObjectName("actionGray_2")
        self.actionAverage = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("Icons/icons8-rgba-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAverage.setIcon(icon16)
        self.actionAverage.setObjectName("actionAverage")
        self.actionLightness = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("Icons/icons8-rgba-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLightness.setIcon(icon17)
        self.actionLightness.setObjectName("actionLightness")
        self.actionLuminance = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("Icons/icons8-rgba-100 (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLuminance.setIcon(icon18)
        self.actionLuminance.setObjectName("actionLuminance")
        self.action1_Bit = QtWidgets.QAction(MainWindow)
        self.action1_Bit.setObjectName("action1_Bit")
        self.action2_Bit_4 = QtWidgets.QAction(MainWindow)
        self.action2_Bit_4.setObjectName("action2_Bit_4")
        self.action3_Bit = QtWidgets.QAction(MainWindow)
        self.action3_Bit.setObjectName("action3_Bit")
        self.action4_Bit_16 = QtWidgets.QAction(MainWindow)
        self.action4_Bit_16.setObjectName("action4_Bit_16")
        self.action5_Bit_32 = QtWidgets.QAction(MainWindow)
        self.action5_Bit_32.setObjectName("action5_Bit_32")
        self.action6_Bit_64 = QtWidgets.QAction(MainWindow)
        self.action6_Bit_64.setObjectName("action6_Bit_64")
        self.action7_Bit_128 = QtWidgets.QAction(MainWindow)
        self.action7_Bit_128.setObjectName("action7_Bit_128")
        self.action8_Bit_256 = QtWidgets.QAction(MainWindow)
        self.action8_Bit_256.setObjectName("action8_Bit_256")
        self.actionGaussian_Blur_3x3 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_3x3.setObjectName("actionGaussian_Blur_3x3")
        self.actionGaussian_Blur_5x5 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_5x5.setObjectName("actionGaussian_Blur_5x5")
        self.actionEnable = QtWidgets.QAction(MainWindow)
        self.actionEnable.setObjectName("actionEnable")
        self.actionDisable = QtWidgets.QAction(MainWindow)
        self.actionDisable.setObjectName("actionDisable")
        self.actionBox = QtWidgets.QAction(MainWindow)
        self.actionBox.setObjectName("actionBox")
        self.actionWindows = QtWidgets.QAction(MainWindow)
        self.actionWindows.setObjectName("actionWindows")
        self.actionNo_Border = QtWidgets.QAction(MainWindow)
        self.actionNo_Border.setObjectName("actionNo_Border")
        self.actionSegoe_UI = QtWidgets.QAction(MainWindow)
        self.actionSegoe_UI.setObjectName("actionSegoe_UI")
        self.action8_pt = QtWidgets.QAction(MainWindow)
        self.action8_pt.setObjectName("action8_pt")
        self.action9_pt = QtWidgets.QAction(MainWindow)
        self.action9_pt.setObjectName("action9_pt")
        self.action10_pt = QtWidgets.QAction(MainWindow)
        self.action10_pt.setObjectName("action10_pt")
        self.action11_pt = QtWidgets.QAction(MainWindow)
        self.action11_pt.setObjectName("action11_pt")
        self.action12_pt = QtWidgets.QAction(MainWindow)
        self.action12_pt.setObjectName("action12_pt")
        self.actionAbout_Apps = QtWidgets.QAction(MainWindow)
        self.actionAbout_Apps.setObjectName("actionAbout_Apps")
        self.actionCheck_For_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_For_Updates.setObjectName("actionCheck_For_Updates")
        self.actionEnglish_US = QtWidgets.QAction(MainWindow)
        self.actionEnglish_US.setObjectName("actionEnglish_US")
        self.actionIndonesia = QtWidgets.QAction(MainWindow)
        self.actionIndonesia.setObjectName("actionIndonesia")
        self.actionRemove_Background = QtWidgets.QAction(MainWindow)
        self.actionRemove_Background.setObjectName("actionRemove_Background")
        self.actionAI_HD_Photo_Upscaling = QtWidgets.QAction(MainWindow)
        self.actionAI_HD_Photo_Upscaling.setObjectName("actionAI_HD_Photo_Upscaling")
        self.actionAI_Image_Generator = QtWidgets.QAction(MainWindow)
        self.actionAI_Image_Generator.setObjectName("actionAI_Image_Generator")
        self.actionLucida_Sans = QtWidgets.QAction(MainWindow)
        self.actionLucida_Sans.setObjectName("actionLucida_Sans")
        self.actionPerpetua = QtWidgets.QAction(MainWindow)
        self.actionPerpetua.setObjectName("actionPerpetua")
        self.actionCanny = QtWidgets.QAction(MainWindow)
        self.actionCanny.setObjectName("actionCanny")
        self.actionKirsh = QtWidgets.QAction(MainWindow)
        self.actionKirsh.setObjectName("actionKirsh")
        self.actionScharr = QtWidgets.QAction(MainWindow)
        self.actionScharr.setObjectName("actionScharr")
        self.actionLaplacian = QtWidgets.QAction(MainWindow)
        self.actionLaplacian.setObjectName("actionLaplacian")
        self.actionLaplacian_of_Gaussian = QtWidgets.QAction(MainWindow)
        self.actionLaplacian_of_Gaussian.setObjectName("actionLaplacian_of_Gaussian")
        self.actionFlip = QtWidgets.QAction(MainWindow)
        self.actionFlip.setObjectName("actionFlip")
        self.actionCrop = QtWidgets.QAction(MainWindow)
        self.actionCrop.setObjectName("actionCrop")
        self.action90_degree = QtWidgets.QAction(MainWindow)
        self.action90_degree.setObjectName("action90_degree")
        self.action180_degree = QtWidgets.QAction(MainWindow)
        self.action180_degree.setObjectName("action180_degree")
        self.action270_degree = QtWidgets.QAction(MainWindow)
        self.action270_degree.setObjectName("action270_degree")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuHistogram.addAction(self.actionInput)
        self.menuHistogram.addAction(self.actionOutput)
        self.menuHistogram.addAction(self.actionInput_Output)
        self.menuView.addAction(self.menuHistogram.menuAction())
        self.menuRGB.addAction(self.actionYellow)
        self.menuRGB.addAction(self.actionCyan)
        self.menuRGB.addAction(self.actionPurple)
        self.menuRGB.addAction(self.actionRed)
        self.menuRGB.addAction(self.actionBlue)
        self.menuRGB.addAction(self.actionBlue_2)
        self.menuRGB.addAction(self.actionGray)
        self.menuRGB.addAction(self.actionPink)
        self.menuRGB.addAction(self.actionGray_2)
        self.menuRGB_to_Grayscale.addAction(self.actionAverage)
        self.menuRGB_to_Grayscale.addAction(self.actionLightness)
        self.menuRGB_to_Grayscale.addAction(self.actionLuminance)
        self.menuBit_Depth.addAction(self.action1_Bit)
        self.menuBit_Depth.addAction(self.action2_Bit_4)
        self.menuBit_Depth.addAction(self.action3_Bit)
        self.menuBit_Depth.addAction(self.action4_Bit_16)
        self.menuBit_Depth.addAction(self.action5_Bit_32)
        self.menuBit_Depth.addAction(self.action6_Bit_64)
        self.menuBit_Depth.addAction(self.action7_Bit_128)
        self.menuBit_Depth.addAction(self.action8_Bit_256)
        self.menuColor.addAction(self.menuRGB.menuAction())
        self.menuColor.addAction(self.menuRGB_to_Grayscale.menuAction())
        self.menuColor.addSeparator()
        self.menuColor.addAction(self.actionBrightness)
        self.menuColor.addAction(self.actionBrightness_Contrast)
        self.menuColor.addAction(self.actionLog_Brightness)
        self.menuColor.addSeparator()
        self.menuColor.addAction(self.actionInvers)
        self.menuColor.addAction(self.menuBit_Depth.menuAction())
        self.menuColor.addAction(self.actionGamma_Correction)
        self.menuImage_Processing.addAction(self.actionHistogram_Equalization_HE)
        self.menuImage_Processing.addAction(self.actionFuzzy_HE_RGB)
        self.menuImage_Processing.addAction(self.actionFuzzy_to_Grayscale)
        self.menuAritmatics_Operation.addAction(self.actionOpen_Aritmatics_Panel)
        self.menuEdge_Detection_2.addAction(self.actionEdge_Detection_1)
        self.menuEdge_Detection_2.addAction(self.actionEdge_Detection_2)
        self.menuEdge_Detection_2.addAction(self.actionEdge_Detection_3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_3x3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_5x5)
        self.menuFilter.addAction(self.actionIdentity)
        self.menuFilter.addAction(self.menuEdge_Detection_2.menuAction())
        self.menuFilter.addAction(self.actionSharpen)
        self.menuFilter.addAction(self.menuGaussian_Blur.menuAction())
        self.menuFilter.addAction(self.actionUnsharp_Masking)
        self.menuFilter.addSeparator()
        self.menuFilter.addAction(self.actionAverage_Filter)
        self.menuFilter.addAction(self.actionLow_Pass_Filter)
        self.menuFilter.addAction(self.actionHigh_Pass_Filter)
        self.menuFilter.addAction(self.actionBandstop_Filter)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionRobert)
        self.menuEdge_Detection.addAction(self.actionCanny)
        self.menuEdge_Detection.addSeparator()
        self.menuEdge_Detection.addAction(self.actionKirsh)
        self.menuEdge_Detection.addAction(self.actionScharr)
        self.menuEdge_Detection.addAction(self.actionLaplacian)
        self.menuEdge_Detection.addAction(self.actionLaplacian_of_Gaussian)
        self.menuErosion.addAction(self.actionSquare_3)
        self.menuErosion.addAction(self.actionSquare_5)
        self.menuErosion.addAction(self.actionCross_3)
        self.menuOpening.addAction(self.actionSquare_9)
        self.menuDilation.addAction(self.actionSquare_4)
        self.menuDilation.addAction(self.actionSquare_6)
        self.menuDilation.addAction(self.actionCross_4)
        self.menuClosing.addAction(self.actionSquare_10)
        self.menuMorphology.addAction(self.menuErosion.menuAction())
        self.menuMorphology.addAction(self.menuDilation.menuAction())
        self.menuMorphology.addAction(self.menuOpening.menuAction())
        self.menuMorphology.addAction(self.menuClosing.menuAction())
        self.menuType_Font.addAction(self.actionSegoe_UI)
        self.menuType_Font.addAction(self.actionLucida_Sans)
        self.menuType_Font.addAction(self.actionPerpetua)
        self.menuAuto_Fit_Image.addAction(self.actionEnable)
        self.menuAuto_Fit_Image.addAction(self.actionDisable)
        self.menuInputBorderStyle.addAction(self.actionBox)
        self.menuInputBorderStyle.addAction(self.actionWindows)
        self.menuInputBorderStyle.addAction(self.actionNo_Border)
        self.menuSize_Font.addAction(self.action8_pt)
        self.menuSize_Font.addAction(self.action9_pt)
        self.menuSize_Font.addAction(self.action10_pt)
        self.menuSize_Font.addAction(self.action11_pt)
        self.menuSize_Font.addAction(self.action12_pt)
        self.menuAppearance.addAction(self.menuInputBorderStyle.menuAction())
        self.menuAppearance.addAction(self.menuAuto_Fit_Image.menuAction())
        self.menuAppearance.addAction(self.menuType_Font.menuAction())
        self.menuAppearance.addAction(self.menuSize_Font.menuAction())
        self.menuLanguage.addAction(self.actionEnglish_US)
        self.menuLanguage.addAction(self.actionIndonesia)
        self.menuThird_Apps.addAction(self.actionRemove_Background)
        self.menuThird_Apps.addAction(self.actionAI_HD_Photo_Upscaling)
        self.menuThird_Apps.addAction(self.actionAI_Image_Generator)
        self.menuAbout.addAction(self.menuAppearance.menuAction())
        self.menuAbout.addAction(self.menuLanguage.menuAction())
        self.menuAbout.addAction(self.menuThird_Apps.menuAction())
        self.menuAbout_2.addAction(self.actionAbout_Apps)
        self.menuAbout_2.addAction(self.actionCheck_For_Updates)
        self.menuRotation.addAction(self.action270_degree)
        self.menuRotation.addAction(self.action90_degree)
        self.menuRotation.addAction(self.action180_degree)
        self.menuGeometry.addAction(self.actionFlip)
        self.menuGeometry.addAction(self.actionCrop)
        self.menuGeometry.addAction(self.menuRotation.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuColor.menuAction())
        self.menubar.addAction(self.menuImage_Processing.menuAction())
        self.menubar.addAction(self.menuAritmatics_Operation.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())
        self.menubar.addAction(self.menuGeometry.menuAction())
        self.menubar.addAction(self.menuMorphology.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuAbout_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikasi Pengolah Citra by Rizky Jein N. A"))
        self.label.setText(_translate("MainWindow", "Image 1"))
        self.label_2.setText(_translate("MainWindow", "Image 2"))
        self.labelEfek.setText(_translate("MainWindow", "Efek :"))
        self.buttonImport.setText(_translate("MainWindow", "Impor"))
        self.buttonUndo.setText(_translate("MainWindow", "Undo Efek"))
        self.buttonEffect1.setText(_translate("MainWindow", "Tidak ada efek 1"))
        self.buttonEffect2.setText(_translate("MainWindow", "Tidak ada efek 2"))
        self.buttonEffect3.setText(_translate("MainWindow", "Tidak ada efek 3"))
        self.buttonSet.setText(_translate("MainWindow", "Atur ke efek 1"))
        self.buttonTetapImport.setText(_translate("MainWindow", "Tetap Impor"))
        self.buttonSimpan.setText(_translate("MainWindow", "Simpan"))
        self.label_3.setText(_translate("MainWindow", "IMAGE PROCESSING"))
        self.label_4.setText(_translate("MainWindow", "Politeknik Negeri Jember | PSDKU Nganjuk"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Histogram"))
        self.menuColor.setTitle(_translate("MainWindow", "Color"))
        self.menuRGB.setTitle(_translate("MainWindow", "RGB"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Bit Depth"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuAritmatics_Operation.setTitle(_translate("MainWindow", "Aritmatics Operations"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuEdge_Detection_2.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuGaussian_Blur.setTitle(_translate("MainWindow", "Gaussian Blur"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuMorphology.setTitle(_translate("MainWindow", "Morphology"))
        self.menuErosion.setTitle(_translate("MainWindow", "Erosion"))
        self.menuOpening.setTitle(_translate("MainWindow", "Opening"))
        self.menuDilation.setTitle(_translate("MainWindow", "Dilation"))
        self.menuClosing.setTitle(_translate("MainWindow", "Closing"))
        self.menuAbout.setTitle(_translate("MainWindow", "Others"))
        self.menuAppearance.setTitle(_translate("MainWindow", "Appearance"))
        self.menuType_Font.setTitle(_translate("MainWindow", "Type Font"))
        self.menuAuto_Fit_Image.setTitle(_translate("MainWindow", "Auto Fit Image"))
        self.menuInputBorderStyle.setTitle(_translate("MainWindow", "InputBorderStyle"))
        self.menuSize_Font.setTitle(_translate("MainWindow", "Size Font"))
        self.menuLanguage.setTitle(_translate("MainWindow", "Language"))
        self.menuThird_Apps.setTitle(_translate("MainWindow", "Third Apps"))
        self.menuAbout_2.setTitle(_translate("MainWindow", "About"))
        self.menuGeometry.setTitle(_translate("MainWindow", "Geometry"))
        self.menuRotation.setTitle(_translate("MainWindow", "Rotation"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionInput_Output.setText(_translate("MainWindow", "Input Output"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionBrightness_Contrast.setText(_translate("MainWindow", "Brightness - Contrast"))
        self.actionLog_Brightness.setText(_translate("MainWindow", "Log Brightness"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.actionGamma_Correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.actionHistogram_Equalization_HE.setText(_translate("MainWindow", "Histogram Equalization (HE)"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionFuzzy_to_Grayscale.setText(_translate("MainWindow", "Fuzzy to Grayscale"))
        self.actionOpen_Aritmatics_Panel.setText(_translate("MainWindow", "Open Aritmatics Panel"))
        self.actionIdentity.setText(_translate("MainWindow", "Identity"))
        self.actionEdge_Detection_1.setText(_translate("MainWindow", "Edge Detection 1"))
        self.actionEdge_Detection_2.setText(_translate("MainWindow", "Edge Detection 2"))
        self.actionEdge_Detection_3.setText(_translate("MainWindow", "Edge Detection 3"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        self.actionAverage_Filter.setText(_translate("MainWindow", "Average Filter"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionHigh_Pass_Filter.setText(_translate("MainWindow", "High Pass Filter"))
        self.actionBandstop_Filter.setText(_translate("MainWindow", "Bandstop Filter"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionSquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_4.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_6.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_4.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionSquare_10.setText(_translate("MainWindow", "Square 9"))
        self.actionYellow.setText(_translate("MainWindow", "Yellow"))
        self.actionCyan.setText(_translate("MainWindow", "Cyan"))
        self.actionPurple.setText(_translate("MainWindow", "Purple"))
        self.actionRed.setText(_translate("MainWindow", "Red"))
        self.actionBlue.setText(_translate("MainWindow", "Green"))
        self.actionBlue_2.setText(_translate("MainWindow", "Blue"))
        self.actionGray.setText(_translate("MainWindow", "Orange"))
        self.actionPink.setText(_translate("MainWindow", "Pink"))
        self.actionGray_2.setText(_translate("MainWindow", "Gray"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.actionLuminance.setText(_translate("MainWindow", "Luminance"))
        self.action1_Bit.setText(_translate("MainWindow", "1 Bit (2)"))
        self.action2_Bit_4.setText(_translate("MainWindow", "2 Bit (4)"))
        self.action3_Bit.setText(_translate("MainWindow", "3 Bit (8)"))
        self.action4_Bit_16.setText(_translate("MainWindow", "4 Bit (16)"))
        self.action5_Bit_32.setText(_translate("MainWindow", "5 Bit (32)"))
        self.action6_Bit_64.setText(_translate("MainWindow", "6 Bit (64)"))
        self.action7_Bit_128.setText(_translate("MainWindow", "7 Bit (128)"))
        self.action8_Bit_256.setText(_translate("MainWindow", "8 Bit (256)"))
        self.actionGaussian_Blur_3x3.setText(_translate("MainWindow", "Gaussian Blur 3x3"))
        self.actionGaussian_Blur_5x5.setText(_translate("MainWindow", "Gaussian Blur 5x5"))
        self.actionEnable.setText(_translate("MainWindow", "Enable"))
        self.actionDisable.setText(_translate("MainWindow", "Disable"))
        self.actionBox.setText(_translate("MainWindow", "Box"))
        self.actionWindows.setText(_translate("MainWindow", "Windows"))
        self.actionNo_Border.setText(_translate("MainWindow", "No Border"))
        self.actionSegoe_UI.setText(_translate("MainWindow", "Segoe UI"))
        self.action8_pt.setText(_translate("MainWindow", "8 pt"))
        self.action9_pt.setText(_translate("MainWindow", "9 pt"))
        self.action10_pt.setText(_translate("MainWindow", "10 pt"))
        self.action11_pt.setText(_translate("MainWindow", "11 pt"))
        self.action12_pt.setText(_translate("MainWindow", "12 pt"))
        self.actionAbout_Apps.setText(_translate("MainWindow", "About Apps"))
        self.actionCheck_For_Updates.setText(_translate("MainWindow", "Check For Updates"))
        self.actionEnglish_US.setText(_translate("MainWindow", "English (US)"))
        self.actionIndonesia.setText(_translate("MainWindow", "Indonesia"))
        self.actionRemove_Background.setText(_translate("MainWindow", "Remove Background"))
        self.actionAI_HD_Photo_Upscaling.setText(_translate("MainWindow", "AI HD Photo and Upscaling"))
        self.actionAI_Image_Generator.setText(_translate("MainWindow", "AI Image Generator"))
        self.actionLucida_Sans.setText(_translate("MainWindow", "Lucida Sans"))
        self.actionPerpetua.setText(_translate("MainWindow", "Perpetua"))
        self.actionCanny.setText(_translate("MainWindow", "Canny"))
        self.actionKirsh.setText(_translate("MainWindow", "Kirsh"))
        self.actionScharr.setText(_translate("MainWindow", "Scharr"))
        self.actionLaplacian.setText(_translate("MainWindow", "Laplacian"))
        self.actionLaplacian_of_Gaussian.setText(_translate("MainWindow", "Laplacian of Gaussian"))
        self.actionFlip.setText(_translate("MainWindow", "Flip Horizontal"))
        self.actionCrop.setText(_translate("MainWindow", "Flip Vertical"))
        self.action90_degree.setText(_translate("MainWindow", "90 degree"))
        self.action180_degree.setText(_translate("MainWindow", "180 degree"))
        self.action270_degree.setText(_translate("MainWindow", "45 degree"))


        # ----------------------------------------------------------------------------------------------------------
        # PENDEFINISIAN OBJEK dan PENGATURAN TAMPILAN-----------------------------------------------------------------------------------------
        # mengosongkan data input dan output pixmap serta mengosongkan data String
        self.pixmap1 = None
        self.pixmap2 = None
        self.pixmap3 = None
        self.pixmap4 = None
        self.pixmap5 = None
        self.input_pixmap1 = None
        self.stringefek1 = None
        self.stringefek2 = None
        self.stringefek3 = None
        self.image_path = None
        self.width = None
        self.height = None

        # inisiasi objek timer, mengatur tampilan image preview dan menyembunyikan tombol
        self.timer = QTimer()
        self.timerEfek = QTimer()
        self.pbPreview.setScaledContents(True)

        self.buttonTetapImport.setVisible(False)
        self.buttonEffect3.setVisible(False)

        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI AKSI PADA MENU -----------------------------------------------------------------------------------------
        self.actionOpen.triggered.connect(self.loadImage) 
        self.actionSave_As.triggered.connect(self.saveImage)
        self.actionExit.triggered.connect(self.exitApplication)

        self.actionAverage.triggered.connect(self.convertToGreyscaleAverage)
        self.actionLightness.triggered.connect(self.convertToGreyscaleLightness) 
        self.actionLuminance.triggered.connect(self.convertToGreyscaleLuminance)
        self.actionBrightness.triggered.connect(self.applyContrastEffect)
        self.actionBrightness_Contrast.triggered.connect(self.showBrightnessContrastDialog)

        self.actionInvers.triggered.connect(self.convertToInvers)

        self.actionHistogram_Equalization_HE.triggered.connect(self.applyHistogramEqualization)
        self.actionFuzzy_HE_RGB.triggered.connect(self.fuzzy_he_rgb)
        self.actionFuzzy_to_Grayscale.triggered.connect(self.fuzzy_greyscale)

        self.actionOpen_Aritmatics_Panel.triggered.connect(self.open_aritmatics_panel)

        self.actionInput.triggered.connect(self.show_input_histogram)
        self.actionOutput.triggered.connect(self.show_output_histogram)


        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI AKSI PADA TOMBOL -----------------------------------------------------------------------------------------
        # TOMBOL IMPOR
        self.buttonImport.clicked.connect(self.loadImage)
        self.buttonSet.clicked.connect(self.aturefek)
        self.buttonUndo.clicked.connect(self.undoEfek)
        self.buttonSimpan.clicked.connect(self.saveImage)
        self.buttonTetapImport.clicked.connect(self.importImage)
        self.buttonEffect1.clicked.connect(self.showPreviewEffect1)
        self.buttonEffect2.clicked.connect(self.showPreviewEffect2)
        self.buttonEffect3.clicked.connect(self.showPreviewEffect3)


        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU FILE -----------------------------------------------------------------------------------------
        # 1) FUNGSI OPEN
    def loadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        
        self.image_path, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", 
                                                    "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)", options=options)
        
        if self.image_path:
            self.pixmap1 = QtGui.QPixmap(self.image_path)
            self.width = self.pixmap1.width()
            self.height = self.pixmap1.height()
            if (self.width > 1000 and self.height > 1000):
                self.labelWarning.setText("Ukuran gambar input terlalu besar!\nAplikasi mungkin akan berjalan lambat ketika melakukan operasi. Tetap lanjutkan?")
                self.buttonTetapImport.setVisible(True)
            else:
                self.importImage()

    def importImage(self):
                self.pbInput.setPixmap(self.pixmap1)
                self.pbInput.setScaledContents(True)
                self.pbOutput.setScaledContents(True)
                self.labelInput.setText(self.image_path)
                self.pixmap2 = None
                self.pixmap3 = None
                self.pixmap4 = None
                self.pixmap5 = None
                self.stringefek1 = None
                self.stringefek2 = None
                self.stringefek3 = None
                self.input_pixmap1 = None
                self.buttonEffect1.setText("Tidak ada efek 1")
                self.buttonEffect2.setText("Tidak ada efek 2")
                self.buttonEffect3.setText("Tidak ada efek 3")
                self.buttonSet.setText("Atur ke efek 1")
                self.labelOutput.setText(None)
                self.labelWarning.setText(None)
                self.buttonTetapImport.setVisible(False)
                self.showImageData()

        # 2) FUNGSI SAVE AS
    def saveImage(self):
        if (self.pbOutput.pixmap() is None):
             self.showWarningSave()
        else :
                options = QFileDialog.Options()
                options |= QFileDialog.ReadOnly
                
                self.image_path, _ = QFileDialog.getSaveFileName(None, "Save Image File", "", 
                                                        "PNG Files (*.png);;JPEG Files (*.jpg *.jpeg);;Bitmap Files (*.bmp);;All Files (*)", options=options)
                
                if self.image_path:
                # pixmap = self.pbInput.pixmap()
                        pixmap = self.pbOutput.pixmap()
                        if pixmap:
                                pixmap.save(self.image_path)

        # 3) FUNGSI EXIT
    def exitApplication(self):
        QtWidgets.qApp.quit()


        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU FILE -----------------------------------------------------------------------------------------
        # 1) RGB - KUNING
    def convertToYellowRGB(self):
        image = self.pbInput.pixmap().toImage()  # Mengambil gambar dari pbInput
        if image.isNull():
            return

        width = image.width()
        height = image.height()

        for y in range(height):
            for x in range(width):
                pixel = image.pixel(x, y)
                r, g, b, a = QColor(pixel).getRgb()  # Mendapatkan nilai R, G, B dari pixel

                # Konversi ke efek kuning dengan mengatur nilai G dan B ke 0
                new_pixel = QColor(r, 255, 100, a)  # Set G ke 255 (kuning) dan B ke 0

                # Tetapkan pixel baru ke gambar
                image.setPixel(x, y, new_pixel.rgb())

        # Tampilkan gambar yang sudah diubah pada pbOutput
        self.pbOutput.setPixmap(QPixmap.fromImage(image))
        self.pbOutput.setScaledContents(True)


        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU COLORS -----------------------------------------------------------------------------------------
        # 2) RGB TO GRAYSCALE - AVERAGE
    def convertToGreyscaleAverage(self):
        #     self.timerEfek.stop()
        #     self.timerEfek.setInterval(1000)
        #     self.timerEfek.start()
        #     if self.timerEfek.isActive:
        #         self.labelLoading.setText("Menerapkan Efek ...")
        #         self.timer.timeout.connect(self.clearLoading)
        #     else:
                input_image = self.pbInput.pixmap().toImage()
                width = input_image.width()
                height = input_image.height()
                
                # Buat gambar abu-abu dengan ukuran yang sama
                grey_image = QImage(width, height, QImage.Format_Grayscale8)
                
                for y in range(height):
                    for x in range(width):
                        pixel = input_image.pixel(x, y)
                        color = QtGui.QColor(pixel)
                        # Ambil nilai merah, hijau, dan biru dari warna pixel
                        red = color.red()
                        green = color.green()
                        blue = color.blue()
                        # Hitung nilai rata-rata komponen warna dan atur ke nilai abu-abu
                        grey_value = (red + green + blue) // 3
                        
                        grey_pixel = qRgb(grey_value, grey_value, grey_value)
                        grey_image.setPixel(x, y, grey_pixel)
                
                if (self.pixmap2 is None):
                        self.pixmap2 = grey_image
                        self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                        self.pbOutput.setScaledContents(True)
                        self.stringefek1 = 'Effect : Average '
                        self.labelOutput.setText(self.stringefek1)
                        self.showEffectComplete()
                elif (self.pixmap3 is None):
                        self.pixmap3 = grey_image
                        self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                        self.pbOutput.setScaledContents(True)
                        self.stringefek2 = 'Effect : Average '
                        self.labelOutput.setText(self.stringefek2)
                        self.showEffectComplete()
                elif (self.pixmap4 is None):
                        self.pixmap4 = grey_image
                        self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
                        self.pbOutput.setScaledContents(True)
                        self.stringefek3 = 'Effect : Average '
                        self.labelOutput.setText(self.stringefek3)
                        self.showEffectComplete()
                elif (self.pixmap5 is None):
                        self.pixmap5 = grey_image
                        self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap5))
                        self.pbOutput.setScaledContents(True)
                        self.showEffectComplete()

        # 2) RGB TO GRAYSCALE - LIGHTNESS
    def convertToGreyscaleLightness(self):
            input_image = self.pbInput.pixmap().toImage()
            width = input_image.width()
            height = input_image.height()
            
            # Buat gambar abu-abu dengan ukuran yang sama
            grey_image = QImage(width, height, QImage.Format_Grayscale8)
            
            for y in range(height):
                for x in range(width):
                    pixel = input_image.pixel(x, y)
                    color = QtGui.QColor(pixel)
                    # Ambil nilai merah, hijau, dan biru dari warna pixel
                    red = color.red()
                    green = color.green()
                    blue = color.blue()
                    # Hitung nilai kecerahan menggunakan metode Lightness
                    max_value = max(red, green, blue)
                    min_value = min(red, green, blue)
                    lightness = (max_value + min_value) // 2
                    grey_pixel = qRgb(lightness, lightness, lightness)
                    grey_image.setPixel(x, y, grey_pixel)
            
            if (self.pixmap2 is None):
                self.pixmap2 = grey_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Lightness '
                self.labelOutput.setText(self.stringefek1)
                self.showEffectComplete()
            elif (self.pixmap3 is None):
                self.pixmap3 = grey_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                self.pbOutput.setScaledContents(True)
                self.stringefek2 = 'Effect : Lightness '
                self.labelOutput.setText(self.stringefek2)
                self.showEffectComplete()
            elif (self.pixmap4 is None):
                self.pixmap4 = grey_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
                self.pbOutput.setScaledContents(True)
                self.stringefek3 = 'Effect : Lightness '
                self.labelOutput.setText(self.stringefek3)
                self.showEffectComplete()
            elif (self.pixmap5 is None):
                self.pixmap5 = grey_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap5))
                self.pbOutput.setScaledContents(True)
                self.showEffectComplete()

        # 2) RGB TO GRAYSCALE - LUMINANCE
    def convertToGreyscaleLuminance(self):
        # Ambil pixmap dari pbInput
        pixmap = self.pbInput.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width, height = img.width(), img.height()

            for y in range(height):
                for x in range(width):
                    pixel = img.pixel(x, y)
                    # Dapatkan nilai merah (red), hijau (green), dan biru (blue) dari pixel
                    red = QtGui.qRed(pixel)
                    green = QtGui.qGreen(pixel)
                    blue = QtGui.qBlue(pixel)
                    # Konversi RGB ke greyscale menggunakan formula Luminance
                    luminance = int(0.299 * red + 0.587 * green + 0.114 * blue)
                    # Buat warna greyscale
                    greyscale_color = QtGui.QColor(luminance, luminance, luminance)
                    # Set pixel ke warna greyscale pada gambar
                    img.setPixel(x, y, greyscale_color.rgb())

            # Terapkan gambar greyscale pada pbOutput
            if (self.pixmap2 is None):
                self.pixmap2 = QtGui.QPixmap.fromImage(img)
                self.pbOutput.setPixmap(self.pixmap2)
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Luminance '
                self.labelOutput.setText(self.stringefek1)
                self.showEffectComplete()
            elif (self.pixmap3 is None):
                self.pixmap3 = QtGui.QPixmap.fromImage(img)
                self.pbOutput.setPixmap(self.pixmap3)
                self.pbOutput.setScaledContents(True)
                self.stringefek2 = 'Effect : Luminance '
                self.labelOutput.setText(self.stringefek2)
                self.showEffectComplete()
            elif (self.pixmap4 is None):
                self.pixmap4 = QtGui.QPixmap.fromImage(img)
                self.pbOutput.setPixmap(self.pixmap4)
                self.pbOutput.setScaledContents(True)
                self.stringefek3 = 'Effect : Luminance '
                self.labelOutput.setText(self.stringefek3)
                self.showEffectComplete()
            elif (self.pixmap5 is None):
                self.pixmap5 = QtGui.QPixmap.fromImage(img)
                self.pbOutput.setPixmap(self.pixmap5)
                self.pbOutput.setScaledContents(True)
                self.showEffectComplete()

        # 6) INVERS
    def convertToInvers(self):
        # Ambil pixmap dari pbInput
            img = self.pbInput.pixmap().toImage()
            width, height = img.width(), img.height()

            for y in range(height):
                for x in range(width):
                    pixel = img.pixel(x, y)
                    # Dapatkan nilai merah (red), hijau (green), dan biru (blue) dari pixel
                    red = QtGui.qRed(pixel)
                    green = QtGui.qGreen(pixel)
                    blue = QtGui.qBlue(pixel)
                    # Inversi warna
                    inverted_color = QtGui.QColor(255 - red, 255 - green, 255 - blue)
                    # Set pixel ke warna invers pada gambar
                    img.setPixel(x, y, inverted_color.rgb())

            if (self.pixmap2 is None):
                self.pixmap2 = QtGui.QPixmap.fromImage(img)
                self.pbOutput.setPixmap(self.pixmap2)
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Invers '
                self.labelOutput.setText(self.stringefek1)
                self.showEffectComplete()
            elif (self.pixmap3 is None):
                self.pixmap3 = QtGui.QPixmap.fromImage(img)
                self.pbOutput.setPixmap(self.pixmap3)
                self.pbOutput.setScaledContents(True)
                self.stringefek2 = 'Effect : Invers '
                self.labelOutput.setText(self.stringefek2)
                self.showEffectComplete()
            elif (self.pixmap4 is None):
                self.pixmap4 = QtGui.QPixmap.fromImage(img)
                self.pbOutput.setPixmap(self.pixmap4)
                self.pbOutput.setScaledContents(True)
                self.stringefek3 = 'Effect : Invers '
                self.labelOutput.setText(self.stringefek3)
                self.showEffectComplete()
            elif (self.pixmap5 is None):
                self.pixmap5 = QtGui.QPixmap.fromImage(img)
                self.pbOutput.setPixmap(self.pixmap5)
                self.pbOutput.setScaledContents(True)
                self.showEffectComplete()

        # 3) BRIGHTNESS
    def applyContrastEffect(self):
        input_image = self.pixmap1.toImage()

        # Dapatkan ukuran gambar
        width = input_image.width()
        height = input_image.height()

        # Membuat salinan gambar untuk diubah
        output_image = QImage(width, height, QImage.Format_RGB32)

        # Faktor kontras (misalnya, 1.5 untuk meningkatkan kontras)
        contrast_factor = 1.5

        for x in range(width):
            for y in range(height):
                pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())

                # Mengubah nilai warna pixel dengan faktor kontras
                new_red = self.applyContrastToColor(pixel_color.red(), contrast_factor)
                new_green = self.applyContrastToColor(pixel_color.green(), contrast_factor)
                new_blue = self.applyContrastToColor(pixel_color.blue(), contrast_factor)

                # Menetapkan warna baru untuk pixel
                output_image.setPixelColor(x, y, QtGui.QColor(new_red, new_green, new_blue))

            if (self.pixmap2 is None):
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Brightness '
                self.labelOutput.setText(self.stringefek1)
                self.showEffectComplete()
            elif (self.pixmap3 is None):
                self.pixmap3 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek2 = 'Effect : Brightness '
                self.labelOutput.setText(self.stringefek2)
                self.showEffectComplete()
            elif (self.pixmap4 is None):
                self.pixmap4 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.stringefek3 = 'Effect : Brightness '
                self.labelOutput.setText(self.stringefek3)
                self.showEffectComplete()
            elif (self.pixmap5 is None):
                self.pixmap5 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(output_image))
                self.pbOutput.setScaledContents(True)
                self.showEffectComplete()
        
    def applyContrastToColor(self, color_value, contrast_factor):
        # Mengaplikasikan kontras pada nilai warna individual
        new_color_value = (color_value - 128) * contrast_factor + 128
        return max(0, min(255, int(new_color_value)))

        # 4) BRIGHTNESS - CONTRAST
    def showBrightnessContrastDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Brightness and Contrast")
        dialog.setModal(True)
        dialog.resize(300, 150)

        layout = QtWidgets.QVBoxLayout()

        # Tambahkan slider untuk brightness
        brightness_label = QtWidgets.QLabel("Brightness:")
        brightness_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        brightness_slider.setRange(-100, 100)
        brightness_slider.setValue(0)
        brightness_value_label = QtWidgets.QLabel("0")
        # Tambahkan slider untuk contrast
        contrast_label = QtWidgets.QLabel("Contrast:")
        contrast_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        contrast_slider.setRange(-100, 100)
        contrast_slider.setValue(0)
        contrast_value_label = QtWidgets.QLabel("0")

        # Tambahkan tombol "Apply"
        apply_button = QtWidgets.QPushButton("Apply")
        apply_button.clicked.connect(dialog.accept)

        layout.addWidget(brightness_label)
        layout.addWidget(brightness_slider)
        layout.addWidget(brightness_value_label) # Tambahkan label nilai brightness
        layout.addWidget(contrast_label)
        layout.addWidget(contrast_slider)
        layout.addWidget(contrast_value_label) # Tambahkan label nilai contrast
        layout.addWidget(apply_button)

        dialog.setLayout(layout)

        # Tambahkan label nilai brightness
        def updateBrightnessLabel(value):
            brightness_value_label.setText(str(value))
        # Tambahkan label nilai contrast
        def updateContrastLabel(value):
            contrast_value_label.setText(str(value))

        brightness_slider.valueChanged.connect(updateBrightnessLabel)
        contrast_slider.valueChanged.connect(updateContrastLabel)

        result = dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            # Dapatkan nilai brightness dan contrast yang dipilih
            brightness_value = brightness_slider.value()
            contrast_value = contrast_slider.value()
            # Terapkan efek brightness dan contrast ke gambar
            self.applyBrightnessContrast(brightness_value, contrast_value)

    def applyBrightnessContrast(self, brightness_value, contrast_value):
        # Konversi QPixmap ke QImage
            input_image = self.pixmap1.toImage()

            # Dapatkan ukuran gambar
            width = input_image.width()
            height = input_image.height()

            # Faktor brightness dari nilai slider (-100 hingga 100)
            brightness_factor = brightness_value / 100.0

            # Faktor contrast dari nilai slider (-100 hingga 100)
            contrast_factor = contrast_value / 100.0

            # Membuat salinan gambar untuk diubah
            output_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())

                    # Mengubah nilai warna pixel dengan faktor brightness
                    new_red = self.applyBrightnessToColor(pixel_color.red(), brightness_factor)
                    new_green = self.applyBrightnessToColor(pixel_color.green(), brightness_factor)
                    new_blue = self.applyBrightnessToColor(pixel_color.blue(), brightness_factor)

                    # Mengubah nilai warna pixel dengan faktor contrast
                    new_red = self.applyContrastToColor(new_red, contrast_factor)
                    new_green = self.applyContrastToColor(new_green, contrast_factor)
                    new_blue = self.applyContrastToColor(new_blue, contrast_factor)

                    # Menetapkan warna baru untuk pixel
                    output_image.setPixelColor(x, y, QtGui.QColor(new_red, new_green, new_blue))

            if (self.pixmap2 is None):
                self.pixmap2 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Brightness - Contrast '
                self.labelOutput.setText(self.stringefek1)
                self.showEffectComplete()
            elif (self.pixmap3 is None):
                self.pixmap3 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                self.pbOutput.setScaledContents(True)
                self.stringefek2 = 'Effect : Brightness - Contrast '
                self.labelOutput.setText(self.stringefek2)
                self.showEffectComplete()
            elif (self.pixmap4 is None):
                self.pixmap4 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
                self.pbOutput.setScaledContents(True)
                self.stringefek3 = 'Effect : Brightness - Contrast '
                self.labelOutput.setText(self.stringefek3)
                self.showEffectComplete()
            elif (self.pixmap5 is None):
                self.pixmap5 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap5))
                self.pbOutput.setScaledContents(True)
                self.showEffectComplete()
    
    def applyBrightnessToColor(self, color_value, brightness_factor):
        # Tambahkan logika untuk mengaplikasikan brightness pada warna di sini
        # Misalnya, Anda bisa menggunakan rumus color_value + brightness_factor
        new_color_value = color_value + brightness_factor
        # Pastikan nilai warna tetap dalam rentang 0-255
        new_color_value = max(0, min(255, new_color_value))

        return new_color_value
    
    #BIT DEPTH
    # def applyBitDepth(self, bit_depth):
    #     if self.input_pixmap1:
    #         # Konversi QPixmap ke QImage
    #         input_image = self.input_pixmap1.toImage()

    #         # Konversi bit depth gambar
    #         if bit_depth == 1:
    #             # Konversi ke 1 bit
    #             new_format = QtGui.QImage.Format_Mono
    #         elif bit_depth == 2:
    #             new_format = QtGui.QImage.Format_MonoLSB
    #         elif bit_depth == 3:
    #             new_format = QtGui.QImage.Format_Indexed8
    #         elif bit_depth == 4:
    #             new_format = QtGui.QImage.Format_RGB32
    #         elif bit_depth == 5:
    #             new_format = QtGui.QImage.Format_ARGB32
    #         elif bit_depth == 6:
    #             new_format = QtGui.QImage.Format_RGB888
    #         elif bit_depth == 7:
    #             new_format = QtGui.QImage.Format_RGB16

    #         # Mengonversi gambar ke format baru
    #         output_image = input_image.convertToFormat(new_format)

    #         # Mengubah QPixmap hasil ke dalam QLabel
    #         output_pixmap = QtGui.QPixmap.fromImage(output_image)
    #         self.pbOutput.setPixmap(output_pixmap)


        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU IMAGE PROCESSING -----------------------------------------------------------------------------------------
        #HISTOGRAM EQUALIZATION (HE)
    def applyHistogramEqualization(self):
            input_image = self.pixmap1.toImage()
            width = input_image.width()
            height = input_image.height()

            equalized_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Menghitung histogram
            histogram = [0] * 256
            total_pixels = width * height
            

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())
                    intensity = pixel_color.red()  # Kami asumsikan gambar grayscale

                    histogram[intensity] += 1

            # Menghitung distribusi kumulatif
            cumulative_distribution = [0] * 256
            cumulative_distribution[0] = histogram[0] / total_pixels

            for i in range(1, 256):
                cumulative_distribution[i] = cumulative_distribution[i - 1] + histogram[i] / total_pixels

            # Menyesuaikan nilai pixel pada gambar hasil
            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())
                    intensity = pixel_color.red()  # Kami asumsikan gambar grayscale

                    new_intensity = int(255 * cumulative_distribution[intensity])
                    new_color = QtGui.QColor(new_intensity, new_intensity, new_intensity)
                    equalized_image.setPixelColor(x, y, new_color)
            
            if (self.pixmap2 is None):
                self.pixmap2 = equalized_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Histogram Equalization '
                self.labelOutput.setText(self.stringefek1)
                self.showEffectComplete()
            elif (self.pixmap3 is None):
                self.pixmap3 = equalized_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                self.pbOutput.setScaledContents(True)
                self.stringefek2 = 'Effect : Histogram Equalization '
                self.labelOutput.setText(self.stringefek2)
                self.showEffectComplete()
            elif (self.pixmap4 is None):
                self.pixmap4 = equalized_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
                self.pbOutput.setScaledContents(True)
                self.stringefek3 = 'Effect : Histogram Equalization '
                self.labelOutput.setText(self.stringefek3)
                self.showEffectComplete()
            elif (self.pixmap5 is None):
                self.pixmap5 = equalized_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap5))
                self.pbOutput.setScaledContents(True)
                self.showEffectComplete()

        #FUZZY HISTOGRAM EQUALIZATION (HE) RGB
    def fuzzy_he_rgb(self):
            input_image = self.pixmap1.toImage()
            width = input_image.width()
            height = input_image.height()

            # Mengambil data piksel dari gambar input
            input_data = np.zeros((height, width, 3), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = QColor(input_image.pixel(x, y))
                    input_data[y, x, 0] = color.red()
                    input_data[y, x, 1] = color.green()
                    input_data[y, x, 2] = color.blue()

            # Menerapkan rumus Fuzzy HE RGB
            output_data = np.zeros_like(input_data)
            for i in range(3):  # Loop untuk saluran warna (R, G, B)
                for y in range(height):
                    for x in range(width):
                        val = input_data[y, x, i]
                        if val < 128:
                            output_data[y, x, i] = int(2 * val ** 2 / 255.0)
                        else:
                            output_data[y, x, i] = int(255 - 2 * (255 - val) ** 2 / 255.0)

            # Membuat gambar output dan menampilkannya di pbOutput
            output_image = QImage(output_data.data, width, height, width * 3, QImage.Format_RGB888)
            if (self.pixmap2 is None):
                self.pixmap2 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Fuzzy HE RGB '
                self.labelOutput.setText(self.stringefek1)
                self.showEffectComplete()
            elif (self.pixmap3 is None):
                self.pixmap3 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                self.pbOutput.setScaledContents(True)
                self.stringefek2 = 'Effect : Fuzzy HE RGB '
                self.labelOutput.setText(self.stringefek2)
                self.showEffectComplete()
            elif (self.pixmap4 is None):
                self.pixmap4 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
                self.pbOutput.setScaledContents(True)
                self.stringefek3 = 'Effect : Fuzzy HE RGB '
                self.labelOutput.setText(self.stringefek3)
                self.showEffectComplete()
            elif (self.pixmap5 is None):
                self.pixmap5 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap5))
                self.pbOutput.setScaledContents(True)
                self.showEffectComplete()

        #FUZZY TO GRAYSCALE
    def fuzzy_greyscale(self):
            input_image = self.pixmap1.toImage()
            width = input_image.width()
            height = input_image.height()

            # Mengambil data piksel dari gambar input
            input_data = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = QColor(input_image.pixel(x, y))
                    # Menghitung nilai greyscale menggunakan rumus Fuzzy
                    val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                    input_data[y, x] = val

            # Membuat gambar output dan menampilkannya di pbOutput
            output_image = QImage(input_data.data, width, height, width, QImage.Format_Grayscale8)
            if (self.pixmap2 is None):
                self.pixmap2 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                self.pbOutput.setScaledContents(True)
                self.stringefek1 = 'Effect : Fuzzy to Grayscale '
                self.labelOutput.setText(self.stringefek1)
                self.showEffectComplete()
            elif (self.pixmap3 is None):
                self.pixmap3 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                self.pbOutput.setScaledContents(True)
                self.stringefek2 = 'Effect : Fuzzy to Grayscale '
                self.labelOutput.setText(self.stringefek2)
                self.showEffectComplete()
            elif (self.pixmap4 is None):
                self.pixmap4 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
                self.pbOutput.setScaledContents(True)
                self.stringefek3 = 'Effect : Fuzzy to Grayscale '
                self.labelOutput.setText(self.stringefek3)
                self.showEffectComplete()
            elif (self.pixmap5 is None):
                self.pixmap5 = output_image
                self.pbOutput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap5))
                self.pbOutput.setScaledContents(True)
                self.showEffectComplete()
            

        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI MENU VIEW -----------------------------------------------------------------------------------------
        # HISTOGRAM INPUT
    def show_input_histogram(self):
        if self.pixmap5 is not None:
            if isinstance(self.pixmap5, QtGui.QImage):
                input_image = self.pixmap5
            elif isinstance(self.pixmap5, QtGui.QPixmap):
                input_image = self.pixmap5.toImage()
        elif self.pixmap4 is not None:
            if isinstance(self.pixmap4, QtGui.QImage):
                input_image = self.pixmap4
            elif isinstance(self.pixmap4, QtGui.QPixmap):
                input_image = self.pixmap4.toImage()
        elif self.pixmap3 is not None:
            if isinstance(self.pixmap3, QtGui.QImage):
                input_image = self.pixmap2
            elif isinstance(self.pixmap3, QtGui.QPixmap):
                input_image = self.pixmap3.toImage()
        elif self.pixmap2 is not None:
            if isinstance(self.pixmap2, QtGui.QImage):
                self.pixmap2 = QtGui.QPixmap(self.image_path)
                input_image = self.pixmap2
            elif isinstance(self.pixmap2, QtGui.QPixmap):
                input_image = self.pixmap2.toImage()
        elif self.pixmap1 is not None:
            input_image = self.pixmap1.toImage()

            # Mengambil data piksel dari gambar input
            width = input_image.width()
            height = input_image.height()
            input_data = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = QColor(input_image.pixel(x, y))
                    val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                    input_data[y, x] = val

            # Menghitung histogram
            histogram, bins = np.histogram(input_data, bins=256, range=(0, 256))

            # Menampilkan grafik histogram
            plt.figure(figsize=(8, 6))
            plt.bar(bins[:-1], histogram, width=1, color='blue')
            plt.title('Histogram Input')
            plt.xlabel('Intensitas Piksel')
            plt.ylabel('Frekuensi')
            plt.show()
    
        #HISTOGRAM OUTPUT
    def show_output_histogram(self):
        if self.pixmap5 is not None:
            if isinstance(self.pixmap5, QtGui.QImage):
                output_image = self.pixmap5
            elif isinstance(self.pixmap5, QtGui.QPixmap):
                output_image = self.pixmap5.toImage()
        elif self.pixmap4 is not None:
            if isinstance(self.pixmap4, QtGui.QImage):
                output_image = self.pixmap4
            elif isinstance(self.pixmap4, QtGui.QPixmap):
                output_image = self.pixmap4.toImage()
        elif self.pixmap3 is not None:
            if isinstance(self.pixmap3, QtGui.QImage):
                output_image = self.pixmap2
            elif isinstance(self.pixmap3, QtGui.QPixmap):
                output_image = self.pixmap3.toImage()
        elif self.pixmap2 is not None:
            if isinstance(self.pixmap2, QtGui.QImage):
                self.pixmap2 = QtGui.QPixmap(self.image_path)
                output_image = self.pixmap2
            elif isinstance(self.pixmap2, QtGui.QPixmap):
                output_image = self.pixmap2.toImage()
        elif self.pixmap1 is not None:
            output_image = self.pixmap1.toImage()

            width = output_image.width()
            height = output_image.height()
            output_data = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = QColor(output_image.pixel(x, y))
                    val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                    output_data[y, x] = val

            histogram, bins = np.histogram(output_data, bins=256, range=(0, 256))

            plt.figure(figsize=(8, 6))
            plt.bar(bins[:-1], histogram, width=1, color='green')
            plt.title('Histogram Output')
            plt.xlabel('Intensitas Piksel')
            plt.ylabel('Frekuensi')
            plt.show()

        # ----------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------------------------------
        # FUNGSI AKSI PADA TOMBOL ----------------------------------------------------------------------------------
        # ATUR KE EFEK
    def aturefek(self):
        if (self.stringefek3 is not None):
                if isinstance(self.pixmap4, QtGui.QImage):
                        self.pbInput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
                        self.pbOutput.setPixmap(QtGui.QPixmap())
                        self.buttonEffect3.setText(self.stringefek3)
                        self.buttonSet.setText("Efek Penuh")
                        self.buttonSet.setEnabled(False)
                        self.labelOutput.setText(None)
                elif isinstance(self.pixmap4, QtGui.QPixmap):
                        self.pbInput.setPixmap(self.pixmap4)
                        self.pbOutput.setPixmap(QtGui.QPixmap())
                        self.buttonEffect3.setText(self.stringefek3)
                        self.buttonSet.setText("Efek Penuh")
                        self.buttonSet.setEnabled(False)
                        self.labelOutput.setText(None)
                else: self.showWarningAtur1()
        elif (self.stringefek2 is not None):
                if isinstance(self.pixmap3, QtGui.QImage):
                        self.pbInput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                        self.pbOutput.setPixmap(QtGui.QPixmap())
                        self.buttonEffect2.setText(self.stringefek2)
                        self.buttonSet.setText("Atur ke efek 3")
                        self.labelOutput.setText(None)
                elif isinstance(self.pixmap3, QtGui.QPixmap):
                        self.pbInput.setPixmap(self.pixmap3)
                        self.pbOutput.setPixmap(QtGui.QPixmap())
                        self.buttonEffect2.setText(self.stringefek2)
                        self.buttonSet.setText("Atur ke efek 3")
                        self.labelOutput.setText(None)
                else: self.showWarningAtur1()
        elif (self.stringefek1 is not None):
                if isinstance(self.pixmap2, QtGui.QImage):
                        self.pbInput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                        self.pbOutput.setPixmap(QtGui.QPixmap())
                        self.buttonEffect1.setText(self.stringefek1)
                        self.buttonSet.setText("Atur ke efek 2")
                        self.labelOutput.setText(None)
                elif isinstance(self.pixmap2, QtGui.QPixmap):
                        self.pbInput.setPixmap(self.pixmap2)
                        self.pbOutput.setPixmap(QtGui.QPixmap())
                        self.buttonEffect1.setText(self.stringefek1)
                        self.buttonSet.setText("Atur ke efek 2")
                        self.labelOutput.setText(None)
                else: self.showWarningAtur1()

    def undoEfek(self):
         if(self.pixmap4 is not None):
                self.stringefek3 = None
                self.pixmap4 = None
                if isinstance(self.pixmap3, QtGui.QImage):
                        self.pbInput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
                elif isinstance(self.pixmap3, QtGui.QPixmap):
                        self.pbInput.setPixmap(self.pixmap3)
                self.pbOutput.setPixmap(QtGui.QPixmap())
                self.buttonEffect3.setText("Tidak ada efek 3")
                self.buttonSet.setText("Atur ke efek 3")
                self.buttonSet.setEnabled(True)
                self.labelOutput.setText(None)
                self.pbPreview.setPixmap(QtGui.QPixmap())
         elif(self.pixmap3 is not None):
                self.stringefek2 = None
                self.pixmap3 = None
                if isinstance(self.pixmap2, QtGui.QImage):
                        self.pbInput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
                elif isinstance(self.pixmap2, QtGui.QPixmap):
                        self.pbInput.setPixmap(self.pixmap2)
                self.pbOutput.setPixmap(QtGui.QPixmap())
                self.buttonEffect2.setText("Tidak ada efek 2")
                self.buttonSet.setText("Atur ke efek 2")
                self.labelOutput.setText(None)
                self.pbPreview.setPixmap(QtGui.QPixmap())
         elif(self.pixmap2 is not None):
                self.stringefek1 = None
                self.pixmap2 = None
                if isinstance(self.pixmap1, QtGui.QImage):
                        self.pbInput.setPixmap(QtGui.QPixmap.fromImage(self.pixmap1))
                elif isinstance(self.pixmap1, QtGui.QPixmap):
                        self.pbInput.setPixmap(self.pixmap1)
                self.pbOutput.setPixmap(QtGui.QPixmap())
                self.buttonEffect1.setText("Tidak ada efek 1")
                self.buttonSet.setText("Atur ke efek 1")
                self.labelOutput.setText(None)
                self.pbPreview.setPixmap(QtGui.QPixmap())
 
    def showWarning(self):
        self.labelWarning.setText("Tidak ada efek yang diterapkan pada Gambar Keluaran")
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()

    def showWarningAtur1(self):
        self.labelWarning.setText("Efek tidak dapat diatur!")
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()

    def showImageData(self):
        if (self.width > 1000 and self.height > 1000):
             self.labelWarning.setText("<b>Lebar Gambar (Width) :</b> " + str(self.width) + "<br><b>Tinggi Gambar (Height) :</b> " + str(self.height) + "<br>Gambar dengan resolusi di atas 1000 x 1000 mungkin akan memakan lebih<br>banyak waktu ketika menerapkan efek")
        else:
             self.labelWarning.setText("<b>Lebar Gambar (Width) :</b> " + str(self.width) + "<br><b>Tinggi Gambar (Height) :</b> " + str(self.height))
        self.timer.setInterval(30000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()

    def showWarningSave(self):
        self.labelWarning.setText("Gambar output kosong\nHarap tambahkan efek untuk menampilkan pada gambar output")
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()

    def showEffectComplete(self):
        self.labelLoading.setText("<b>Efek berhasil diterapkan</b>")
        self.timerEfek.setInterval(3000)
        self.timerEfek.timeout.connect(self.clearLoading)
        self.timerEfek.start()

    def clearLoading(self):
        self.labelLoading.clear()
        self.timerEfek.stop()

    def clearWarning(self):
        self.labelWarning.clear()
        self.timer.stop()

    def showPreviewEffect1(self):
        if isinstance(self.pixmap2, QtGui.QImage):
                self.pbPreview.setPixmap(QtGui.QPixmap.fromImage(self.pixmap2))
        elif isinstance(self.pixmap2, QtGui.QPixmap):
                self.pbPreview.setPixmap(self.pixmap2)

    def showPreviewEffect2(self):
        if isinstance(self.pixmap3, QtGui.QImage):
                self.pbPreview.setPixmap(QtGui.QPixmap.fromImage(self.pixmap3))
        elif isinstance(self.pixmap3, QtGui.QPixmap):
                self.pbPreview.setPixmap(self.pixmap3)

    def showPreviewEffect3(self):
        if isinstance(self.pixmap4, QtGui.QImage):
                self.pbPreview.setPixmap(QtGui.QPixmap.fromImage(self.pixmap4))
        elif isinstance(self.pixmap4, QtGui.QPixmap):
                self.pbPreview.setPixmap(self.pixmap4)

    def open_aritmatics_panel(self):
        self.aritmatics_panel = QtWidgets.QMainWindow()
        ui = Ui_AritmaticalPanel()
        ui.setupUi(self.aritmatics_panel)
        self.aritmatics_panel.show()

# END OF LOGIC CODE --------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
