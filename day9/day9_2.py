def movement(rope,H, T):
    # no need to see left right , the main point is to follow prev node and do adjustment
    
    if abs(H[0] - T[0])>1 and abs(H[1] - T[1]) >1: # move  2 ways 
        
        if H[1] > T[1]:
            T= (T[0] ,T[1]+1)
        else:
            T= (T[0] ,T[1]-1)

        if H[0] > T[0]:
            T= (T[0]+1 ,T[1])
        else:
            T= (T[0]-1 ,T[1])

    elif abs(H[1] - T[1]) >1:# 'move left / right only '
        ####### this is very important :use H[0] as the ref as the anchor, instead of T[0]
        ### e.g. H(2,5) , T(0,4)
       
        if H[1] > T[1]:
            T= (H[0] ,T[1]+1)
        else:
            T= (H[0] ,T[1]-1)
        # not in same row, need to check if they are diagonal if 'l''r'
        # move to same row with H 
    elif abs(H[0] - T[0]) >1:# 'move up down only '
        ####### this is very important :use H[0] as the ref as the anchor, instead of T[0]
        ### e.g. H(2,5) , T(0,4)
        if H[0] > T[0]:
            T= (T[0]+1 ,H[1])
        else:
            T= (T[0]-1 ,H[1])
        # not in same row, need to check if they are diagonal if 'l''r'
        # move to same row with H 
    print(rope, H,T)
    return T
import re
from collections import deque
with open('day9/day9_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
ropes = [(0,0) for i in range(10)]




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
        ropes[0] = (ropes[0][0] + MOVEROW[dir], ropes[0][1] + MOVECOL[dir])
        ropes[1] = movement(1,ropes[0],ropes[1])
        for rope in range(2,len(ropes)):
            ropes[rope] = movement(rope,ropes[rope-1], ropes[rope])
    
        if ropes[9] not in path:
            print('adding ropes[9]:',ropes[9] )
            path[ropes[9]] = 0 
    
    print('H[0] :' , ropes[0] , '  ' )
    print('H[1] :' , ropes[1] , '  ' )
    print('H[2] :' , ropes[2] , '  ' )
    print('H[3] :' , ropes[3] , '  ' )
    print('H[4] :' , ropes[4] , '  ' )
    print('H[5] :' , ropes[5] , '  ' )
    print('H[6] :' , ropes[6] , '  ' )
    print('H[7] :' , ropes[7] , '  ' )
    print('H[8] :' , ropes[8] , '  ' )
    print('H[9] :' , ropes[9] , '  ' )
    print('--------')

        
        
#print(path)
print(len(path))
