#!/bin/python
import sys
grid = []
for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)
max=0  
for i in range(17):
    for j in range(17):
        mult=1
        for k in range(4):
            mult*=grid[i+k][j+k]
            if mult>max:
                max=mult          
for i in range(17):
    for j in range(20):
        mult=1
        for k in range(4):
            mult*=grid[i+k][j]
            if mult>max:
                max=mult
for i in range(20):
    for j in range(17):
        mult=1
        for k in range(4):
            mult*=grid[i][j+k]
            if mult>max:
                max=mult
for i in range(17):
    for j in range(3,20):
        mult=1
        for k in range(4):
            mult*=grid[i+k][j-k]
            if mult>max:
                max=mult                          
print max            
