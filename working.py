# Sudoku Solver
# Instead of using a method like naive bayes, we use a backtracking method. 
# The solver puts in a number for every "0" and continues putting numbers for the remaining "0".
# If it fails at one point, the solver goes back one step and tries another number. 

# Enter your sudoku in the following format.
# This board is from https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html in order to check result. 

board = [[2,0,0,3,0,0,0,0,0],
        [8,0,4,0,6,2,0,0,3],
        [0,1,3,8,0,0,2,0,0],
        [0,0,0,0,2,0,3,9,0],
        [5,0,7,0,0,0,6,2,1],
        [0,3,2,0,0,6,0,0,0],
        [0,2,0,0,0,9,1,4,0],
        [6,0,1,2,5,0,8,0,9],
        [0,0,0,0,0,1,0,0,2]]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            # Call solve() again with new board
            if solve(bo):
                return True

            # If solve() does not return True, we reset the value to 0
            bo[row][col] = 0

    return False

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
    return None
            
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
    # Using the pos (e.g. pos = (0,9)), we determine the index of the 3x3 boxes.
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    #Check if we have same number in 3x3 box.
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    
    return True


print_board(board)
solve(board)
print("_______________________\n")
print_board(board)



  
    
            