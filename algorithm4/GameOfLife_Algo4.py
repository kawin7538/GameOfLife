# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:40:17 2019

@author: Kawin-PC
"""

#https://www.r-bloggers.com/fast-conways-game-of-life-in-r/

from LifeGrid_Algo4 import LifeGrid
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
    #shift to bottom
    grid1=np.append(np.zeros([1,grid.numCols()]),grid[:grid.numRows()-1],axis=0)
    #shift to above
    grid2=np.append(grid[1:],np.zeros([1,grid.numCols()]),axis=0)
    #shift to left
    grid3=np.append(grid[:,1:],np.zeros([grid.numRows(),1]),axis=-1)
    #shift to right
    grid4=np.append(np.zeros([grid.numRows(),1]),grid[:,:grid.numCols()-1],axis=-1)
    #shift to bottom and left
    grid5=np.append(grid1[:,1:],np.zeros([grid.numRows(),1]),axis=-1)
    #shift to bottom and right
    grid6=np.append(np.zeros([grid.numRows(),1]),grid1[:,:grid.numCols()-1],axis=-1)
    #shift to above and left
    grid7=np.append(grid2[:,1:],np.zeros([grid.numRows(),1]),axis=-1)
    #shift to above and right
    grid8=np.append(np.zeros([grid.numRows(),1]),grid2[:,:grid.numCols()-1],axis=-1)
    #sum of all 8 girds
    temp_grid=grid1+grid2+grid3+grid4+grid5+grid6+grid7+grid8
    
    grid_new=grid._grid
    grid_new[(grid._grid==0) & (temp_grid==3)]=1
    grid_new[(grid._grid==1) & (temp_grid<2)]=0
    grid_new[(grid._grid==1) & (temp_grid>3)]=0
    grid._grid=grid_new
    
#function that draw grid
def draw(grid):
    #initial string as "Generation"
    s="Generation\n"
    #loop iteration until i and j
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            #add string of value to main string
            s+=' '+str(int(grid._grid[i,j]))
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