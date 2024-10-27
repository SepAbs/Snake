b=[]
for i in range(50):
    b.append(" "*50)

obj="<="
Loc=[25, 24]
#def edges(Loc):
b[Loc[0]]=b[Loc[0]][:Loc[1]] + obj +b[Loc[0]][Loc[1]+len(obj)+1:]
def side(s):
    if s=="<":
        b[Loc[0]]=b[Loc[0]][:Loc[1]-1] + obj +b[Loc[0]][Loc[1]+len(obj):]
    elif s==">":
        b[Loc[0]]=b[Loc[0]][:Loc[1]+1] + obj +b[Loc[0]][Loc[1]+len(obj)+2:]
    for i in b:
        print(i)
