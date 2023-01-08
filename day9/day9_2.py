import re
from collections import deque
with open('day9/day9_sample1.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
ropes = [(0,0) for i in range(10)]

adj=''


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
        
        for rope in range(len(ropes)-1):
           # print('error before', ropes[rope] , '   ', ropes[rope+1])

            
            # T is some row as H and it , just follow H  , or it means moving L / R
            if ropes[rope+1][0] == ropes[rope][0] and abs(ropes[rope][1] - ropes[rope+1][1]) >1:
                ropes[rope+1]= (ropes[rope+1][0]+ MOVEROW[dir],ropes[rope+1][1]+MOVECOL[dir])
            # not in same row, need to check if they are diagonal if 'l''r'
            # move to same row with H 
            elif ropes[rope+1][0] != ropes[rope][0] and abs(ropes[rope][1] - ropes[rope+1][1]) >1 and (dir == 'L' or dir == 'R' ):
               
                ropes[rope+1]=(ropes[rope][0], ropes[rope+1][1]+MOVECOL[dir] )
        
            elif ropes[rope+1][1] == ropes[rope][1] and abs(ropes[rope][0] - ropes[rope+1][0]) >1:
                ropes[rope+1]= (ropes[rope+1][0]+ MOVEROW[dir],ropes[rope+1][1]+MOVECOL[dir])
            elif ropes[rope+1][1] != ropes[rope][1] and abs(ropes[rope][0] - ropes[rope+1][0]) >1 and (dir == 'U' or dir == 'D' ):
                ropes[rope+1]=(ropes[rope+1][0]+ MOVEROW[dir] , ropes[rope][1])
            elif ropes[rope+1][0] == ropes[rope][0] and abs(ropes[rope][1] - ropes[rope+1][1]) <=1:
                 a = 1 
            elif ropes[rope+1][1] == ropes[rope][1] and abs(ropes[rope][0] - ropes[rope+1][0]) <=1:
                a=1
                #print('here: same row , same place  :',rope+1) 
            elif ropes[rope+1][0] != ropes[rope][0]  and ropes[rope+1][1] != ropes[rope][1] and abs(ropes[rope][1] - ropes[rope+1][1]) >1 and abs(ropes[rope][0] - ropes[rope+1][0]) >1 :
                print('all side need to update')
                #ropes[rope+1]=(ropes[rope][0]+ MOVEROW[dir], ropes[rope][1])
            elif ropes[rope+1][1] != ropes[rope][1] and abs(ropes[rope][1] - ropes[rope+1][1]) >1 and (dir == 'U' or dir == 'D' ):
                # move up but actually need to move 2 dir
                
                H=(ropes[rope+1][0]+ MOVEROW[dir] , ropes[rope+1][1]+MOVECOL[dir])
                #print('1 :' , H)
                if (dir == 'U' or dir == 'D') and H[1] -T[1] >0:
                    adj = 'R'
                elif (dir == 'U' or dir == 'D') and H[1] -T[1] <0:
                    adj = 'L'
                elif(dir == 'L' or dir == 'R') and H[0] -T[0] >0:
                    adj = 'U'
                elif(dir == 'L' or dir == 'R') and H[0] -T[0] <0:
                    adj = 'D'
                H = (H[0]+ MOVEROW[adj] , H[1]+MOVECOL[adj])
                #print ('2: ',H)
                ropes[rope+1] = H
            elif ropes[rope+1][0] != ropes[rope][0] and abs(ropes[rope][0] - ropes[rope+1][0]) >1 and (dir == 'L' or dir == 'R' ):
                # move up but actually need to move 2 dir
                print( rope,'before node:',ropes[rope], '  node + 1:' , ropes[rope+1])
                H=(ropes[rope+1][0]+ MOVEROW[dir] , ropes[rope+1][1]+MOVECOL[dir])
                print('before node:',ropes[rope])
                print('1 :' , H)
                if (dir == 'U' or dir == 'D') and H[1] -T[1] >0:
                    adj = 'R'
                elif (dir == 'U' or dir == 'D') and H[1] -T[1] <0:
                    adj = 'L'
                elif(dir == 'L' or dir == 'R') and H[0] -T[0] >0:
                    adj = 'U'
                elif(dir == 'L' or dir == 'R') and H[0] -T[0] <0:
                    adj = 'D'
                H = (H[0]+ MOVEROW[adj] , H[1]+MOVECOL[adj])
                print ('2: ',H)
                ropes[rope+1] = H
            else:
                print('here',rope+1, ropes[rope+1][1] != ropes[rope][1], '   ',abs(ropes[rope][0] - ropes[rope+1][0]) >1  ,'  ', (dir == 'U' or dir == 'D' ))
            #print('error after', ropes[rope] , '   ', ropes[rope+1])
       
    
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
