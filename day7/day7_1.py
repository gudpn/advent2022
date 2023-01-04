class TreeNode():
    def __init__(self,name: str, size:int,children= None,parent= None, dir:bool = False):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = size
        self.dir = dir

    def get_size(self):
        return self.size 
    def get_name(self):
        return self.name
    def totalsize(self):
        answer = 0 
        if answer >0:
            return answer + self.size 
        if self.dir == True:
            for i in self.children:
                answer = i.size + answer 
        return answer 
        
    def calTreefunc(self):
        answer = 0
        print(self.get_name())
        if  self.dir == True :
         #  this is a directory
            if self.children is not None:
                for i in self.children:
                    print( self.get_name() ,' have children: ',i.get_name())
                    if i.size < 100000 and i.dir == True:
                        print('before', answer)
                        answer +=  i.size
                        print('total:',answer)
                
                    print(self.get_name() ,'is a dir with self.size = ', self.get_size())
                    answer += i.calTreefunc()
                print('total before return:',answer)
        return answer
    def sumDir(self):
        answer = self.size
        for i in self.children:
            answer += i.sumDir()
        print(self.get_name(), 'has a size:', answer)
        self.size = answer
        return answer
    
        
def calOuterfunc( file :TreeNode):
    answer =0 
    if file.dir == True: 
        for i in file.children:
            if i.size < 100000 and i.dir == True:
                answer += i.size #ori
                print( i.get_name(), '  answer ', answer)
            print(' before add answer:' ,answer )       
            answer += calOuterfunc(i) #ori
            print('after answer:' ,answer ) 
    return answer

        
import re
with open('day7/day7_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()

filesys =TreeNode(name='/', size = 0, dir= True)
filesys.parent = filesys
current  = filesys
answer = 0  
for line in lines:
    #print(line)
    args = line.split(' ')
    print (args)
    if args[0] == '$' and args[1] == 'cd':
        args[2] = re.sub('\n+','', args[2])
        if args[2]== '/':
            print(' move to / ')
            current  = filesys
        elif args[2] == '..' : #move to parent
            print('move to parent')
            current = current.parent
        else : #move to a dir
            print('move to a dir')
            for i in current.children:
                print(i.name, '  ==  ', args[2])
                if i.name == args[2]:
                    current = i
                    print('in' ,current.get_name())
            """
            a = TreeNode(name='a', size = 0, parent= filesys)
            b = TreeNode(name='b', size = 0, parent= filesys)
            c = TreeNode(name='c', size = 0, parent= filesys)
            e = TreeNode(name='e', size = 0, parent= filesys)
            filesys.children = [a,b,c,e]
            
            for i in filesys.children:
                print(i.name, '  ==  ', args[2])
                if i.name == args[2]:
                    current = i
                    print('in' ,current.get_name())
            """
    if args[0] == '$' and args[1] == 'ls\n':# wait for next line
        print ('ls')
    # dir x | size filename   
    if args[0] == 'dir': #add a directory if 
        print('add directory')
        args[1] = re.sub('\n+','', args[1])
        if current.children is None:
            current.children =[TreeNode(name=args[1], size = 0, parent= current, dir = True)]
        else:
            current.children.append(TreeNode(name=args[1], size = 0, parent= current, dir= True))
        print( 'children: ', current.children[0].get_name())
    if args[0].isdigit() :
        print('a file with size')
        args[1] = re.sub('\n+','', args[1])
        if current.children is None:
            current.children =[TreeNode(name=args[1], size = int(args[0]), parent= current, dir=False)]
        else:
            current.children.append(TreeNode(name=args[1], size = int(args[0]), parent= current, dir= False))
    

print('sumDir', filesys.sumDir())
print('calOuterfunc ', calOuterfunc(filesys))
print('calTreefunc ', filesys.calTreefunc())
print('totals : ', filesys.totalsize())



        