import os
import time
import sys
import textwrap


class Data:
    FileName=None
    MainCwd = None
    cwd = None
    path = None
    cpaths = []
    cfiles = []
    InitializeTimeStamp = None
    version = '0.2.14'
    
    text = ""

    def __init__(self):
        self.MainCwd = os.getcwd()
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)

        self.InitializeTimeStamp = str(time.asctime())

        self.UPL()

    def InitSettings(self):
        self.FileName=None
        self.cpaths = []
        self.cfiles = []
        self.text = ""
        self.cwd = self.MainCwd
        self.path = os.path.join(self.cwd)

    def UPL(self):
        self.cpaths = list()
        self.cfiles = list()
        cwd = self.cwd
        path = self.path
        for c in os.walk(path).__next__()[1]:
            self.cpaths.append(c)
        for c in os.walk(path).__next__()[2]:
            self.cfiles.append(c)

    def readF(self, AllLines=True, sts=False, lines=200):
        #sts = Since Time Stamp
        text = self.text
        
        if self.FileName == None:
            print("[ERROR: NO FILE SELECTED]")
            print("Use SelectFile() to select a file.")
            
        else:
            FileName = self.FileName
            with open(FileName, 'r') as f:
                text = f.read()
                self.text = text
            f.close()

        DisplayText = ""
        counted_lines = 0
        lastIndex = 0
        if sts or not AllLines:
            if not sts:
                for n in text:
                    if counted_lines >= lines:
                        lastIndex = text.index(n)
                        break
                    elif n == '\n':
                        counted_lines+=1
                    
            else:
                lastIndex = text.rfind('TIMESTAMPSTR')
                
            DisplayText = text[lastIndex:]
        else:
            DisplayText = self.text

            
        print(DisplayText)

    def sf(self, file):
        self.UPL()
        self.FileName = file
        self.readF(sts=True) #This now prints from
        #last timestamp string
        

    def cd(self, newpath=""):
        if len(str(newpath))==0:
            newpath = self.MainCwd
        elif str(newpath)[-1] == '/':
            newpath = str(newpath)[:-1]
        os.chdir(newpath)
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)
        #self.InitSettings()

    def NewFile(self, name, TITLE=' ', Type='txt'):
        file = name + "." + Type

        dateCreated = time.asctime()
        
        with open(file, 'w') as f:
            f.write('\t[FILE: ' + file + ']\n')
            f.write('\t[DATE CREATED: ' + str(dateCreated)+\
                    ']\n')
            f.write('\t[Title: ' + TITLE + ']\n')
        f.close()

    
    def EditFile(self):
        self.readF()
        file = self.FileName
        bp = str(input('input bullet point type: '))
        with open(file) as f:
            t = f.read()
        f.close()

        pretext = bp
        ind_lvl = 0
        key_commands = ['done', '-->', '<--']

        
        def lastDateMatches(string):
                strStart=t.rfind(string)
                date = t[(strStart+20):(strStart+26)]
                initDate = str(self.InitializeTimeStamp)[4:10]

                if date == initDate:
                    return True
                else:
                    return False


        timestampstring = "TIMESTAMPSTR:  "+\
                          '['+\
                          str(self.InitializeTimeStamp)+\
                          ']'
            
        if not lastDateMatches('TIMESTAMPSTR'):
            t += '\n' + \
                 '\t' + timestampstring + \
                 '\n' + \
                 '\t#####Last Save: [' + \
                 time.asctime() + \
                 ']#####\n\n'

        
        print("""
            to end input: type 'done' or press Ctrl+c
            to indent: type '-->'
            to unindent: type '<--'
        """)


                
        while 1:
            
            try:
                
                string = input(str(pretext))

                if string.lower() == 'done':
                    break
                
                elif string == '-->':
                    pretext = '  ' + pretext
                    lvl += 1

                elif string == '<--':
                    if ind_lvl > 0:
                        pretext = pretext[2:]
                        ind_lvl -= 1

                
            except KeyboardInterrupt:
                break

            
            key_match = 3
            for k in key_commands:
                if string == k:
                    key_match -= 1
            if key_match < 3:
                t += ''
            else:
                t += pretext + string + '\n'

        
##        while 1:            
##            try:
##                line = sys.stdin.readline()
##
##            except KeyboardInterrupt:
##                break
##
##            if not line:
##                break
##
##            t += line
##        #Old text input editor

        with open(file, 'w') as f:
            f.write(t)
        f.close()

        with open(file) as f:
            text = f.read()
            self.text = text
        f.close()
            
    def lp(self):
        self.UPL()
        print("##########---FOLDERS---##########")
        for c in self.cpaths:
            print(c)
        print("##########----FILES----##########")
        for c in self.cfiles:
            print(c)


    def help(self):
        print('''

        ##########---Help Section---##########

        InitSetting()
        -Sets specific variables to the initial settings

        UPL()
        -Update Path List: Updates the directory

        readF()
        -Reads the current file, and stores it
        in variable: [text].
        
        sf(New File)
        -Selects a file. This file is stored and saved 
        until a new file is selected.

        cd([file])
        -Changes current directory. If left blank, it will
        return to the original directory. Type '..' to
        move up one level in the directory.

        NewFile(filename, extension=txt)
        -Creates a new file.
        WARNING: IF THE FILE EXISTS, THEN THE ORIGINAL
        WILL BE DELETED

        EditFile()
        -Edits the current file.
        NOTICE: This only works for txt files.

        lp()
        -Lists all folders and files in the current
        directory.

        help()
        -Displays this text...

        ''')



    def __str__(self):
        self.UPL()

        return 'FileName: '+str(self.FileName)+'\n'+\
               'Current Directory: '+str(self.cwd)+'\n'+\
               'Current Files: '+self.cfiles+'\n'+\
               'Current Paths: '+self.cpaths+'\n'
    

    

    
