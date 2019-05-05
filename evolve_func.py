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