


answer = 0 

with open('day3/day3_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)
for line in lines:
        #line 0 , line 2 
    a = len(line)-1
    fh = int(a/2)
    a1 = line[0:fh]
    a2 = line[fh:]

    for chr in a1:
        if chr in a2:
            ascii = ord(chr)
            if  65<= ascii <= 90:
                answer = answer + ascii - 38
            elif  97<= ascii <= 122:
                answer = answer + ascii - 96
            break
    print(answer)




   
  