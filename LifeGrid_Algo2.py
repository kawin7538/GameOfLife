# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:02:08 2019

@author: Kawin-PC
"""

import numpy as np

class LifeGrid:
    
    def __init__(self,rows,cols):
        #initial nrow and ncol
        self._rows=rows
        self._cols=cols
        
        self._liveDict=dict()
        
        #set all element in grid as DEAD CELL
        self.configure(list())
        
    #method that return nrow and ncol
    def numRows(self):
        return self._rows
    def numCols(self):
        return self._cols
    
    #configure status of cell from live cell in coordList
    def configure(self,coordList):
        #set status of all cell to dead
        self._liveDict.clear()
        #set status of specific cell as LIVE CELL
        for coord in coordList:
            self.setCell(coord[0],coord[1])
        
    #method that check whether it's live cell
    def isLiveCell(self,row,col):
        return (row,col) in self._liveDict.keys()
    
    #method that clear that cell to DEAD CELL
    def clearCell(self,row,col):
        try:
            del self._liveDict[(row,col)]
        except:
            return ;
        
    #method that set that cell to LIVE CELL
    def setCell(self,row,col):
        self._liveDict[(row,col)]=1
        
    #method that check live cell around it
    def numLiveNeighbors(self,row,col):
        #this line is same as
        #   ans=0
        #   for i in range(max(0,row-1),min(row+1,self.numRows()-1)+1):
        #       for j in range(max(0,col-1),min(col+1,self.numCols()-1)+1):
        #           if self.isLiveCell(i,j):
        #               ans+=1
        #why must use range(max(0,row-1),min(row+1,self.numRows()-1)+1)?
        #   ans -> in normal state will check as
        #           i-1 i i+1
        #           ?   ?   ?
        #           ?   *   ?
        #           ?   ?   ?
        #           if row want to find is 0
        #           -1  0 +1
        #            ?  ?  ?
        #            ?  *  ?
        #            ?  ?  ?
        #           so should start from 0
        #           if row want to find is nrow-1
        #           nrow-2  nrow-1  norw
        #           ?       ?       ?
        #           ?       *       ?
        #           ?       ?       ?
        #           so shouhld end at nrow-1
        #       col is same as row
        ans = sum([1 for j in range(max(0,col-1),min(col+1,self.numCols()-1)+1) \
                for i in range(max(0,row-1),min(row+1,self.numRows()-1)+1) if \
                self.isLiveCell(i,j)])
        #return ans-1 if itself is LIVE CELL else return ans
        return (ans-1 if self.isLiveCell(row,col) else ans)
        
    
# this part will run if this file is main file
if __name__ == "__main__":
    a=LifeGrid(5,5)
    a.configure([(0,0),(1,1),(2,0)])
    print(a._liveDict)
    print(a.numLiveNeighbors(1,0))
    
    