from bombs import makeBombs
from grid import *
from Square import setValue

def startGame():
    print(("Welocome in Saper Game! Please choose level: \nbeginner - wrtie 1  \nadvanced - write 2"))
    choose = None
    while(choose not in [1,2,3]):
        try:
            choose=int(input("Your choose: "))
            if choose not in [1,2,3]:
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

    return grid


def playGame(grid):

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
                    grid=unhideGrid(msc[0],msc[1],grid)
        except ValueError:
            print("Ops, wrong command! Try again.")

        n = grid.shape[0]
        m = grid.shape[1]
        for i in range(n):
            for j in range(n):
                if grid[i,j].getHidden()==False:
                    count+=1
        if count == (n*n - m):
            print("You win!")
            break
        printGrid(grid)

playGame(startGame())