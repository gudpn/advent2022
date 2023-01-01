
answer = 0 
i = 1
with open('day4/day4_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)

for line in lines:
        #line 0 , line 2 
    a,b = line.split(',')
    a1,a2 = a.split('-')
    b1,b2 = b.split('-')
    a1,a2 = int(a1),int(a2)
    b1,b2 = int(b1),int(b2)
    
    if (a2< b1 and a1<=a2 ) \
        or (b2<a1 and a1<=a2):
        print ( ' counttt i:  ', i, '  ',a,b)
        answer = answer + 1 
    else:
        print ( 'i:  ', i, '  ',a,b)  
    i = i+1
print('answer ' ,i-1 - answer)


    




   
  