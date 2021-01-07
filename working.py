# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:53:25 2021

@author: kenge
"""

board = [[7,8,0,4,0,0,1,2,0],
         [6,0,0,0,7,5,0,0,9],
         [0,0,0,6,0,1,0,7,8],
         [0,0,7,0,4,0,2,6,0],
         [0,0,1,0,5,0,9,3,0],
         [9,0,4,0,6,0,0,0,5],
         [0,7,0,3,0,0,0,1,2],
         [1,2,0,0,0,7,4,0,0],
         [0,4,9,2,0,6,0,0,7]]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
            
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
                
            if j == 8:
                print(bo[i][j])
                
            else:
                print(str(bo[i][j]) + " ", end = "")
                
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) 
            
def valid(bo, num, pos):
    
    # Check row
    for i in range(len(bo[0])):
        # Check each element in row if it is the same
        # Make sure to ignore the position we just inserted
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Check collumn
    for i in range(len(bo)):
        # Check each element in column if it is the same
        # Make sure to ignore the position we just inserted
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check 3x3 boxes
    # We put indexes on the 3x3 boxes: 
    # (0,0), (0,1), (0,2)
    # (1,0), (1,1), (1,2)
    # (2,0), (2,1), (2,2)
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
  
    
            