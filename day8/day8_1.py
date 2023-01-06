class node():
    def __init__(self, height:int ,row: int, col:int):
        self.height = height
        self.row = row
        self.col = col
    def getrow(self):
        return self.row
    def getcol(self):
        return self.col
    def getheight(self):
        return self.height
    def cord(self, str):
        print( str,' : (',self.row,',' ,self.col,')')
    def isValid(self):
        if self.row == -1 and self.col == -1:
            return False
        else: 
            return True
    def isVisible(self, target:int):

        if int(self.height) > int(target):
            return True
        else: 
            return False
        
import re
from collections import deque
with open('day8/day8_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
y = len(lines)
x = len(lines[0])

map = [[0 for col in range(x-1)] for row in range(y)]
for i,line in enumerate(lines):
    
    for j,char in enumerate(line):
        if char != '\n':
            map[i][j] = char

visible = 0 
visibles = {}
queue = deque()
start = node(map[0][0],0,0)
dummy = node(0,-1,-1)
queue.append(start)
visited = {} # hashmap 

while queue:
    curr = queue.popleft()
    row = curr.getrow()
    col = curr.getcol()
    print('curr: ',row, '  ', col)
    if (row,col) not in visited: # start working # below 4 is for putting them in queue/ visisted
        left = node(map[row][col-1],row,col-1) if col-1>=0  else dummy
        right = node(map[row][col+1],row,col+1) if col+1<x-1 else dummy
        top = node(map[row-1][col],row-1,col) if row-1>=0 else dummy
        bottom = node(map[row+1][col],row+1,col) if row+1<y else dummy

        #add queue
        if  left.isValid(): queue.append(left)
        if  right.isValid(): queue.append(right)
        if  top.isValid(): queue.append(top)
        if  bottom.isValid(): queue.append(bottom)
        

        #check visiable need to get (top bottom left right max )
        if not left.isValid() or not right.isValid() or not top.isValid() or not bottom.isValid(): 
            # is edge 
            visible += 1
            visibles[row,col] = map[row][col]
        elif curr.isVisible(max(map[row][:col],default=0))   :#check left
            visible += 1
            visibles[row,col] = map[row][col]
        elif curr.isVisible(max(map[row][col+1:],default=0))   :#check right
            visible += 1
            visibles[row,col] = map[row][col]
        elif curr.isVisible(max([a[col] for a in map][:row],default=0))   :#check top
            visible += 1
            visibles[row,col] = map[row][col]
        elif curr.isVisible(max([a[col] for a in map][row+1:],default=0))   :#check left
            visible += 1
            visibles[row,col] = map[row][col]

        # add visited 
        visited[row,col] = map[row][col]

    #print(visibles)
    print(visible)





            








