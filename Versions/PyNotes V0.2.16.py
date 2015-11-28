#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 11.04.2015
#Version: 0.2.16
#Description: Organize and take notes with PyNotes!


#imports
import os
import sys
import time
import textwrap


#globals
files = []
CPaths = []
#DoNotChange
ORIGINAL_CWD = os.getcwd()


#classes
class PyNotes:
    FileName=None
    MainCwd = None
    cwd = None
    path = None
    cpaths = []
    cfiles = []
    InitializeTimeStamp = None
    version = '0.2.16'
    
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

        # \t is for tab
        print('\t', end='')
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

    def EditFile(self, file='', system=False, message=""):
        #use line numbers in text to go back and edit line
        #will be used with index
        if len(file)>0:
            self.sf(file)
        self.readF(sts=True)
        #this reads from last timestamp, not whole text
        if self.FileName == None:
            return None
        file = self.FileName
        text = self.text

        # Initial Variables
        bp = input('input bullet point: ') #Bullet Point
        try:
            bp = int(bp)
            bp = chr(bp)
        except ValueError:
            bp = str(bp)
            bp = str(bp)
        SaveText = str(input('type(y/n) for TimeStamp text: ')) #controls if last save text is turned on
        savebool = True
        if SaveText == 'n':
            savebool = False
        width = 55
        lenI = 1
        Coding = False
        
        '''
        All indenting and bullet point editing will be
        done and implemented in the GUI version of
        PyNotes, expected to be in version v1.

        IDEA!!!!!
        since the program uses textwrap, which reads and
        edits the text that was inputed...
        use that ability to do bulletpoints/indentation

        this above statement has been officially completed
        as of version 0.1.08.


        ##replace last index[-1] with [-(len(bp))]

        ##implement code key_command, for code input
            this will have no bullet points
            indents will be either 2 or 4
            textwrap will be turned off

        ##add subtitle key_command

        pySlideShow
            clear screen for each slide
            include margins/borders
            -text version
            -PySlides is pygame version

        ##Shorten the read text
            make it in the  past 50 lines
            or in the past 300 characters
            ##or since the last TIMESTAMPSTR

        ##put the timestampstr at before rest of text

        ##Make a new file for the outline.
            this will use the bp pretty much.
            import the new data class, and
            modify so:
                class outliner(data):
                    def EditFile() #this is only
                                   #thing changed

        needs modify previous lines
            erase lines..
            maybe not break on input.........
                This can cause a TON of problems..
                if it is even possible in the first place

        Add SideNote Capability
            if there is something not related to the topic

        Implement a Highlight Mode
            It would make the object more noticible
            try to use fonts or abstract characters            
        
                    
        '''
        
        with open(file) as f:
            t = f.read()
        f.close()
        if not system:
            pretext = bp
            ind_lvl = 0
            key_commands = ['DONE', '-->',
                            '--->', '<---', #user errors
                            '<--', 'CHBP',
                            'TITLELINE', 'SUBTITLE',
                            'CODEMODE', 'CODEEXIT',
                            'BULLETS']

