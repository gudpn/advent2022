from collections import deque

with open('day6/day6_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)
message = ''
window = deque()
for line in lines:
    message = line


for i in range(4):
    while message[i] in window:
        
        window.popleft()
    window.append(message[i])

    
for i in range(4,len(message)):
    while message[i] in window:
        window.popleft()

    if len(window) == 4:
        print(i)
        break
    window.append(message[i])


