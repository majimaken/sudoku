# Sudoku Solver

## Instructions

1) Open sudoku_solve.py in Python IDE
2) Enter your Sudoku to solve in the following format

```python
board = [[2,0,0,3,0,0,0,0,0],
        [8,0,4,0,6,2,0,0,3],
        [0,1,3,8,0,0,2,0,0],
        [0,0,0,0,2,0,3,9,0],
        [5,0,7,0,0,0,6,2,1],
        [0,3,2,0,0,6,0,0,0],
        [0,2,0,0,0,9,1,4,0],
        [6,0,1,2,5,0,8,0,9],
        [0,0,0,0,0,1,0,0,2]]
```

3) Execute code and check prints (the first print is the original Sudoku and the second is the solved one)

## Methods

### Backtracking Algorithm
The most common algorithm for solving Sudoku puzzles is backtracking. This process detects the empty fields and gradually inserts digits that work at that time. After that, the algorithm goes to the next field and again inserts a number that works. If it runs into a dead end and inserting the possible options would violate the rules, the algorithm goes back one step and inserts another possible number in the last field. This continues until it reaches the last field.  

### Implementation 

The solver is divided into several functions. 

* solve() is the core and goes through the empty fields by calling the find_empty() function. It inserts values between 1-9 and tests the field with valid().

* print_board() makes sure that the Sudoku field (here as a list) is printed vividly.

* find_empty() returns the indices of the next empty field.

* valid() checks the three main rules: The numbers 1-9 may occur only once in each row, line and 3x3 square. 
