import re
from collections import deque
import heapq
class Monkey():
    def __init__(self,name): 
        self.name = name
        self.items = deque()
        self.operation = None
        self.test = None
        self.ifTrue = None
        self.ifFalse = None
        self.times = 0 
    def addItems(self,items:deque):
        self.items = items
    def addOperation(self,operation):
        self.operation = operation
    def addTest(self,test):
        self.test = test
    def addIfTrue(self,ifTrue):
        self.ifTrue = ifTrue
    def addifFalse(self,ifFalse):
        self.ifFalse = ifFalse
    def doOperation(self,item):
        worry = 0 
        operation,num = monkey.operation
      
        if num == 'old':
            num = item
        num = int(num)
        
        if operation[0] == '+':
            worry = item  + num
        elif operation[0] == '-':
            worry = item  - num
        elif operation[0] == '*':
            worry = item  * num
        elif operation[0] == '/':
            worry = item / num
        #print(item, operation , num, ' = ', worry )
        return worry
    def addPackageToMonkey(self,worry,To):
        #print('addpackage',worry, To )
        package = self.items.popleft()

        for monkey in monkeys:
            if monkey.name == To:
                monkey.items.append(worry)
                break
            
def printRound(round=None):
    a = []
    if round in (1,2,3,4,5,6,710,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000):
        print('---- ROUND -----', round)
        for _ in monkeys:
            print('MONKEY', _.name, ': ',_.items,'  Total times:', _.times)
            a.append( -1*_.times)
        heapq.heapify(a)
        total = 1
        for i in range(2):
            total = heapq.heappop(a)* total
        print(total)


with open('day11/day11_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()

monkeys = []

def readfile(lines,special_mod):
    name = ''
    monkey = None
    package = []
    operation = []
    test = []

    for line in lines:
        line = line.strip()
        if re.findall('Monkey', line):
            name = line.split(' ')[-1][:-1]
            monkey = Monkey(name)
          
        elif re.findall('Starting items', line):
            package= list(line.split(':')[-1].split(','))
            package = [int(i) for i in package]
            package = deque(package)
            monkey.addItems(package)
        elif re.findall('Operation', line):
            symbol, obj= line.split(' ')[-2:]
            operation = [symbol, obj]
            monkey.addOperation(operation)
        elif re.findall('Test:', line):
            num= line.split(' ')[-1]
            test = ['/', int(num)] 
            monkey.addTest(test)
            special_mod = int(num) * special_mod
            print(special_mod)
        elif re.findall('true:', line):
            monkey.addIfTrue(line.split(' ')[-1])
        elif re.findall('false:', line):
             monkey.addifFalse(line.split(' ')[-1])
        else:
            monkeys.append(monkey)
            
            
           # monkeys.append(monkey)
    monkeys.append(monkey)
    return special_mod
special_mod = 1
special_mod = readfile(lines,special_mod)
special_mod = int(special_mod)


# start working

digits = 1

for round in range(1,10001):
    if round in (10,100,1000):
        digits *= 10    
    for monkey in monkeys:
        #print('-----Monkey',monkey.name,'-----')
        for item in list(monkey.items):
            #print('-----Monkey',monkey.name,'-----')
            #operation
            monkey.times += 1
            worry = monkey.doOperation(item)
            #print(worry)
            
            #worry = worry//3
            #test
            #print(monkey.test)
            #print('before',monkey.items)
            # testing
            
            worry = worry%special_mod


            if  worry % (monkey.test[1]) == 0: #iftrue
               #worry = worry//monkey.test[1]
               monkey.addPackageToMonkey(worry,monkey.ifTrue)
          
            else:
                #worry = worry//monkey.test[1]
                monkey.addPackageToMonkey(worry,monkey.ifFalse)
            #print('after', monkey.items)
        
    printRound(round)    


            





