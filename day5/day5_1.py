"""


[T] [V]                     [W]    
[V] [C] [P] [D]             [B]    
[J] [P] [R] [N] [B]         [Z]    
[W] [Q] [D] [M] [T]     [L] [T]    
[N] [J] [H] [B] [P] [T] [P] [L]    
[R] [D] [F] [P] [R] [P] [R] [S] [G]
[M] [W] [J] [R] [V] [B] [J] [C] [S]
[S] [B] [B] [F] [H] [C] [B] [N] [L]
 1   2   3   4   5   6   7   8   9 

"""
import re
class Stack:
    def __init__(self):
        self.items = []
    def empty(self):
        return not self.items
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[-1]

def init_stacks():
    #stack 1 :
    stacks[0].push('S')
    stacks[0].push('M')
    stacks[0].push('R')
    stacks[0].push('N')
    stacks[0].push('W')
    stacks[0].push('J')
    stacks[0].push('V')
    stacks[0].push('T')

  #stack 2 :
    stacks[1].push('B')
    stacks[1].push('W')
    stacks[1].push('D')
    stacks[1].push('J')
    stacks[1].push('Q')
    stacks[1].push('P')
    stacks[1].push('C')
    stacks[1].push('V')
#stack 3 :
    stacks[2].push('B')
    stacks[2].push('J')
    stacks[2].push('F')
    stacks[2].push('H')
    stacks[2].push('D')
    stacks[2].push('R')
    stacks[2].push('P')
#stack 4 :
    stacks[3].push('F')
    stacks[3].push('R')
    stacks[3].push('P')
    stacks[3].push('B')
    stacks[3].push('M')
    stacks[3].push('N')
    stacks[3].push('D')
#stack 5 :
    stacks[4].push('H')
    stacks[4].push('V')
    stacks[4].push('R')
    stacks[4].push('P')
    stacks[4].push('T')
    stacks[4].push('B')
#stack 6 :
    stacks[5].push('C')
    stacks[5].push('B')
    stacks[5].push('P')
    stacks[5].push('T')
#stack 7 :
    stacks[6].push('B')
    stacks[6].push('J')
    stacks[6].push('R')
    stacks[6].push('P')
    stacks[6].push('L')
#stack 8 :
    stacks[7].push('N')
    stacks[7].push('C')
    stacks[7].push('S')
    stacks[7].push('L')
    stacks[7].push('T')
    stacks[7].push('Z')
    stacks[7].push('B')
    stacks[7].push('W')  
#stack 9 :
    stacks[8].push('L')
    stacks[8].push('S')
    stacks[8].push('G')

answer = ''
stacks = [Stack() for x in range (9)]
init_stacks()
with open('day5/day5_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)

for line in lines:
    digits = re.findall(r'\d+', line)
    digits = [int(_) for _ in digits]
    for _ in range(digits[0]):
        box = stacks[digits[1]-1].pop()
        stacks[digits[2]-1].push(box)

for i in stacks:
    answer = answer + i.peek()
print(answer)
