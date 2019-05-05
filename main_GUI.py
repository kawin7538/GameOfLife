# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
import numpy as np
import sys
from LifeGrid import LifeGrid
from evolve_func import evolve

class Ui_MainWindow(object):
    def __init__(self,HEIGHT,WIDTH,init=[]):
        self._grid=LifeGrid(HEIGHT,WIDTH)
        self._grid.configure(init)
        self._height=HEIGHT
        self._width=WIDTH
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 780, 580))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 740, 520))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setRowCount(self._height)
        self.tableWidget.setColumnCount(self._width)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tabWidget.addTab(self.tab, "")        
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 0, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.nextclick)
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        for i in range(5):
            for j in range(5):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem())
                if self._grid.isLiveCell(i,j):
                    self.tableWidget.item(i,j).setBackground(QColor(255,0,0))
                else:
                    self.tableWidget.item(i,j).setBackground(QColor(255,255,255))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GameOfLife"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "MainPage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Performance"))
        self.pushButton.setText(_translate("MainWindow", "NEXT"))
       
    def nextclick(self):
        evolve(self._grid)
        for i in range(5):
            for j in range(5):
                if self._grid.isLiveCell(i,j):
                    self.tableWidget.item(i,j).setBackground(QColor(255,0,0))
                else:
                    self.tableWidget.item(i,j).setBackground(QColor(255,255,255))


if __name__ == "__main__":
    INIT_CONFIG=[(np.random.randint(0,5),np.random.randint(0,5)) for j in range(int(5*5*0.7))]
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(5,5,INIT_CONFIG)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

