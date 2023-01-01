

score = {'A': 1, 'B': 2, 'C': 3} #rock, paper, scissors
condition = {'Z': 6, 'Y': 3, 'X':0}
win_symbol= {'A': 'C' , 'B':'A', 'C':'B'} 
answer = 0 

with open('day2/day2_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
    #print(lines)
for line in lines:
        #line 0 , line 2 
    if line[2] == 'Y':
        action = line[0]
    elif line[2] == 'X':
        action = win_symbol[line[0]]
    else: 
        action =list(filter(lambda x: win_symbol[x] == line[0], win_symbol))[0]

    answer = answer + score[action] + condition[line[2]]
print(answer)
