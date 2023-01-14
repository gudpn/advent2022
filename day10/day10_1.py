import re
from collections import deque
with open('day10/day10_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()

cycle = 1
register = 1
list  = {20:0, 60:0, 100:0, 140:0,180:0,220:0}

for line in lines:
    if ' ' not in line:
        cmd = line.strip()
    else:
        cmd, num = line.strip().split(' ')
        
  
    print("start current is ", cycle, line)
    
    
    if cmd == 'noop':
        print('end cycle ',cycle , register)

        cycle +=1 
        print('end cycle ',cycle , register)        
    elif cmd == 'addx':
        print('end cycle ',cycle , register)
        cycle += 1 
        print('end cycle ',cycle , register)
        if cycle in list:
            list[cycle] = cycle * register
        
        cycle +=1
        register += int(num)
        print('end cycle ',cycle , register)
    print(' ',cycle , register)
    if cycle in list:
        list[cycle] = cycle * register
    
print(list)
print(cycle)

sumsss = sum(list.values() )
print(sumsss)