##            user_errors = ['--.', '-..'
##                           ',__', '__.']
##            for u in user_errors:
##                key_commands.append(u)
            
            print("""
            to end input: type 'DONE' or press Ctrl+c
            to indent: type '-->'
            to unindent: type '<--'
            to make title line: type 'TITLELINE'
            to make subtitle line: type 'SUBTITLE'
            to change the bullet point: type 'CHBP'
            to enter Code Input: type 'CODEMODE'
            to exit Code Input: type 'CODEEXIT'
            to see bullet points: type 'BULLETS'
                
            """)
            def specialPoints():
                for i in range(1, 9):
                    print(str(i) + ' = ' + chr(i))
                for i in range(11, 32):
                    print(str(i) + ' = ' + chr(i))
                            
            #This checks if the last time modified was on
            #the same date as the current date..
            #This is to separate your notes by day.
            #It returns true if last modified date is
            #current date.
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
                

                #20-26
                 
            while 1:
                try:
                    if pretext == '':
                        pretext = bp
                        width = 55
                        
                    string = input(str(pretext))
                    lenI = len(bp)

                    
                    #key_commands
                    if string.lower() == 'done':
                        break
                        
                    elif string == '-->' or string == '--->':
                        spaces = ' '
                        for i in range(lenI):
                            spaces += ' '
                        pretext = spaces + pretext
                        ind_lvl += 1
                        width -= len(spaces) #2

                    elif string == '<--' or string == '<---':
                        if ind_lvl > 0:
                            pretext = pretext[lenI+1:]
                            ind_lvl -= 1
                            width += len(spaces) #2

                    elif string == 'CHBP':
                        char = input('input bullet point: ')
                        try:
                            char = int(char)
                            newbp = chr(char)
                        except ValueError:
                            char = str(char)
                            newbp = str(char)
                        pretext = pretext[:-lenI] + newbp
                        bp = newbp
                            
                    elif string == 'TITLELINE':
                        ind_lvl = 0
                        pretext = ''
                        string2 = input('input title: ')
                        string = "--[" + string2 + "]--"
                    elif string == 'SUBTITLE':
                        ind_lvl = 0
                        pretext = ''
                        string2 = input('input subtitle: ')
                        string = "[" + string2 + "]"

                    elif string == 'CODEMODE':
                        ind_lvl = 0
                        pretext = '  '
                        Coding = True
                        savedBp = bp
                        bp = ''
                    elif string == 'CODEEXIT':
                        Coding = False
                        pretext = ''
                        bp = savedBp
                        
                    elif string == 'BULLETS':
                        specialPoints()

                    

                    elif len(string) > width:
                        #this is breaking indentation
                        #FIND IT!!!!!
                        # .....Found it.. yay
                        lines = textwrap.wrap(string, width)
                        new_string = ''
                        for l in lines:
                        
                            index = lines.index(l)
                            if index == len(lines)-1:
                                new_string += l + \
                                              '\n'
                            else:
                                new_string += l + \
                                              '\n' + \
                                              pretext[:-lenI] + \
                                              ' '

                        string = new_string
                            
                    
                    #does not write key commands
                    key_match = 3
                    for k in key_commands:
                        if string == k:
                            key_match -= 1
                    if key_match < 3:
                        t += ''
                    else:
                        if len(string) > width:
                            t += pretext + string
                        else:
                            t += pretext + string + '\n'

                    
                except KeyboardInterrupt:
                    break
                    
            else:
                t += 'SYSTEM\t'+message+'\n'



        #This shows the time of the last save,
        #if savebool is true.

        if savebool:
            t += '\n\tLast Save: [' + \
                 time.asctime() + \
                 ']\n\n'
            

        #Ask to backup file
        backupText = str(input('BackUp File?(y/n)'))
        backup = False
        if backupText.lower() == 'y' or backupText.lower() == 'yes':
            backup = True
            
        #Save File
        with open(file, 'w') as f:
            f.write(t)
        f.close()

        #Write to file backup location too, if backup=True
        if backup:
            currentCwd = self.cwd
            os.chdir(self.MainCwd)
            with open('Backup/'+file, 'w') as f:
                f.write(t)
            f.close()
            os.chdir(currentCwd)
            print("Backup Successful!")

        #Set current text to text in the file
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
        return 'File Name: ' + str(self.FileName) + '\n' +\
               'Main cwd: ' + str(self.MainCwd) + '\n' +\
               'Current cwd: ' + str(self.cwd) + '\n' +\
               'Current path: ' + str(self.path) + '\n' +\
               'Time Stamp: ' +\
               str(self.InitializeTimeStamp) + '\n' +\
               'Version: v' + str(self.version) + '\n'
               
        

    
        


#functions
def UFL(folder="Files\\"):
    global files
    files = list()
    cwd = os.getcwd()
    path = os.path.join(cwd, folder)
    #print("------------FILES------------")
    for c in os.walk(path).__next__()[2]:
        #print(c)
        files.append(c)

def UPL():
    global CPaths
    CPaths = list()
    cwd = os.getcwd()
    path = os.path.join(cwd)
    print("##########---FOLDERS---##########")
    for c in os.walk(path).__next__()[1]:
        print(c)
        CPaths.append(c)
    print("##########----FILES----##########")
    for c in os.walk(path).__next__()[2]:
        print(c)
        CPaths.append(c)


