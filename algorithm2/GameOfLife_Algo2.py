# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:02:54 2019

@author: Kawin-PC
"""

#import LifeGrid class from LifeGrid file
from LifeGrid_Algo2 import LifeGrid
#import numpy and rename it to np
import numpy as np

#initialize start live cell as tuple (random 70%)
INIT_CONFIG=[(np.random.randint(0,4),np.random.randint(0,4)) for i in range(int(4*4*0.7))]

#initialize width and height of game ( can change to input later )
GRID_WIDTH=4
GRID_HEIGHT=4

#initialize generation of game ( can change to input later )
NUM_GEN=5

#function that evolve grid for one turn
def evolve(grid):
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
    
#function that draw grid
def draw(grid):
    #initial string as "Generation"
    s="Generation\n"
    #loop iteration until i and j
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            #add string of value to main string
            s+=' '+str(int(grid[i][j]))
        s+='\n'
    #print main string
    print(s)
    
#run the following lines if this is main file only
if __name__=="__main__":
    #initialize grid with HEIGHT AND WIDTH
    grid=LifeGrid(GRID_HEIGHT,GRID_WIDTH)
    #configure grid with initial live cell
    grid.configure(INIT_CONFIG)
    #draw grid before evolve
    draw(grid)
    #describe how to do in each gen
    for i in range(NUM_GEN):
        #evolve grid
        evolve(grid)
        #draw grid
        draw(grid)