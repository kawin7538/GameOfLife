# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:38:24 2019

@author: Kawin-PC
"""

#import library name numpy and rename it to np
import numpy as np

class LifeGrid:
    
    DEAD_CELL=0
    LIVE_CELL=0
    
    def __init__(self,rows,cols):
        #initial nrow and ncol
        self._rows=rows
        self._cols=cols
        #initial grid rows*cols
        self._grid=np.zeros([rows,cols])
        
    #method that return nrow and ncol
    def numRows(self):
        return self._rows
    def numCols(self):
        return self._cols
    
    #configure status of cell from live cell in coordList
    def configure(self,coordList):
        #set all elements in grid as 0
        self._grid=np.zeros([self.numRows(),self.numCols()])
        #set status of specific cell as LIVE CELL
        for coord in coordList:
            self.setCell(coord[0],coord[1])
            self[coord[0]][coord[1]]=1
        
    #method that check whether it's live cell
    def isLiveCell(self,row,col):
        return self[row][col]==1
    
    #method that clear that cell to DEAD CELL
    def clearCell(self,row,col):
        #set value of that cell as 0
        self._grid[row][col]=0
        
    #method that set that cell to LIVE CELL
    def setCell(self,row,col):
        self._grid[row][col]=1
        
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
    
    #function that abbreviate self._grid[row][col] to self[row][col]
    def __getitem__(self,row):
        return self._grid[row]
        
    
# this part will run if this file is main file
# end of description this file
if __name__ == "__main__":
    a=LifeGrid(5,5)
    a.configure([(0,0),(1,1),(2,0)])
    print(a.numLiveNeighbors(1,0))
    print(a[2],a[1][1])
    print(type(a._grid))