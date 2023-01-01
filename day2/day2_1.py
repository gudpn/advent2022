

score = {'X': 1, 'Y': 2, 'Z': 3} #rock, paper, scissors
condition = {'win': 6, 'draw': 3, 'lose':0}
symbol= {'A': 'X' , 'B':'Y', 'C':'Z'} 
answer = 0 
with open('day2/day2_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)
for line in lines:
        #line 0 , line 2 
    o = symbol[line[0]] 
    if o == line[2]:
        status =  'draw'
    elif (o== 'X' and line[2] == 'Y' ) \
            or  (o == 'Y' and line[2] == 'Z') \
                or (o == 'Z' and line[2] == 'X'  ):
        status = 'win'
    else:
        status = 'lose'
    #print(symbol[line[0]])
    answer = answer + score[line[2]] + condition[status]
print(answer)
