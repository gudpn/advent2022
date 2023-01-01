
answer = 0 
i = 1
with open('day3/day3_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)
linesss = ['','','']
for line in lines:
        #line 0 , line 2 
    linesss[(i-1)%3] = line
    if i % 3 == 0 : 
        for chr in linesss[0]:
            if chr in linesss[1] and chr in linesss[2]:
                ascii = ord(chr)
                if  65<= ascii <= 90:
                    answer = answer + ascii - 38
                elif  97<= ascii <= 122:
                    answer = answer + ascii - 96
                break
        print('answer ' ,answer)
    i = i + 1




   
  