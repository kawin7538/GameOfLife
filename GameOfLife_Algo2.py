# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:02:54 2019

@author: Kawin-PC
"""

#import LifeGrid class from LifeGrid file
from LifeGrid_Algo2 import LifeGrid
from time import time
import seaborn as sns;sns.set()
import numpy as np
import matplotlib.pyplot as plt

#initialize generation of game ( can change to input later )
NUM_GEN=10

#function that evolve grid for one turn
def evolve(grid):
    #initialize liveCells as empty list
    liveCells=set()
    unknownCells=set()
    for _,key in enumerate(grid._liveDict):
        unknownCells.update([(i,j) for j in range(max(0,key[1]-1),min(key[1]+1\
                              ,grid.numCols()-1)+1) for i in range(max(0,key[0]\
                                           -1),min(key[0]+1,grid.numRows()-1)+1) if not grid.isLiveCell(i,j)])
        neighbors=grid.numLiveNeighbors(key[0],key[1])
        if (neighbors==2 and grid.isLiveCell(key[0],key[1])) or neighbors==3:
            liveCells.add((key[0],key[1]))
    for i,j in unknownCells:
        neighbors=grid.numLiveNeighbors(i,j)
        if (neighbors==2 and grid.isLiveCell(i,j)) or neighbors==3:
            liveCells.add((i,j))
    grid.configure(list(liveCells))
    
#run the following lines if this is main file only
if __name__=="__main__":
    n=[10,100,1000,10000,100000]
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
            print(f"Start GEN:{i}")
            #evolve grid
            evolve(grid)
            #draw grid
            #draw(grid)
            print(f"End GEN:{i}")
        endd=time()
        ans.append(endd-start)
        print(endd-start,"Second")
    sns_plot=sns.lineplot(n,ans)
    sns_plot.figure.savefig("Algo2_10percent"+".png")