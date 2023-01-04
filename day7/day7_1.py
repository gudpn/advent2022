class TreeNode():
    def __init__(self,name: str, size:int,children= None,parent= None):
        self.name = name
        self.children = [] or children
        self.parent = parent
        self.size = size

    def get_size(self):
        return self.size 
    def get_name(self):
        return self.name
import re
with open('day7/day7_input.txt', 'r') as file:
    # Read the contents of the file
    lines = file.readlines()
   # print(lines)


filesys =TreeNode(name='/', size = 0)
filesys.parent = filesys
current  = filesys

for line in lines:
    #print(line)
    args = line.split(' ')
    print (args)
    
    if args[0] == '$' and args[1] == 'cd':
        args[2] = re.sub('\n+','', args[2])
        print('args[2]', args[2])
        if args[2]== '/':
            print(' move to / ')
            current  = filesys
        elif args[2] == '..' : #move to parent
            print('move to parent')
            current = current.parent
        else : #move to a dir
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
    if args[0] == '$' and args[1] == 'ls':# wait for next line
        print ('ls')
    if args[0] == 'dir': #add a directory if 
        print('add directory')
        args[1] = re.sub('\n+','', args[1])
        if current.children is None:
            current.children =[TreeNode(name=args[1], size = 0, parent= filesys)]
        else:
            current.children.append(TreeNode(name=args[1], size = 0, parent= filesys))
        print( 'children: ', current.children[0].get_name())
    
    
