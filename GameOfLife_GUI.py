# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:01:40 2019

@author: Kawin-PC
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidgetItem
from main_GUI import Ui_MainWindow
from GameOfLife import evolve
from LifeGrid import LifeGrid

class MyApp(QMainWindow):
    def __init__(self,grid , parent=None):
        QWidget.__init__(self, parent)
        self._grid=grid
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_start()
        
    def init_start(self):
        for i in range(5):
            for j in range(5):
                self.tableWidget.setItem(i,j,self.change(i,j))
    
    def change(self,i,j):
        return QTableWidgetItem(str(int(self._grid[i][j])))
                            
if __name__ == '__main__':
    INIT_CONFIG=[(0,0),(1,1),(2,2),(3,3),(0,2)]
    grid=LifeGrid(5,5)
    grid.configure(INIT_CONFIG)
    app = QApplication(sys.argv)
    myapp = MyApp(grid)
    myapp.show()
    sys.exit(app.exec_())