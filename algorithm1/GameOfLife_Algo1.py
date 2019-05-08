# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:36:58 2019

@author: Kawin-PC
"""

#import LifeGrid class from LifeGrid file
from LifeGrid_Algo1 import LifeGrid
#import numpy to random integer
import numpy as np

#initialize start live cell as tuple
INIT_CONFIG=[(np.random.randint(0,4),np.random.randint(0,4)) for i in range(int(4*4*0.7))]

#initialize width and height of game ( can change to input later )
GRID_WIDTH=4
GRID_HEIGHT=4

#initialize generation of game ( can change to input later )
NUM_GEN=5

#function that evolve grid for one turn
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
    
#function that draw grid
def draw(grid):
    #initial string as "Generation"
    s="Generation\n"
    #loop iteration until i and j
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            #add string of value to main string
            s+=' '+str(grid[i][j])
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