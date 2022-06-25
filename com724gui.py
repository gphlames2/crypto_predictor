# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'com724gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(439, 270, 521, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.listView = QtWidgets.QListView(self.horizontalFrame)
        self.listView.setGeometry(QtCore.QRect(385, 0, 141, 301))
        self.listView.setMaximumSize(QtCore.QSize(141, 301))
        self.listView.setObjectName("listView")
        self.widget = QtWidgets.QWidget(self.horizontalFrame)
        self.widget.setGeometry(QtCore.QRect(0, -1, 381, 301))
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(440, 181, 521, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.check_editor = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.check_editor.setObjectName("check_editor")
        self.horizontalLayout_3.addWidget(self.check_editor)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.check_editor.setText(_translate("MainWindow", "Check"))
    def populate_gui(self):
        self.comboBox.addItems(['24h','7d'])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

