# Open the file in read-only mode
import heapq
curr = 0 
maxi = 0 
asshold = []


with open('day1/day1_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)
for line in lines:
    if line != '\n' :
        curr = curr+ int(line)
    else:
        asshold.append(curr)
        curr = 0
heap = [-x for x in asshold]
heapq.heapify(heap)

for _ in range(3):
    maxi = maxi + -heapq.heappop(heap)
print(maxi)