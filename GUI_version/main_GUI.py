# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


#this file is create from 

#all functions from PyQt5 is only GUI part , let it be
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
#import numpy and rename it to np
import numpy as np
#import library name sys
import sys
#import class LifeGrid from LifeGrid_Algo2
from LifeGrid_Algo2 import LifeGrid
#import function name evolve_v2 from evolve_func
from evolve_func import evolve_v2

#class Ui_MainWindow that created from QtDesigner (only __init__ and nextclick is written later)
class Ui_MainWindow(object):
    #initial function in class
    def __init__(self,HEIGHT,WIDTH,init=[]):
        #create LifeGrid
        self._grid=LifeGrid(HEIGHT,WIDTH)
        #configure grid
        self._grid.configure(init)
        #set height and width
        self._height=HEIGHT
        self._width=WIDTH
    
    #this function is almost pure-gui phase, look at clicked.connect only
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
        
        #set function nextclick activate when click it , to be continue in nextclick()
        self.pushButton.clicked.connect(self.nextclick)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #set color in table , set red if live , and white when died
        for i in range(5):
            for j in range(5):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem())
                if self._grid.isLiveCell(i,j):
                    self.tableWidget.item(i,j).setBackground(QColor(255,0,0))
                else:
                    self.tableWidget.item(i,j).setBackground(QColor(255,255,255))

    #this is only change name of element of GUI , let it be.
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GameOfLife"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "MainPage"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Performance"))
        self.pushButton.setText(_translate("MainWindow", "NEXT"))
       
    #the most important in this file, function that change with condition of game
    def nextclick(self):
        evolve_v2(self._grid)
        #set color in table , set red if live , and white when died
        for i in range(5):
            for j in range(5):
                if self._grid.isLiveCell(i,j):
                    self.tableWidget.item(i,j).setBackground(QColor(255,0,0))
                else:
                    self.tableWidget.item(i,j).setBackground(QColor(255,255,255))     
                    

if __name__ == "__main__":
    #create random live cell at rate 70%
    INIT_CONFIG=[(np.random.randint(0,5),np.random.randint(0,5)) for j in range(int(5*5*0.7))]
    #create new application
    app = QtWidgets.QApplication(sys.argv)
    #create new main window
    MainWindow = QtWidgets.QMainWindow()
    #initial ui as new GUI with 5*5 cells
    ui = Ui_MainWindow(5,5,INIT_CONFIG)
    #link ui to MainWindow
    ui.setupUi(MainWindow)
    #show main window
    MainWindow.show()
    #pause code until app is finished
    sys.exit(app.exec_())

