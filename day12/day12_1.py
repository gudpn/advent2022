from collections import deque
with open('day12/day12_sample.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()



def move(point,dir):
    r , c = (point)
 
    newpt = (r + MOVEROW[dir] , c + MOVECOL[dir])
    print(newpt,  0<= newpt[0] < len(map)  , 0<= newpt[1] < len(map[0]) )
    if  0<= newpt[0] < len(map)  and 0<= newpt[1] < len(map[0]) :
        print(newpt)
        if  abs(value(newpt) - value(point)) <=1  : 
            #can climb
            print('In move move from', point, ' to ', newpt)
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
        return 777
    else:
        return ord(map[r][c])-96

dir_map =[]
map = []
START = (0,0)
END = (0,0)
row = 0
col = 0
for line in lines:
    
    if line.find('S') >=0:
        col = line.find('S')
        START = (row,col)
    if line.find('E') >=0:
        col = line.find('E')
        END = (row,col)
    map.append(list(line.strip()))
    dir_map.append(list(line.strip()))
    row += 1

MOVEROW = {'L':0,'R':0,'U':-1, 'D': 1} 
MOVECOL = {'L':-1,'R':1,'U':0, 'D': 0} 
dir = ['L', 'R','U', 'D']
arrow = {'L':'<', 'R':'>','U':'^', 'D':'v'}
print(START,END)
print(len(map))
print(len(map[1]))

# finding shortest path 
visited = {}
min_dis = {} #save the shortest path value

searching = True
current_q = deque()
current_q.append(START)
min_dis[START] = 0
while searching and len(current_q) >0: 
    current = current_q.popleft()
    
    #find neighbour 
    if current not in visited:
        for i in dir:
            neighbour = move(current,i) 
            r,c = neighbour
            if neighbour != current: # a valid neigbour
                if neighbour not in visited: 
                    min_dis[neighbour] = min_dis[current] +1
                 
                    print('min dis from ', neighbour ,'and S :' , min_dis[current] +1)
                else: # need to store the min
                    min_dis[neighbour] = min(min_dis[neighbour],min_dis[current] +1)
              
                    print('min dis from ', neighbour ,'and S updated:' , min(min_dis[neighbour],min_dis[current] +1))
                if neighbour not in current_q:
                
                    current_q.append(neighbour)
                
        if current == END:
            searching = False
            print(min_dis[END])
        print('Finished ', current)

        visited[current] = 1
print(min_dis)

p = max(min_dis, key=min_dis.get)
print(p, min_dis[p])



for  i in dir_map:
    print(i)