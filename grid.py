from Square import Square
import numpy as np

def makeGrid(n,bombs):
    grid = np.zeros((n,n),dtype=object)
    for i in range(n):
        for j in range(n):
            for k in range(len(bombs)):
                if i == bombs[k][0] and j == bombs[k][1]:
                    grid[i,j] = Square(True,True)
            if type(grid[i,j]) == int:
                grid[i,j] = Square(False,True)
    return grid

def printGrid(grid):
    n = grid.shape[0]
    print("\n ",end="")
    for j in range(n+1):
        print("%2d " %(j),end="")
    print("\n")
    for i in range(n):
        print("%2d " %(i+1),end="")
        for j in range(n):
            if grid[i,j].getHidden()==True:
                if grid[i,j].getFlag()==True:
                    print('%3s' %'X' ,end="")
                else:
                    print('%3s' %'.' ,end="")
            else:
                if grid[i,j].getValue()==9:
                    print('%3s' %"B",end='')
                else:
                    print('%3d' %grid[i,j].getValue(),end='')
        print("")


def unhideGrid(x, y,grid):
    n = grid.shape[0]
    if (x < 0 or x > n - 1):
        return grid  ## poza tablicą wyjście
    if (y < 0 or y > n - 1):
        return grid  ## poza tablicą wyjście
    if (grid[x, y].getHidden() == False):
        return grid  ## już odkryte wyjście

    if (grid[x, y].getValue() != 9 and grid[x, y].getHidden() == True):
        grid[x, y].showSquare()  ## odkryj!

    if (grid[x, y].getValue() != 0):
        return grid  ## wartość > 0 wyjście

    unhideGrid(x - 1, y - 1,grid);
    unhideGrid(x - 1, y,grid);
    unhideGrid(x - 1, y + 1,grid);
    unhideGrid(x + 1, y - 1,grid);
    unhideGrid(x + 1, y,grid);
    unhideGrid(x + 1, y + 1,grid);
    unhideGrid(x, y - 1,grid);
    unhideGrid(x, y,grid);
    unhideGrid(x, y + 1,grid);

    return grid