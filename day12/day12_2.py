
import re
from collections import deque
import heapq
with open('day12/day12_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()


def move(point,dir):
    r , c = (point)
 
    newpt = (r + MOVEROW[dir] , c + MOVECOL[dir])
    if  (0 <= newpt[0] < len(map)  and 0 <= newpt[1] < len(map[0])):
        if  value(newpt) <=value(point) + 1:
            #can climb
            #print('In move move from', point, ' to ', newpt)
            return newpt
        else:
            return point
    else:
        return point # return the original one/ (0,0)

def value(point):
    r,c = (point)
    if map[r][c] == 'S':
        return 0
    elif map[r][c] == 'E':
        return 25
    else:
        return ord(map[r][c])-96

def checkdir(p1,p2 ):
    r1 , c1 = (p1)
    r2 , c2 = (p2)

    if r1 == r2: # l or r
        if c1 <c2:
            return 'R'
        else:
            return 'L'
    else: #u or d
        if r1< r2:
            return 'D'
        else:
            return 'U'


dir_map =[]
map = []
STARTS = []
END = (0,0)
row = 0
col = 0
for line in lines:
    if 'S' in line:
        col = line.find('S')
        
        STARTS.append((row,col))
    if 'a' in line:
        cols =  [ a.start() for a in re.finditer('a',line)]
       
        for col in cols:
            STARTS.append((row,col))
    if 'E' in line:
        col = line.find('E')
        END = (row,col)
    map.append(list(line.strip()))
    dir_map.append(list(line.strip()))
    row += 1

MOVEROW = {'L':0,'R':0,'U':-1, 'D': 1} 
MOVECOL = {'L':-1,'R':1,'U':0, 'D': 0} 
dir = ['L', 'R','U', 'D']
arrow = {'L':'<', 'R':'>','U':'^', 'D':'v'}


def findStart(START,END):


    # finding shortest path 
    visited = {}
    min_dis = {} #save the shortest path value

    searching = True
    current_q = []
    #current_q.append((0, START))
    min_dis[START] = 0

    heapq.heappush(current_q,(0,START))
    while searching and  len(current_q) >0: 
        steps,current = heapq.heappop(current_q)
        
        #find neighbour 
        if current not in visited:
            for i in dir:
                neighbour = move(current,i) 
                r,c = neighbour
                if neighbour != current: # a valid neigbour
                    if neighbour not in visited: 
                        min_dis[neighbour] = min_dis[current] +1
                        #print('min dis from ', neighbour ,'and S :' , min_dis[current] +1)
                    
                    else: # need to store the min
                        
                        x = min_dis[neighbour]
                        
                        min_dis[neighbour] = min(min_dis[neighbour],min_dis[current] +1)
                    heapq.heappush(current_q,(steps +1,neighbour))    
            if current == END:
                searching = False
                print('herere' , min_dis[END])
                return (min_dis[END])
            visited[current] = 1
    return 9292929  ##very very learge num

mini = []
print(STARTS)
print(END)
for START in STARTS: 
    
    c = findStart(START,END)
    heapq.heappush(mini, (c, START))
print (heapq.heappop(mini))
    


 





