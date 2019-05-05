# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 20:43:16 2019

@author: Kawin-PC
"""

#import LifeGrid class from LifeGrid file
from LifeGrid import LifeGrid

#initialize start live cell as tuple
INIT_CONFIG=[(0,0),(1,0),(2,0)]

#initialize width and height of game ( can change to input later )
GRID_WIDTH=4
GRID_HEIGHT=4

#initialize generation of game ( can change to input later )
NUM_GEN=3

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

#draw grid function ( can change to Tkinter or HTML Later )
def draw(grid):
    #access every cell in grid
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            #print this cell and end line with " " not "\n"
            print(grid[i][j],end=" ")
        #print empty line to show next row
        print()
    #print empty line to end grid show
    print()
    
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