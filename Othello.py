import random

board=[]
rad=[]
for a in range(1,9):
    rad.append("#")
    
for a in range(1,9):
    board.append(rad)
    

for e in board:
    for r in e:
        print(r,end=' ')
    print()
