# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 08:44:05 2019

@author: Kawin-PC

Student Id : 61070505203
"""

import ctypes

class Array:
    def __init__(self,size,show_status=False):
        assert size>0,"Array size must be > 0"
        self._size=size
        PyArrayType=ctypes.py_object*size
        self._elements=PyArrayType()
        self.clear(None)
        if show_status:
            print("\n1D Array Initial")
    def __len__(self):
        return self._size
    def __getitem__(self,index):
        assert index>=0 and index<len(self),"INdex Out Of Range"
        return self._elements[index]
    def __setitem__(self,index,value):
        assert index>=0 and index<len(self),"Index Out Of Range"
        self._elements[index]=value
    def clear(self,value):
        for i in range(len(self)):
            self._elements[i]=value
    def __iter__(self):
        return _ArrayIterator(self._elements)
    
class _ArrayIterator:
    def __init__(self,array):
        self._arrayRef=array
        self._curNdx=0
    def __iter__(self):
        return self
    def __next__(self):
        if self._curNdx<len(self._arrayRef):
            entry=self._arrayRef[self._curNdx]
            self._curNdx+=1
            return entry
        else:
            raise StopIteration
            
class Array2D:
    def __init__(self,nrow,ncol,show_status=False):
        self._row=Array(nrow)
        for i in range(nrow):
            self._row[i]=Array(ncol)
        if show_status:
            print("\n2D Array Initial")
    def numRows(self):
        return len(self._row)
    def numCols(self):
        return len(self._row[0])
    def clear(self,value):
        for i in range(self.numRows()):
            self._row[i].clear(value)
    def __getitem__(self,ndxTuple):
        assert len(ndxTuple)==2,"Invalid number of array subscripts"
        row,col=ndxTuple[0],ndxTuple[1]
        assert row>=0 and row<self.numRows() and col>=0 and col<self.numCols(),\
        "Array subscript out of range"
        the1da=self._row[row]
        return the1da[col]
    def __setitem__(self,ndxTuple,value):
        assert len(ndxTuple)==2,"Invalid number of array subscripts"
        row,col=ndxTuple[0],ndxTuple[1]
        assert row>=0 and row<self.numRows() and col>=0 and col<self.numCols(),\
        "Array subscript out of range"
        the1da=self._row[row]
        the1da[col]=value
    
            
if __name__=="__main__":
    a=Array(5,True)
    for i in range(len(a)):
        a[i]=i
    for i in range(len(a)):
        print(a[i],end=" ")
        
    aa=Array2D(5,5,True)
    for i in range(aa.numRows()):
        for j in range(aa.numCols()):
            aa[i,j]=i+j
    for i in range(aa.numRows()):
        for j in range(aa.numCols()):
            print(aa[i,j],end=" ")
        print("\n")
    for i in a:
        print(i)
    