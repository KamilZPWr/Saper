class Square:
    def __init__(self, bomb, hidden):
        self.bomb = bomb
        self.hidden = True
        self.value = 0
        self.flag = False

    def getType(self):
        if self.bomb == True:
            return True
        else:
            return False

    def addValue(self):
        self.value += 1

    def getValue(self):
        return self.value

    def setBomb(self):
        self.value = 9

    def showSquare(self):
        self.hidden = False

    def getHidden(self):
        return self.hidden

    def setFlag(self, val):
        self.flag = val

    def getFlag(self):
        return self.flag

def setValue(grid):
    n = grid.shape[0]
    for i in range(n):
        for j in range(n):
            if grid[i,j].getType() == True:
                grid[i,j].setBomb()
                if i-1>=0 and j-1 >=0 and grid[i-1,j-1].getType() != True:
                    grid[i-1,j-1].addValue()
                if i-1>=0 and grid[i-1,j].getType() != True:
                    grid[i-1,j].addValue()
                if i-1>=0 and j+1 < n and grid[i-1,j+1].getType() != True:
                    grid[i-1,j+1].addValue()
                if j-1 >=0 and grid[i,j-1].getType() != True:
                    grid[i,j-1].addValue()
                if j+1<n and grid[i,j+1].getType() != True:
                    grid[i,j+1].addValue()
                if i+1<n and j-1 >=0 and grid[i+1,j-1].getType() != True:
                    grid[i+1,j-1].addValue()
                if i+1<n and grid[i+1,j].getType() != True:
                    grid[i+1,j].addValue()
                if i+1<n and j+1 <n and grid[i+1,j+1].getType() != True:
                    grid[i+1,j+1].addValue()
    return grid