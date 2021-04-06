#The task is to generate a 9 x 9 valid Sudoku grid and find its solution
#A player can fill the grid following the below set of rules:
#1.In all rows there should be unique elements from 1-9
#2.In all columns there should be unique elements from 1-9
#3.In all 9 sub matrices(3×3 grids) the elements should be 1-9 without repetition.

import random    #random module to generate/choose random numbers between a range
import copy      #copy module for deep copy operations
print("")
print("Welcome to Sudoku :D")
print("")

#Making first a 9 x 9 empty Sudoku grid
grid = [['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_','_'],]

#function to find and return the sub matrix to which the element belongs
def findcell(m,n):
    if m < 3:
        if n < 3:
            c = 1
        elif 6 > n >= 3:
            c = 2
        elif 9 > n >= 6:
            c = 3
    elif 6 > m >= 3:
        if n < 3:
            c = 4
        elif 6 > n >= 3:
            c = 5
        elif 9 > n >= 6:
            c = 6
    elif 9 > m >= 6:
        if n < 3:
            c = 7
        elif 6 > n >= 3:
            c = 8
        elif 9 > n >= 6:
            c = 9
    return c

#function to store all elements in a list belonging to a particular submatrix
def getcelllist(x):
    cell = []
    if x == 1:
        for i in range(3):
            for j in range(3):
                cell.append(grid[i][j])
    elif x == 2:
        for i in range(3):
            for j in range(3, 6):
                cell.append(grid[i][j])
    elif x == 3:
        for i in range(3):
            for j in range(6, 9):
                cell.append(grid[i][j])
    elif x == 4:
        for i in range(3, 6):
            for j in range(3):
                cell.append(grid[i][j])
    elif x == 5:
        for i in range(3, 6):
            for j in range(3, 6):
                cell.append(grid[i][j])
    elif x == 6:
        for i in range(3, 6):
            for j in range(6, 9):
                cell.append(grid[i][j])
    elif x == 7:
        for i in range(6, 9):
            for j in range(3):
                cell.append(grid[i][j])
    elif x == 8:
        for i in range(6, 9):
            for j in range(3, 6):
                cell.append(grid[i][j])
    elif x == 9:
        for i in range(6, 9):
            for j in range(6, 9):
                cell.append(grid[i][j])

    return cell

#function to print the Generated Sudoku Puzzle
# "|" and "-" used to separate the sub matrices
# 'end=" "' appends space instead of newline
def printsudoku(grid):
    for i in range(9):
        for j in range(9):
            if j == 3 or j == 6 or j == 9:
                print("|",end=" ")        
            print(grid[i][j],end=" ")
        if i ==2 or i==5:
            print("\n---------------------",end=' ')
        print("")

#function to fill all elements of diagonal submatrices
#in the initial empty grid,diagonal sub matrices are independent of other empty sub matrices
#So by filling them first we need to do only box check        
# num.remove(x) is used so that a element is not repeated during filling
def filldiagonalsubgrids():
    start = 0
    stop = 3
    for i in range(3):
        num = [1,2,3,4,5,6,7,8,9]
        for m in range(start,stop):
            for n in range(start,stop):
                x = random.choice(num)
                grid[m][n] = x
                num.remove(x)
        start+=3
        stop+=3

#function to check if a cell is empty or not
#if cell is empty store the row and column number in the list
def isempty(c):
    for m in range(9):
        for n in range(9):
            if grid[m][n] == '_':
                c[0] = m
                c[1] = n
                return True
    return False

#function to check whether n element can be placed in the cell satisfying all valid conditons of Sudoku
def isvalid(x,m,n):
    row = grid[m]
    column = [grid[i][n] for i in range(9)]
    subgrid = getcelllist(findcell(m,n))
    if x not in row and x not in column and x not in subgrid:
        return True
    return False

#function to generate the solution of Sudoku puzzle
#c is a list to store the row and column number of element
#i+1 are elements ranging from 1-9
def solvesudoku():
    c = [0,0]
    if not isempty(c):
        return True
    row = c[0]
    column = c[1]
    for i in range(9):
        if isvalid(i+1,row,column):
            grid[row][column] = i+1
            if solvesudoku():
                return True
            grid[row][column] = '_'
#function to remove 'N' no. of random elements after forming a fully solved Sudoku puzzle
#deep copy constructs a new compound object and then recursively inserts copies into it of the objects found in the original.
def gensudoku():
    grid1=copy.deepcopy(grid)
    for i in range(81-random.randint(32,38)):
        m=random.randint(0,8)
        n=random.randint(0,8)
        if grid1[m][n]!="_":
            grid1[m][n]="_"
    return grid1

filldiagonalsubgrids()
if solvesudoku():
    printsudoku(gensudoku())
#choice to whether see solution of generated Sudoku puzzle
choice=input("Do you want computer to reveal the solution? Press Y/N: ").lower()
print("")
if choice == 'y':
    printsudoku(grid) 
if choice == 'n':
    print("Good Luck! :)")
 