def startUp():
    def titleDisplay():
        for i in range(8):
            print()
        print("""
        --------------------
        Welcome to PyNotes V0.2.16
        
        This program is used to take notes
        and save them to a simple text document
        
        Author: Max Ferney
        if you have any questions or concerns
        about this program, you may email
        me at maxferney@gmail.com please set
        the title of the subject to PyNotes, so
        I know what it is. Thank you.

        This is now on Github!!!
        so everything above is done through github..
        or something like that, you can email me
        if you would like to though still.
        (Use FileManager to start)
        --------------------
        """)
        for i in range(4):
            print()
    titleDisplay()


startUp()
FileManager = PyNotes()
#(You can rename filemanager to a shorter variable,
# I use the variable 'a')


#This is only if you have subdirectories in your files
#folder

def quickstart(path, system=False, file=None):
    global a
    if not system:
        a = PyNotes()
        a.cd('Files')
        a.cd(path)
    else:
        a = PyNotes()
        a.cd('Files')
        a.cd(path)
        a.sf(file)
        a.EditFile()
    

def notes():
    
    
    #Wed Oct 28 08:34:13 2015
    day = time.asctime()[:3]
    hour = time.asctime()[11:13]
    minute = time.asctime()[14:16]
    hour = int(hour)
    minute = int(minute)

    def is_in_time(days=['mon', 'wed', 'fri'],
                   starttime='08:00',
                   endtime='08:50',
                   minutes_before_start=30):
        pass
        

    #classes
    CSCI = False
    PSYC = False
    MUST = False
    WRIT = False
    
    #Computer Science / Psychology
    if day.lower() == 'tue' or day.lower() == 'thu':
##        if (int(hour) >= 12 and int(minute) >= 15) and \
##           (int(hour) <= 13 and int(minute) <= 50):
##            #csci
##            quickstart('CSCI', True, 'csci207_notes01.txt')
        # Computer Science
        if int(hour) >= 12 and int(hour) <= 13:
            if hour == 12:
                if minute >= 15 and minute <= 59:
                    CSCI = True
            if hour == 13:
                if minute >= 00 and minute <= 45:
                    CSCI = True

        # Psychology
        if int(hour) >= 16 and int(hour) <= 18:
            if hour == 16:
                if minute >= 45 and minute <= 59:
                    PSYC = True
            if hour == 17:
                if minute >= 00 and minute <= 59:
                    PSYC = True
            if hour == 18:
                if minute >= 00 and minute <= 15:
                    PSYC = True
        
                
            
                    
##        elif ((int(hour) == 16 and int(minute) >= 45) or \
##             (int(hour) >= 17 and int(minute) >= 00)) and \
##             (int(hour) <= 18 and int(minute) <= 15):
##            #psyc
##            pass
    elif day.lower() == 'mon' or \
         day.lower() == 'wed' or \
         day.lower() == 'fri':
        
        if int(hour) >= 7 and int(hour) <= 8:
            if hour == 7:
                if minute >= 45 and minute <= 59:
                    WRIT = True
            if hour == 8:
                if minute >= 00 and minute <= 50:
                    WRIT = True
        
##        if ((int(hour) >= 7 and int(minute) >= 50) and \
##            (int(hour) <= 8 and int(minute) <= 50)):
##            #writ
##            pass
        elif day.lower() == 'mon' and \
             day.lower() != 'wed' and \
             day.lower() != 'fri':
            if int(hour) >= 16 and int(hour) <= 19:
                if hour == 16:
                    if minute >= 45 and minute <= 59:
                        MUST = True
                if hour == 17 or \
                   hour == 18:
                    if minute >= 00 and minute <= 59:
                        MUST = True
                if hour == 19:
                    if minute >= 00 and minute <= 45:
                        MUST = True
##            if ((int(hour) >= 16 and int(minute) >= 45) and \
##                (int(hour) <= 21 and int(minute) <= 50)):
##                #must
##                pass

    #Start Notes
    if CSCI:
        quickstart('CSCI', True, 'csci207_notes01.txt')
    elif PSYC:
        quickstart('PSYC', True, 'PsychologyNotes_01.txt')
    elif WRIT:
        quickstart('WRIT', True, 'Writ notes 2.txt')
    elif MUST:
        quickstart('MUST', True, 'Music_appr.txt')
    else:
        print("NOT VALID CLASS TIME")
        #turn this into a raise error, possibly
