

#use this to make a 2d array using ascii

titles=['tx','ty']
names=['abc','defg']
class table:
    titles = []
    names = []
    border_top="_"
    border_sides="|"
    border_bottom="_"
    tablelines="_"
    width=2
    height=3
    long_name=0
    variables = []
    
    

    def __init__(self,
                 titles,
                 names,
                 variables=[['ax','ay'],['bx','by']]):
        
        self.titles = titles
        self.names = names
        self.variables = variables
        
        longest = len(names[0])
        for n in self.names:
            self.height += 2
            if len(n) > longest:
                longest = len(n)
        self.width += (longest+2)
        self.long_name = longest
        for t in self.titles:
            #                   ' '  |
            self.width += len(t)+4 + 1

        
        

    def draw(self):
        width = self.width
        name_box = ''
        
        for ln in range(self.long_name):
            name_box+=' '
            
        border_line = ''
        for s in range(self.long_name+2):
            border_line+='_'
        
        name_spaces = ''
        
        '______________________'
        '| long |  t1  |  t2  |'
        '|______|______|______|'
        '| abc  |  ax  |  ay  |'
        '|______|      |      |'
        '| defg |  bx  |  by  |'
        '|______|______|______|'
        #Border Top
        for w in range(width):
            print(self.border_top,end='')
        print()
        
        #Title Line
        print(self.border_sides+' '+name_box+' |',end='')
        for t in self.titles:
            print('  '+t+'  ',end='|')
        print()

        #Spaces Line
        print('|'+border_line,end='|')
        for t in range(len(self.titles)):
            print(border_line,end='|')
        print()

        #Name Lines
        
        for name in self.names:
            
            #name
            print(end='|')
            newname=name
            if len(name) < self.long_name:
                space_diff = self.long_name-len(name)
                for s in range(space_diff):
                    newname+=' '
            print(' '+newname+' ',end='|')
            
            #variable
            for v in self.variables[self.names.index(name)]:
                print('  '+v+'  ',end='|')
            print()
            print('|'+border_line+'|',end='')
            for t in range(len(self.titles)):
                print(border_line,end='|')
            print()
            
            
            

    

        
        
            

t = table(titles, names)





