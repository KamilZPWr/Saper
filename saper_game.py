import random as r
import numpy as np

### klasa dla pojedynczych kwadratów
class Square:
    def __init__(self,bomb,hidden):
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
        self.value=9

    def showSquare(self):
        self.hidden = False

    def getHidden(self):
        return self.hidden

    def setFlag(self,val):
        self.flag=val

    def getFlag(self):
        return self.flag

### funkcja losująca bomby
def makeBombs(n,m):
    bombs=[]
    while(len(bombs)!=m):
        a = r.randint(0, n-1)
        b = r.randint(0, n-1)
        if [a,b] in bombs:
            continue
        else:
            bombs=bombs+[[a,b]]
    return bombs

### funkcja tworząca planszę
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

### funkcja obliczająca ilość sąsiadów
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
    
    
def unhide(x,y):
    if (x<0 or x>n-1):
        return grid ## poza tablicą wyjście
    if (y<0 or y>n-1):
        return grid ## poza tablicą wyjście
    if (grid[x,y].getHidden()==False):
        return grid ## już odkryte wyjście
 
    if(grid[x,y].getValue()!=9 and grid[x,y].getHidden()==True):
        grid[x,y].showSquare()   ## odkryj!
 
    if (grid[x,y].getValue()!=0):
        return grid## wartość > 0 wyjście
 
    ##wywołanie funkcji dla każdego sąsiada
    unhide(x-1,y-1);
    unhide(x-1,y);
    unhide(x-1,y+1);
    unhide(x+1,y-1);
    unhide(x+1,y);
    unhide(x+1,y+1);
    unhide(x,y-1);
    unhide(x,y);
    unhide(x,y+1);
    
    return grid

def printGrid(grid):
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

#### script
tmp = True
print(("Welocome in Saper Game! Please choose level: \nbeginner - wrtie 1  \nadvanced - write 2"))
while(tmp):
    try:
        choose=int(input("Your choose: "))
        if choose in [1,2,3]:
            tmp = False
        else:
            print("Ops, wrong number! Try again.")
    except ValueError:
        print("You must write number, nothing else!")

if  choose == 1:
    n = 8
    m = 10
elif choose == 2:
    n = 16
    m = 40

bombs = makeBombs(n,m)
grid = makeGrid(n,bombs)
grid=setValue(grid)

print("\nINSTRUCTION: To type place write only ,,X Y'', to flag place write ,,flag'' before, to unflag write ,,unflag'', to exit write ,,exit''.")
printGrid(grid)
while(True):
    count = 0
    
    msc=str(input("\nType place : "))
    msc=msc.split()
    try:
        if msc[0].upper() == "EXIT":
            break
        elif msc[0].upper()=='FLAG':
            msc[1]=int(msc[1])-1
            msc[2]=int(msc[2])-1
            grid[msc[1],msc[2]].setFlag(True)
        elif msc[0].upper()=='UNFLAG':
            msc[1]=int(msc[1])-1
            msc[2]=int(msc[2])-1
            grid[msc[1],msc[2]].setFlag(False)
        else:
            msc[0]=int(msc[0])-1
            msc[1]=int(msc[1])-1
            if grid[msc[0],msc[1]].getValue()==9:
                grid[msc[0],msc[1]].showSquare()
                printGrid(grid)
                print("Ops! It was bomb, you lose.")
                break
            elif grid[msc[0],msc[1]].getValue() in [1,2,3,4,5,6,7,8]:
                grid[msc[0],msc[1]].showSquare()
            else:
                grid=unhide(msc[0],msc[1])
    except ValueError:
        print("Ops, wrong command! Try again.")
    for i in range(n):
        for j in range(n):
            if grid[i,j].getHidden()==False:
                count+=1
    if count == (n*n - m):
        print("You win!")
        break
    printGrid(grid)
