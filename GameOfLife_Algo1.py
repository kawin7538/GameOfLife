# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:36:58 2019

@author: Kawin-PC
"""

#import LifeGrid class from LifeGrid file
from LifeGrid_Test1 import LifeGrid
from time import time
import seaborn as sns;sns.set()
import numpy as np
import matplotlib.pyplot as plt

#initialize start live cell as tuple
INIT_CONFIG=[]

#initialize width and height of game ( can change to input later )
GRID_WIDTH=4
GRID_HEIGHT=4

#initialize generation of game ( can change to input later )
NUM_GEN=100

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
    
#run the following lines if this is main file only
if __name__=="__main__":
    n=[10,100,1000]
    ans=[]
    for i in n:
        print("FOR",i,"CELLS , 10%")
        INIT_CONFIG=[(np.random.randint(0,i),np.random.randint(0,i)) for j in range(int(i*i*0.1))]
        #initialize grid with HEIGHT AND WIDTH
        grid=LifeGrid(i,i)
        #configure grid with initial live cell
        grid.configure(INIT_CONFIG)
        #draw grid before evolve
        #draw(grid)
        start=time()
        #describe how to do in each gen
        for i in range(NUM_GEN):
            #evolve grid
            evolve(grid)
            #draw grid
            #draw(grid)
            print(f"GEN:{i}")
        endd=time()
        ans.append(endd-start)
        print(endd-start,"Second")
    sns_plot=sns.scatterplot(n,ans)
    sns_plot.figure.savefig("10percent"+".png")