from collections import deque

with open('day6/day6_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)
message = ''
size = 14
window = deque()
for line in lines:
    message = line


for i in range(size):
    while message[i] in window:
        
        window.popleft()
    window.append(message[i])

    
for i in range(size,len(message)):
    while message[i] in window:
        window.popleft()

    if len(window) == size:
        print(i)
        break
    window.append(message[i])


