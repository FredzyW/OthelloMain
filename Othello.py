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
#Man kan edita om man går in på filen på Githubs hemsida och klickar edit på Toms fil
