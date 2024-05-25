from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(300, 500)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 500))
        self.frame.setStyleSheet("QFrame{    \n"
"    background-color:rgb(18,65,129);\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")


        self.choose_file_bt = QtWidgets.QPushButton(self.frame)
        self.choose_file_bt.setGeometry(QtCore.QRect(90, 400, 120, 23))
        self.choose_file_bt.setStyleSheet("QPushButton{\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255,255,255);\n"
"}")
        self.choose_file_bt.setFlat(False)
        self.choose_file_bt.setObjectName("choose_file_bt")


        self.emblem_label = QtWidgets.QLabel(self.frame)
        self.emblem_label.setGeometry(QtCore.QRect(85, 10, 130, 100))
        self.emblem_label.setText("")
        self.emblem_label.setPixmap(QtGui.QPixmap("design/emblem_of_MIA.png"))
        self.emblem_label.setObjectName("emblem_label")


        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(60, 220, 171, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color:rgb(124, 113, 116);\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 196, 209, 255), stop:1 rgba(0, 0, 255, 210));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")


        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 280, 180, 30))


        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(True)
        font.setWeight(75)


        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: white;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Транскрибация аудио УБК"))
        self.choose_file_bt.setText(_translate("MainWindow", "Выбор аудиозаписи"))
