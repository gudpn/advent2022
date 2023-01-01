# Open the file in read-only mode

curr = 0 
maxi = 0 


with open('day1/day1_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
    #print(lines)
for line in lines:
    if line != '\n' :
        curr = curr+ int(line)
    else:
        maxi = max(maxi,curr)
        curr = 0
print(maxi)