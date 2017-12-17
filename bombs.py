import random as r

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