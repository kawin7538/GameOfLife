# -*- coding: utf-8 -*-
"""
Created on Sat May  4 15:57:55 2019

@author: Kawin-PC
"""

def evolve(grid):
    #initialize liveCells as empty list
    liveCells=list()
    #access every cells in grid
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            #count neighbors that is LIVE CELL around (i,j)
            neighbors=grid.numLiveNeighbors(i,j)
            #if neighbors is 2 and (i,j) has live or neighbors is 3
            if (neighbors==2 and grid.isLiveCell(i,j)) or neighbors==3:
                #this cell will live in next turn
                liveCells.append((i,j))
    #configure grid with new live Cell
    grid.configure(liveCells)
    
def evolve_v2(grid):
    #initialize liveCells as empty set
    liveCells=set()
    #initial unknown cell as empty set
    unknownCells=set()
    #iteration in every item in liveDict
    for key,_ in grid._liveDict.items():
        #add all dead cell around this live cell to unknownCells
        unknownCells.update([(i,j) for j in range(max(0,key[1]-1),min(key[1]+1\
                              ,grid.numCols()-1)+1) for i in range(max(0,key[0]\
                                           -1),min(key[0]+1,grid.numRows()-1)+1) if not grid.isLiveCell(i,j)])
        #find number of neighbors around this cell
        neighbors=grid.numLiveNeighbors(key[0],key[1])
        #check neighbors from condition , if true then add to liveCells
        if (neighbors==2 and grid.isLiveCell(key[0],key[1])) or neighbors==3:
            liveCells.add(key)
    #iteration in every unknownCells
    for i,j in unknownCells:
        #find neighbors of this cell
        neighbors=grid.numLiveNeighbors(i,j)
        #check condition with neighbors , if true then add to liveCells
        if (neighbors==2 and grid.isLiveCell(i,j)) or neighbors==3:
            liveCells.add((i,j))
    #configure grid with liveCells
    grid.configure(list(liveCells))