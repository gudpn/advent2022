
def drawCRT( CRT_cycle,mid_sprite):

    row = (CRT_cycle//40)
    col = CRT_cycle % 40  
    symbol =''
    if abs(col - mid_sprite) <=1:
        symbol='#'
    else:
        print( col, 'mid_sprite:', mid_sprite)
        symbol='.'

    CRT[row] =  list((CRT[row]))
    CRT[row][col] = symbol
    CRT[row] = ''.join(CRT[row])
    return CRT
    
#from collections import deque
with open('day10/day10_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()

cycle = 1
CRT = ['_'*40 for s in range(6)]
CRT_cycle = 0 

register = 1
lists = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}

for line in lines:
    if ' ' not in line:
        cmd = line.strip()
    else:
        cmd, num = line.strip().split(' ')


    if cmd == 'noop':
        CRT = drawCRT(CRT_cycle,register)
        
        cycle += 1
        CRT_cycle += 1 
    elif cmd == 'addx':
        CRT = drawCRT(CRT_cycle,register)


        cycle += 1
        CRT_cycle += 1 
        if cycle in lists:
            lists[cycle] = cycle * register
        CRT = drawCRT(CRT_cycle,register)

        cycle += 1
        CRT_cycle += 1 
        register += int(num)

    if cycle in lists:
        lists[cycle] = cycle * register

# print(lists)
# print(cycle)##

# sumsss = sum(lists.values() )
# print(sumsss)
for i in CRT:
    print(i)
