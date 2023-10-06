from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer
# from Mainapp import Ui_MainWindow

class Ui_MainWindows(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 675)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(5, 0, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pbInput1 = QtWidgets.QLabel(self.centralwidget)
        self.pbInput1.setGeometry(QtCore.QRect(5, 50, 256, 256))
        self.pbInput1.setAutoFillBackground(False)
        self.pbInput1.setFrameShape(QtWidgets.QFrame.Panel)
        self.pbInput1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbInput1.setLineWidth(1)
        self.pbInput1.setText("")
        self.pbInput1.setObjectName("pbInput1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 320, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pbInput2 = QtWidgets.QLabel(self.centralwidget)
        self.pbInput2.setGeometry(QtCore.QRect(5, 370, 256, 256))
        self.pbInput2.setAutoFillBackground(False)
        self.pbInput2.setFrameShape(QtWidgets.QFrame.Panel)
        self.pbInput2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbInput2.setLineWidth(1)
        self.pbInput2.setText("")
        self.pbInput2.setObjectName("pbInput2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 0, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pbOutput = QtWidgets.QLabel(self.centralwidget)
        self.pbOutput.setGeometry(QtCore.QRect(280, 30, 512, 512))
        self.pbOutput.setAutoFillBackground(False)
        self.pbOutput.setFrameShape(QtWidgets.QFrame.Panel)
        self.pbOutput.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pbOutput.setLineWidth(1)
        self.pbOutput.setText("")
        self.pbOutput.setObjectName("pbOutput")
        self.labelOutput = QtWidgets.QLabel(self.centralwidget)
        self.labelOutput.setGeometry(QtCore.QRect(440, 0, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelOutput.setFont(font)
        self.labelOutput.setText("")
        self.labelOutput.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelOutput.setObjectName("labelOutput")
        self.labelLoading = QtWidgets.QLabel(self.centralwidget)
        self.labelLoading.setGeometry(QtCore.QRect(280, 540, 241, 21))
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
        self.labelWarning.setGeometry(QtCore.QRect(280, 570, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelWarning.setFont(font)
        self.labelWarning.setText("")
        self.labelWarning.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelWarning.setObjectName("labelWarning")
        self.buttonImport1 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImport1.setGeometry(QtCore.QRect(183, 3, 80, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonImport1.sizePolicy().hasHeightForWidth())
        self.buttonImport1.setSizePolicy(sizePolicy)
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
        self.buttonImport1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonImport1.setFont(font)
        self.buttonImport1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonImport1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonImport1.setObjectName("buttonImport1")
        self.buttonImport2 = QtWidgets.QPushButton(self.centralwidget)
        self.buttonImport2.setGeometry(QtCore.QRect(183, 323, 80, 28))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonImport2.sizePolicy().hasHeightForWidth())
        self.buttonImport2.setSizePolicy(sizePolicy)
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
        self.buttonImport2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        self.buttonImport2.setFont(font)
        self.buttonImport2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonImport2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonImport2.setObjectName("buttonImport2")
        self.labelPath2 = QtWidgets.QLabel(self.centralwidget)
        self.labelPath2.setGeometry(QtCore.QRect(5, 350, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelPath2.setFont(font)
        self.labelPath2.setText("")
        self.labelPath2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelPath2.setObjectName("labelPath2")
        self.labelPath1 = QtWidgets.QLabel(self.centralwidget)
        self.labelPath1.setGeometry(QtCore.QRect(5, 30, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.labelPath1.setFont(font)
        self.labelPath1.setText("")
        self.labelPath1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelPath1.setObjectName("labelPath1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOperations = QtWidgets.QMenu(self.menubar)
        self.menuOperations.setObjectName("menuOperations")
        self.menuLogical_Operations = QtWidgets.QMenu(self.menubar)
        self.menuLogical_Operations.setObjectName("menuLogical_Operations")
        self.menuOthers = QtWidgets.QMenu(self.menubar)
        self.menuOthers.setObjectName("menuOthers")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInput_Gambar_1 = QtWidgets.QAction(MainWindow)
        self.actionInput_Gambar_1.setObjectName("actionInput_Gambar_1")
        self.actionInput_Image_2 = QtWidgets.QAction(MainWindow)
        self.actionInput_Image_2.setObjectName("actionInput_Image_2")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/icons8-open-file-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionBack = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/icons8-exit-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBack.setIcon(icon1)
        self.actionBack.setObjectName("actionBack")
        self.actionSummations = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/icons8-plus-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSummations.setIcon(icon2)
        self.actionSummations.setObjectName("actionSummations")
        self.actionSubstraction = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/icons8-minus-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSubstraction.setIcon(icon3)
        self.actionSubstraction.setObjectName("actionSubstraction")
        self.actionMultiplication_x = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/icons8-multiply-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMultiplication_x.setIcon(icon4)
        self.actionMultiplication_x.setObjectName("actionMultiplication_x")
        self.actionDistribution = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/icons8-divide-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDistribution.setIcon(icon5)
        self.actionDistribution.setObjectName("actionDistribution")
        self.actionAND = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/andLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAND.setIcon(icon6)
        self.actionAND.setObjectName("actionAND")
        self.actionOR = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/orLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOR.setIcon(icon7)
        self.actionOR.setObjectName("actionOR")
        self.actionXOR = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/xorLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionXOR.setIcon(icon8)
        self.actionXOR.setObjectName("actionXOR")
        self.actionNOT = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/notLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNOT.setIcon(icon9)
        self.actionNOT.setObjectName("actionNOT")
        self.actionNAND = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icons/NAND.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNAND.setIcon(icon10)
        self.actionNAND.setObjectName("actionNAND")
        self.actionNOR = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Icons/NOR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNOR.setIcon(icon11)
        self.actionNOR.setObjectName("actionNOR")
        self.actionXNOR = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("Icons/XNOR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionXNOR.setIcon(icon12)
        self.actionXNOR.setObjectName("actionXNOR")
        self.actionImage_Blending = QtWidgets.QAction(MainWindow)
        self.actionImage_Blending.setObjectName("actionImage_Blending")
        self.actionImage_Matching = QtWidgets.QAction(MainWindow)
        self.actionImage_Matching.setObjectName("actionImage_Matching")
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionBack)
        self.menuOperations.addAction(self.actionSummations)
        self.menuOperations.addAction(self.actionSubstraction)
        self.menuOperations.addAction(self.actionMultiplication_x)
        self.menuOperations.addAction(self.actionDistribution)
        self.menuLogical_Operations.addAction(self.actionNOT)
        self.menuLogical_Operations.addAction(self.actionAND)
        self.menuLogical_Operations.addAction(self.actionNAND)
        self.menuLogical_Operations.addAction(self.actionOR)
        self.menuLogical_Operations.addAction(self.actionNOR)
        self.menuLogical_Operations.addAction(self.actionXOR)
        self.menuLogical_Operations.addAction(self.actionXNOR)
        self.menuLogical_Operations.addSeparator()
        self.menuOthers.addAction(self.actionImage_Blending)
        self.menuOthers.addAction(self.actionImage_Matching)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOperations.menuAction())
        self.menubar.addAction(self.menuLogical_Operations.menuAction())
        self.menubar.addAction(self.menuOthers.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aritmatical by Maulana Akbar Firdausya"))
        self.label.setText(_translate("MainWindow", "Gambar Masukan 1"))
        self.label_2.setText(_translate("MainWindow", "Gambar Masukan 2"))
        self.label_3.setText(_translate("MainWindow", "Keluaran Gambar"))
        self.buttonImport1.setText(_translate("MainWindow", "Impor"))
        self.buttonImport2.setText(_translate("MainWindow", "Impor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOperations.setTitle(_translate("MainWindow", "Aritmatical Operations"))
        self.menuLogical_Operations.setTitle(_translate("MainWindow", "Logical Operations"))
        self.menuOthers.setTitle(_translate("MainWindow", "Others"))
        self.actionInput_Gambar_1.setText(_translate("MainWindow", "Input Image 1"))
        self.actionInput_Image_2.setText(_translate("MainWindow", "Input Image 2"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionBack.setText(_translate("MainWindow", "Exit and Back"))
        self.actionSummations.setText(_translate("MainWindow", "Summation (+)"))
        self.actionSubstraction.setText(_translate("MainWindow", "Substraction (-)"))
        self.actionMultiplication_x.setText(_translate("MainWindow", "Multiplication (*)"))
        self.actionDistribution.setText(_translate("MainWindow", "Distribution (/)"))
        self.actionAND.setText(_translate("MainWindow", "AND"))
        self.actionOR.setText(_translate("MainWindow", "OR"))
        self.actionXOR.setText(_translate("MainWindow", "XOR"))
        self.actionNOT.setText(_translate("MainWindow", "NOT"))
        self.actionNAND.setText(_translate("MainWindow", "NAND"))
        self.actionNOR.setText(_translate("MainWindow", "NOR"))
        self.actionXNOR.setText(_translate("MainWindow", "XNOR"))
        self.actionImage_Blending.setText(_translate("MainWindow", "Image Blending"))
        self.actionImage_Matching.setText(_translate("MainWindow", "Image Matching"))

        # ---
        # ---
        # PENDEFINISIAN OBJEK dan PENGATURAN TAMPILAN-----------------------------------------------------------------------------------------
        # mengosongkan data input dan output pixmap serta mengosongkan data String
        self.pixmap1 = None
        self.pixmap2 = None
        self.pixmap3 = None
        self.pixmap4 = None
        self.pixmap5 = None
        self.input_pixmap1 = None
        self.stringefek = None
        self.timer = QTimer()
        self.timerEfek = QTimer()

        self.actionSave_As.triggered.connect(self.save_image)
        self.actionBack.triggered.connect(self.exitApplication)
        self.actionSummations.triggered.connect(self.penjumlahan_operation)
        self.actionSubstraction.triggered.connect(self.pengurangan_operation)
        self.actionMultiplication_x.triggered.connect(self.perkalian_operation)
        self.actionDistribution.triggered.connect(self.pembagian_operation)
        self.actionAND.triggered.connect(self.and_operation) 
        self.actionOR.triggered.connect(self.or_operation)
        self.actionXOR.triggered.connect(self.xor_operation)
        self.actionNOT.triggered.connect(self.not_operation)
        self.actionNOR.triggered.connect(self.nor_operation)
        self.actionNAND.triggered.connect(self.nand_operation)
        self.actionXNOR.triggered.connect(self.xnor_operation)

        self.actionImage_Blending.triggered.connect(self.blend_images)
        self.actionImage_Matching.triggered.connect(self.match_images)

        self.buttonImport1.clicked.connect(self.open_pixmap1)
        self.buttonImport2.clicked.connect(self.open_pixmap2)

        # ---
        # ---
        # FUNGSI MENU FILE -----------------------------------------------------------------------------------------
        # 1) FUNGSI OPEN IMAGE 1
    def open_pixmap1(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        
        image_path, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", 
                                                    "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)", options=options)
        
        if image_path:
            self.pixmap1 = QtGui.QPixmap(image_path)
            self.pbInput1.setPixmap(self.pixmap1)
            self.pbInput1.setScaledContents(True)
            self.labelPath1.setText(image_path)
            self.stringefek = None
            self.input_pixmap1 = None
            self.labelOutput.setText(None)

        # 1) FUNGSI OPEN IMAGE 1
    def open_pixmap2(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        
        image_path, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", 
                                                    "Image Files (*.png *.jpg *.bmp *.gif *.jpeg);;All Files (*)", options=options)
        
        if image_path:
            self.pixmap2 = QtGui.QPixmap(image_path)
            self.pbInput2.setPixmap(self.pixmap2)
            self.pbInput2.setScaledContents(True)
            self.labelPath2.setText(image_path)
            self.stringefek = None
            self.input_pixmap1 = None
            self.labelOutput.setText(None)

            # 3) FUNGSI EXIT
    def exitApplication(self):
        MainWindow.close()

        # 1) FUNGSI SAVE AS
    def save_image(self):
        if hasattr(self, 'gambars'):
            # Inisialisasi opsi untuk dialog pemilihan berkas
            options = QFileDialog.Options()
            # Menambahkan opsi mode baca saja ke dalam opsi dialog
            options |= QFileDialog.ReadOnly 
            # menampung file path dari dialog open file dan difilter hanya format png , jpg , bmp
            file_name, _ = QFileDialog.getSaveFileName(None, "Save Image File", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
            # check apakah terdapat path file
            if file_name:
                #Simpan gambar yang telah diformat
                self.gambars.save(file_name)

        # ---
        # ---
        # FUNGSI MENU ARITMATICAL OPERATION -----------------------------------------------------------------------------------------
        # 1) SUMMATION
    def penjumlahan_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_plus = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixelColor(x, y))
                    color2 = QtGui.QColor(image2.pixelColor(x, y))

                    r_result = min(color1.red() + color2.red(), 255)
                    g_result = min(color1.green() + color2.green(), 255)
                    b_result = min(color1.blue() + color2.blue(), 255)

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_plus.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_plus)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.gambars = result_plus
            self.stringefek = "Operasi : Penjumlahan "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()

        else: self.showWarning()

                    
        # 2) SUBSTRACTION
    def pengurangan_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_min = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixelColor(x, y))
                    color2 = QtGui.QColor(image2.pixelColor(x, y))

                    r_result = max(color1.red() - color2.red(), 0)  # Batasan nilai minimum
                    g_result = max(color1.green() - color2.green(), 0)  # Batasan nilai minimum
                    b_result = max(color1.blue() - color2.blue(), 0)  # Batasan nilai minimum

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_min.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_min)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.gambars = result_min
            self.stringefek = "Operasi : Pengurangan "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()
        
        else: self.showWarning

        # 3) MULTIPLICATION
    def perkalian_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_kali = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixelColor(x, y))
                    color2 = QtGui.QColor(image2.pixelColor(x, y))

                    r_result = min(color1.red() * color2.red(), 255)  # Batasan nilai maksimum
                    g_result = min(color1.green() * color2.green(), 255)  # Batasan nilai maksimum
                    b_result = min(color1.blue() * color2.blue(), 255)  # Batasan nilai maksimum

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_kali.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_kali)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.gambars = result_kali
            self.stringefek = "Operasi : Perkalian "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()
            
        else: self.showWarning()

        # 4) DISTRIBUTION   
    def pembagian_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_bagi = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixelColor(x, y))
                    color2 = QtGui.QColor(image2.pixelColor(x, y))

                    # Hindari pembagian oleh nol atau nilai yang sangat kecil
                    divisorRed = max(color2.red(), 1)
                    divisorgreen = max(color2.green(),1)
                    divisorBlue = max(color2.blue(),1)
                    
                    r_result = max(round(color1.red() / divisorRed), 0)  # Batasan nilai maksimum
                    g_result = max(round(color1.green() / divisorgreen), 0)  # Batasan nilai maksimum
                    b_result = max(round(color1.blue() / divisorBlue), 0)  # Batasan nilai maksimum

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_bagi.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_bagi)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.gambars = result_bagi
            self.stringefek = "Operasi : Pembagian "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()
        
        else: self.showWarning
        
        # ---
        # ---
        # FUNGSI MENU LOGICAL / GATES OPERATION -----------------------------------------------------------------------------------------
        # 1) AND
    def and_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_and = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixelColor(x, y))
                    color2 = QtGui.QColor(image2.pixelColor(x, y))
                        
                    r_result = color1.red() & color2.red()
                    g_result = color1.green() & color2.green()
                    b_result = color1.blue() & color2.blue()

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_and.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_and)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.gambars = result_and
            self.stringefek = "Operasi : AND "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()
            
        else: self.showWarning
        
        # 2) OR
    def or_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_orop = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixelColor(x, y))
                    color2 = QtGui.QColor(image2.pixelColor(x, y))

                    r_result = color1.red() | color2.red()
                    g_result = color1.green() | color2.green()
                    b_result = color1.blue() | color2.blue()

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_orop.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_orop)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.gambars = result_orop
            self.stringefek = "Operasi : OR "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()
            
        else: self.showWarning
        
        # 3) XOR
    def xor_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_xor = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixel(x, y))
                    color2 = QtGui.QColor(image2.pixel(x, y))

                    r_result = color1.red() ^ color2.red()
                    g_result = color1.green() ^ color2.green()
                    b_result = color1.blue() ^ color2.blue()

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_xor.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_xor)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.stringefek = "Operasi : XOR "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()

        else:
            self.showWarning()

        # 4) NOT
    def not_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_notop = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixelColor(x, y))
                    color2 = QtGui.QColor(image2.pixelColor(x, y))

                    r_result = 255 - color2.red()
                    g_result = 255 - color2.green()
                    b_result = 255 - color2.blue()

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_notop.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_notop)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.gambars = result_notop
            self.stringefek = "Operasi : NOT "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()

        else: self.showWarning

    def nor_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_nor = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixel(x, y))
                    color2 = QtGui.QColor(image2.pixel(x, y))

                    r_result = 255 if (color1.red() == 0 and color2.red() == 0) else 0
                    g_result = 255 if (color1.green() == 0 and color2.green() == 0) else 0
                    b_result = 255 if (color1.blue() == 0 and color2.blue() == 0) else 0

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_nor.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_nor)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.stringefek = "Operasi : NOR "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()

        else: self.showWarning()

    def nand_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_nand = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixel(x, y))
                    color2 = QtGui.QColor(image2.pixel(x, y))

                    r_result = 255 if (color1.red() != 255 or color2.red() != 255) else 0
                    g_result = 255 if (color1.green() != 255 or color2.green() != 255) else 0
                    b_result = 255 if (color1.blue() != 255 or color2.blue() != 255) else 0

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_nand.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_nand)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.stringefek = "Operasi : NAND "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()

        else: self.showWarning()

    def xnor_operation(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            result_xnor = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixel(x, y))
                    color2 = QtGui.QColor(image2.pixel(x, y))

                    r_result = 255 if (color1.red() == color2.red()) else 0
                    g_result = 255 if (color1.green() == color2.green()) else 0
                    b_result = 255 if (color1.blue() == color2.blue()) else 0

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    result_xnor.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_xnor)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.stringefek = "Operasi : XNOR "
            self.labelOutput.setText(self.stringefek)
            self.showEffectComplete()

        else:
            self.showWarning()

    def blend_images(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            width = min(self.pixmap1.width(), self.pixmap2.width())
            height = min(self.pixmap1.height(), self.pixmap2.height())
            blended_image = QImage(width, height, QImage.Format_RGB888)

            image1 = self.pixmap1.toImage()
            image2 = self.pixmap2.toImage()

            for x in range(width):
                for y in range(height):
                    color1 = QtGui.QColor(image1.pixel(x, y))
                    color2 = QtGui.QColor(image2.pixel(x, y))

                    r_result = int((1 - self.blend_factor) * color1.red() + self.blend_factor * color2.red())
                    g_result = int((1 - self.blend_factor) * color1.green() + self.blend_factor * color2.green())
                    b_result = int((1 - self.blend_factor) * color1.blue() + self.blend_factor * color2.blue())

                    result_pixel = QtGui.qRgb(r_result, g_result, b_result)
                    blended_image.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(blended_image)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.showEffectComplete()

        else:
            self.showWarning()

    def match_images(self):
        if self.pixmap1 is not None and self.pixmap2 is not None:
            main_width = self.pixmap1.width()
            main_height = self.pixmap1.height()
            template_width = self.pixmap2.width()
            template_height = self.pixmap2.height()

            result_image = QImage(main_width, main_height, QImage.Format_RGB888)

            pixmap1 = self.pixmap1.toImage()
            pixmap2 = self.pixmap2.toImage()

            # Loop melalui citra utama untuk mencocokkan citra template
            for x in range(main_width - template_width + 1):
                for y in range(main_height - template_height + 1):
                    match_score = self.calculate_match_score(pixmap1, pixmap2, x, y)
                    result_pixel = QtGui.qRgb(match_score, match_score, match_score)
                    result_image.setPixel(x, y, result_pixel)

            result_pixmap = QPixmap.fromImage(result_image)
            self.pbOutput.setPixmap(result_pixmap)
            self.pbOutput.setScaledContents(True)
            self.showEffectComplete()

        else:
            self.showWarning()

    def calculate_match_score(self, pixmap1, pixmap2, x, y):
        score = 0

        template_width = pixmap2.width()
        template_height = pixmap2.height()

        for i in range(template_width):
            for j in range(template_height):
                main_pixel = QtGui.QColor(pixmap1.pixel(x + i, y + j))
                template_pixel = QtGui.QColor(pixmap2.pixel(i, j))

                # Hitung perbedaan antara piksel citra utama dan piksel citra template
                score += abs(main_pixel.red() - template_pixel.red())
                score += abs(main_pixel.green() - template_pixel.green())
                score += abs(main_pixel.blue() - template_pixel.blue())

        return score
    
    def showWarning(self):
        self.labelWarning.setText("Tidak ada efek yang diterapkan pada Gambar Keluaran")
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.clearWarning)
        self.timer.start()


    def showEffectComplete(self):
        self.labelLoading.setText("<b>Efek berhasil diterapkan</b>")
        self.timerEfek.setInterval(3000)
        self.timerEfek.timeout.connect(self.clearLoading)
        self.timerEfek.start()

    def clearWarning(self):
        self.labelWarning.clear()
        self.timer.stop()

    def clearLoading(self):
        self.labelLoading.clear()
        self.timerEfek.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindows()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
