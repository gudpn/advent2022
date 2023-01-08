
import re
from collections import deque
with open('day9/day9_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
H = (0,0)
T = (0,0)
S = (0,0)
path = {}
MOVEROW = {'L':0,'R':0,'U':1, 'D': -1} 
MOVECOL = {'L':-1,'R':1,'U':0, 'D': 0} 
for line in lines:
    dir,step = line.strip().split(' ')
    print(dir,step)
    step = int(step)
    for i in range(step):
        H = (H[0] + MOVEROW[dir], H[1] + MOVECOL[dir])
        # T is some row as H and it , just follow H  , or it means moving L / R
        if T[0] == H[0] and abs(H[1] - T[1]) >1:
            T= (T[0]+ MOVEROW[dir],T[1]+MOVECOL[dir])
        # not in same row, need to check if they are diagonal if 'l''r'
        # move to same row with H 
        elif T[0] != H[0] and abs(H[1] - T[1]) >1 and (dir == 'L' or dir == 'R' ):
            T=(H[0], T[1]+MOVECOL[dir] )
       
        elif T[1] == H[1] and abs(H[0] - T[0]) >1:
            T= (T[0]+ MOVEROW[dir],T[1]+MOVECOL[dir])
        elif T[1] != H[1] and abs(H[0] - T[0]) >1 and (dir == 'U' or dir == 'D' ):
            T=(T[0]+ MOVEROW[dir] , H[1])
       
            
        if T not in path:
            path[T] = 0 
        print('H:', H , '    ', 'T:', T )
print(path)
print(len(path))
