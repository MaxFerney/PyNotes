#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 8.24.2016
#Version: 0.3.09.1
#Description: Organize and take notes with PyNotes!
#Bugs: 0


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
    MainCwd = 'C:\\Users\\lisaf_000\\Desktop\\Python\\PyNotes'
    cwd = None
    path = None
    cpaths = []
    cfiles = []
    InitializeTimeStamp = None
    version = '0.3.09.1'
    lastIndex = 0
    previousIndex = 0
    last_indented_line = 0
    last_indented_level = 0

    #time variable
    
    text = ""

    def __init__(self):
        #self.MainCwd = os.getcwd()
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

    def readF(self, sts=False, Display=True):
        #sts = Since Time Stamp
        text = self.text

        AllLines=True
        lines=200
        
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
                
        if sts:
            lastIndex = text.rfind('TIMESTAMPSTR')
            DisplayText = text[lastIndex:]
            if Display:
                # \t is for tab before time
                print('\t', end='')
                
        else:
            DisplayText = self.text

        self.text = DisplayText
        if Display:
            print(DisplayText)

    def sf(self, file, show_text=True, alltext=False):
        self.UPL()
        self.FileName = file
        if not show_text:
            self.readF(sts=True, Display=False)
        else:
            if alltext:
                self.readF(sts=False, Display=True)
            else:
                self.readF(sts=True, Display=True)

    def cd(self, newpath=''):
        if len(str(newpath))==0 or str(newpath)=="" or str(newpath)=='sysmain':
            newpath = self.MainCwd
        elif str(newpath)[-1] == '/':
            newpath = str(newpath)[:-1]
        os.chdir(newpath)
        self.cwd = os.getcwd()
        self.path = os.path.join(self.cwd)   

    def search(self, string='',
               section_length=100,):
        # Initialize Variables
        reset_index = False
        if string == '':
            string=input('string: ')
        stringUpper = string[0].upper() + string[1:]
        stringLower = string[0].lower() + string[1:]
        index = self.text.find(stringUpper, self.lastIndex)
        index2 = self.text.find(stringLower, self.lastIndex)
        
        # Set Index
        if index < index2 and index != -1:
                self.lastIndex = index
        elif index2 < index and index2 != -1:
                self.lastIndex = index2
                

        # Reset Index
        else:
            print('#\n#\n#Message Text Variable: End String\n#\n#')
            print("==========NO RESULTS FOUND==========")
            reset_index = True

        # Printing
        print('\n\t\t-----------substring-----------\n')
        print(self.text[self.lastIndex-section_length:
                        self.lastIndex+section_length])
        print('\n\t\t-----------substring-----------\n')
    
        # Reset Variables / Reset Index
        if not reset_index:
            print(str(self.lastIndex))
            print('#\n#\n#Message Text Variable: Next String\n#\n#')
            self.lastIndex += 1
            print(str(self.lastIndex))
        else:
            self.lastIndex = 0
            print('#\n#\n#Message Text Variable: Reset String\n#\n#')
            reset_index=False
            
    def NewFile(self, name, TITLE=' ', Type='txt'):
        file = name + "." + Type
        dateCreated = time.asctime()
        page_top = ''
        for i in range(59):
            page_top+='='
        with open(file, 'w') as f:
            f.write('\n' + page_top + '\n')
            f.write('\t[FILE: ' + file + ']\n')
            f.write('\t[DATE CREATED: ' + str(dateCreated)+\
                    ']\n')
            f.write('\t[Title: ' + TITLE + ']\n\n\n')
        f.close()

        self.sf(file, alltext=True)
        print('File Selected')

    def EditFile(self, file='', system=False, message=""):
        def testchar(string):
            try:
                string = int(string)
                string = chr(string)
            except ValueError:
                string = str(string)
            return string

        def adjust_indent(ind_lvl=0,
                          spaces='',
                          width=55,
                          bp='',
                          pretext=''):
            for i in range(ind_lvl):
                spaces += "   "
                width-=3
            pretext = spaces + bp
            return_var = [ind_lvl, spaces, width, bp, pretext]
##            print("IND_LVL: " + str(ind_lvl))
##            print("SPACES:  " + str(len(spaces)))
##            print("WIDTH:   " + str(width))
##            print("BP:      " + str(bp))
##            print("PRETEXT: " + str(pretext))
            return return_var
                



        #if filename variable is used
        if len(file)>0:
            self.sf(file)
        self.readF(sts=True)
        
        #this reads from last timestamp, not whole text
        if self.FileName == None:
            return None
        file = self.FileName
        text = self.text

        # Initial Variables
        print()
        bp = input('input bullet point: ')
        #create predefined variable custom error
        bp = testchar(bp)
        
        #text for saving
        SaveText = str(input('type(y/n) for TimeStamp text: ')) #controls if last save text is turned on
        savebool = False
        if SaveText == 'y':
            savebool = True

        #start from last index
        indent_bool = False
        last_indent_ask = input('start from last indent(y/n): ')
        if last_indent_ask == 'y':
            indent_bool = True

        width = 55
        lenI = 1

        #text commands
        Coding = False
        
        tagging = False
        taggingPretext = ''

        delete_last_line = False
        last_string = ''

        t = ''

        ordering = False
        current_number = 1
##        ind_lvl = 0
        ordered_ind_lvl = 0
        temp_bp = bp
        start_order = False
        
        with open(file) as f:
            t = f.read()
        f.close()
        
        if not system:
            pretext = bp
            ind_lvl = 0
            key_commands = ['DONE', 'CHBP',
                            '--->', '<---',     #user errors
                            '00>', '<00',       #user errors
                            '==>', '<==',       #user errors
                            '--', '<-', '->',   #user errors
                            ',--', '--.',       #user errors
                            '-->>', '<<--',     #user errors
                            '>', '<',           #user errors
                            '--:', ':--',       #user errors
                            '<--', '-->',
                            'TITLELINE', 'SUBTITLE',
                            'CODEMODE', 'CODEEXIT',
                            'BULLETS', 'SIDENOTE',
                            'DELETE_LAST_LINE',
                            'TAGSTRING',
                            'ORDERED',
                            'TIME']
            
            print("""
            to end input: type 'DONE' or press Ctrl+c
            to indent: type '-->'
            to dedent: type '<--'
            to make a tagged string: type 'TAGSTRING'
            to make a sidenote: type 'SIDENOTE'
            to make a highlight: type 'HIGHLIGHT'
            to change the bullet point: type 'CHBP'
            to enter Code Input: type 'CODEMODE'
            to exit Code Input: type 'CODEEXIT'
            to see bullet points: type 'BULLETS'
            to erase last line: type 'DELETE_LAST_LINE'
            to make a list: type 'ORDERED'
            to exit list mode: type 'ORDERED END'
            to check for time remaining: 'TIME'
                
            """)
            # Functions
            def specialPoints():
                for i in range(1, 9):
                    print(str(i) + ' = ' + chr(i))
                for i in range(11, 32):
                    print(str(i) + ' = ' + chr(i))


            def tag_string(system=False,
                           tagstart='blank',
                           tagend='blank',
                           pretext='',
                           lenI=0):
                # Inputs
                if not system:
                    tagstart = input('start tag: ')
                    tagend = input('end tag: ')
                tagstart = testchar(tagstart)
                tagend = testchar(tagend)
                note = input('NOTE: ')
                #Function
                taggingPretext = pretext
                pretext = pretext[:-lenI]
                string = tagstart + tagstart + \
                         ' ' + note + ' ' + \
                         tagend + tagend
                tagging = True
                if len(pretext) + len(string) >= 55:
                    print(pretext + string + '\n')
                else:
                    print(pretext + string)
                variables = [taggingPretext, tagging, string, pretext]
                return variables


            def textwrap_function(string, width, pretext, lenI):
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
                                      '  '

                string = new_string
                variables = [string, width, pretext, lenI]
                return variables

            #this function may be interfering with saving
            def Ordered(bp,
                        ind_lvl,
                        ordered_ind_lvl,
                        current_number,
                        temp_bp,
                        ordering,
                        pretext,
                        start_order,
                        lenI,
                        string,
                        key_commands):

                #fix numbers indentation..
                #fix bp recovery
                
                #Reset
                if start_order:
                    ordered_ind_lvl = ind_lvl
                    temp_bp = bp
##                    print('temp bp: ' + temp_bp)
##                    print('\n--Ordering Start--\n')
                    start_order = False
                    ordering = True
                #Exit
                elif (ind_lvl < ordered_ind_lvl and ordering) or \
                     (string == 'ORDERED END'): #mod
                    ordering = False
                    current_number = 1
                    lenI = len(bp) #this fixes the code.
                    bp = temp_bp
##                    print('\n--ind_lvl < ordered list--\n')
                    pretext = pretext[:-lenI] + bp
                #Indent
                elif ind_lvl > ordered_ind_lvl and ordering:
                    ordering = True
                    bp = ' -'
##                    print('\n--l > ordered list--\n')
                    pretext = pretext[:-lenI] + bp
                #Increase Number
                elif ind_lvl == ordered_ind_lvl and ordering:
                    key = False
                    for k in key_commands:
                        if string == k:
                            key=True
                    if not key:
                        current_number += 1
                    bp = str(current_number) + ')'
##                    print('\nind_lvl = ordered list\n')
                    pretext = pretext[:-lenI] + bp

                variables = [bp,
                             ind_lvl,
                             ordered_ind_lvl,
                             current_number,
                             temp_bp,
                             ordering,
                             pretext,
                             start_order,
                             lenI]
                return variables

            #Open File
            with open(file, 'w') as f:
                f.write(t)
            f.close()


            if indent_bool:
                var = adjust_indent(ind_lvl=self.last_indented_level,
                                    spaces='',
                                    width=55,
                                    bp=bp,
                                    pretext=pretext)
                ind_lvl = var[0]
                spaces = var[1]
                width = var[2]
                pretext = var[4]
                
                

                            
            #This checks if the last time modified was on
            #the same date as the current date..
            #This is to separate your notes by day.
            #It returns true if last modified date is
            #current date.
            def lastDateMatches(string):
                strStart=t.rfind(string)
                date = t[(strStart+20-1):(strStart+26-1)]
                initDate = str(self.InitializeTimeStamp)[4:10]

                if date == initDate:
                    return True
                else:
                    return False
                    

            timestampstring = "TIMESTAMPSTR: "+\
                              ' '+\
                              str(self.InitializeTimeStamp)+\
                              ' '
            
            if not lastDateMatches('TIMESTAMPSTR'):
                long_line = ''
                for s in range(54):
                    long_line += '+'
                t += '\n' + long_line
                t += '\n' + \
                     '\t' + timestampstring + \
                     '\n' + \
                     '\tLast Save:     ' + \
                     time.asctime() + \
                     ' \n'
                t += long_line + '\n\n\n'

         
            while 1: 
                try:
                    if pretext == '' :
                        pretext = bp
                        width = 55

                    elif tagging:
                        tagging = False
                        pretext = taggingPretext

                    elif ordering:
##                        bp = str(current_number) + ')'
##                        pretext = pretext[:-lenI] + bp
                        var = Ordered(bp,
                                      ind_lvl,
                                      ordered_ind_lvl,
                                      current_number,
                                      temp_bp,
                                      ordering,
                                      pretext,
                                      start_order,
                                      lenI,
                                      string,
                                      key_commands)
                        bp = var[0]
                        ordered_ind_lvl = var[2]
                        current_number = var[3]
                        temp_bp = var[4]
                        ordering = var[5]
                        pretext = var[6]


                        
                        
                        
                    string = input(str(pretext))
                    lenI = len(bp)

                    
                    
                    #key_commands
                    if string.lower() == 'done':
                        break
                        
                    elif string == '-->' or \
                         string == '--->' or \
                         string == '->':
                        spaces = '  '
                        for i in range(lenI):
                            spaces += ' '
                        pretext = spaces + pretext
                        ind_lvl += 1
                        width -= len(spaces) #2

                        indent_vars = [pretext,
                                       ind_lvl,
                                       width,
                                       spaces]

                    elif string == '<--' or \
                         string == '<---' or \
                         string == '<-':
                        if ind_lvl > 0:
                            pretext = pretext[lenI+2:]
                            ind_lvl -= 1
                            width += len(spaces) #2

                            indent_vars = [pretext,
                                           ind_lvl,
                                           width,
                                           spaces]

                    elif string == 'CHBP':
                        char = input('input bullet point: ')
                        newbp = testchar(char)
                        pretext = pretext[:-lenI] + newbp
                        bp = newbp
                            
                    elif string == 'TITLELINE':
                        ind_lvl = 0
                        pretext = ''
                        string2 = input('input title: ')
                        string = "--[" + string2 + "]--"
                        print(string)
                    elif string == 'SUBTITLE':
                        ind_lvl = 0 #change this...do tagstring for this
                        pretext = ''
                        string2 = input('input subtitle: ')
                        string = "[" + string2 + "]"
                        print(string)

                    elif string == 'CODEMODE':
                        ind_lvl = 0
                        pretext = '  '
                        Coding = True
                        savedBp = bp
                        bp = ' >'
                    elif string == 'CODEEXIT':
                        Coding = False
                        pretext = ''
                        bp = savedBp
                        
                    elif string == 'BULLETS':
                        specialPoints()

                    elif string == 'TIME':
                        timevar=time.asctime()
                        print('---'+str(timevar)[11:19]+'---')

                    elif string == 'TAGSTRING':
                        var = tag_string(pretext=pretext,
                                         lenI=lenI)
                        taggingPretext = var[0]
                        tagging = var[1]
                        string = var[2]
                        pretext = var[3]
                    elif string == 'SIDENOTE':
                        var = tag_string(True,
                                         "<>", "<>",
                                         pretext=pretext,
                                         lenI=lenI)
                        taggingPretext = var[0]
                        tagging = var[1]
                        string = var[2]
                        pretext = var[3]
                    elif string == 'HIGHLIGHT':
                        var = tag_string(True,
                                         chr(4), chr(4),
                                         pretext=pretext,
                                         lenI=lenI)
                        taggingPretext = var[0]
                        tagging = var[1]
                        string = var[2]
                        pretext = var[3]

                    elif string == 'DELETE_LAST_LINE':
                        t = t[0:-len(last_string)]
                        print(pretext[:lenI] +\
                              'deleted string:' +\
                              last_string)

                    elif string == 'ORDERED':# or ordering:
                        if not ordering:
                            start_order = True
                            bp = temp_bp

##                        print('\nordering from string')
                        ordering = True
                        if ordering:
                            var = Ordered(bp,
                                          ind_lvl,
                                          ordered_ind_lvl,
                                          current_number,
                                          temp_bp,
                                          ordering,
                                          pretext,
                                          start_order,
                                          lenI,
                                          string,
                                          key_commands)
                            bp = var[0]
                            ind_lvl = var[1]
                            ordered_ind_lvl = var[2]
                            current_number = var[3]
                            temp_bp = var[4]
                            ordering = var[5]
                            pretext = var[6]
                            start_order = var[7]
                            lenI = var[8]

                    elif string == 'ORDERED END':
                        ordering = False
##                        bp = temp_bp #this breaks it
                        

                        
                    #This should be last conditional
                    elif len(string) > width:
                        var = textwrap_function(string, width, pretext, lenI)
                        string = var[0]
                        width = var[1]
                        pretext = var[2]
                        lenI = var[3]
                        
                            
                    
                    #does not write key commands
                    key_match = 3
                    self.last_indented_line = lenI
                    self.last_indented_level = ind_lvl
                    
                    for k in key_commands:
                        if string == k:
                            key_match -= 1
                            
                    if key_match < 3:
                        t += ''
                        

                    #finalizes text variable "t"
                    else:
                        if string == '':
                            t += '\n'
                            last_string = '\n'
                        elif len(string) > width:
                            t += pretext + string
                            last_string = pretext + string
                        else:
                            t += pretext + string + '\n'
                            last_string = pretext + string + '\n'

                #Break Loop    
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

    def bugs(self):
        print('''

            ------Bugs------
            01  ###FIXED###
                Indentation with numbered bullets
                
                getting rid of it breaks numbered indent
                    but fixes overall indent
                keeping it breaks overall indent
                    but fixes numbered indent

            02
                Saved Indent
                    not tested for bullet points longer
                     than one character long


            ''')


    def VersionLog(self):
        print('''
        All indenting and bullet point editing will be
        done and implemented in the GUI version of
        PyNotes, expected to be in version v1.

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

        ##needs modify previous lines
            erase lines..
            maybe not break on input.........
                This can cause a TON of problems..
                if it is even possible in the first place

        ##Add SideNote Capability
            if there is something not related to the topic

        #<REVISIT> Implement a Highlight Mode(
            It would make the object more noticible
            try to use fonts or abstract characters
            try using Colorama
                (only works in system console)

            Use Error Text Colors, special colors.
                needs to make a custom font for this

            #use <>[]{}()//\\||(make tags)

        0.3.02(incomplete)
        AUTOSAVE
            an autosave feature to pretty much run the
            editfile function multiple times.
                editFile(inloop=False):
                    ...
                    editFile(inloop=True)
                    ...
        0.3.05
        Implement Search feature
            display all TITLELINEs
            add tags
            allow the user to search for a title/tags
            

        Look into Ipython/jupyter
            ipython is a website for Jupyter
        
        ###Custom Made Warning    
        import warnings as w
        >>> w.showwarning("message", Warning, "mod", 21)



        Add a spell checker feature
            This will be able to edit everything up to
            the top
            Use a text file for reference, maybe one for
            each topic or study.
                place a text file in the corresponding
                subject

        
        ##Add a command to entirely delete the above line
            make it easy not to mistake it, or call it
            accidentally
        look for a bullet point, so that other lines
        can be deleted


        Create a few custom errors for more specific
            error handling
            predefined variables in function
                bullet point, save


        0.3.04
        TextWrap Function
        Hightlight and sidenote are pretty much identical.
            Make it a function, maybe with the textwrap
            function.

        0.3.03
        Allow subtitle to be indented

        0.3.05.1    
        add a numbered bullet point function
            input number of bullets
        self.NewFile() now selects the file when created
            
        0.3.05
        Simplified self.readF() function
            got rid of useless code

        0.3.06
        add bug tracker

        0.3.06.1 (planned)
        Raise an error where the bug is.

        0.3.08
        Continue from last indent.
            use for frequently saving while taking notes
            (since it kept crashing while note taking)

        0.3.09
        Fall 2016 Semester

        0.3.09.1 
        Include a time for classes
            current time, time until end
            implement this with notes function
            #or time function with editfile.
        0.3.09.2
        give editfile a "class" mode
            -will determine time remaining
                
            
        
        
                     
        ''')


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
        
        sf(filename)
        -Selects a file. This file is stored and saved 
        until a new file is selected.

        cd(path)
        -Changes current directory. If left blank, it will
        return to the original directory. Type '..' to
        move up one level in the directory.

        NewFile(filename, title, extension=txt)
        -Creates a new file.
        WARNING: IF THE FILE EXISTS, THEN THE ORIGINAL
        WILL BE DELETED

        EditFile()
        -Edits the current file.
        NOTICE: This only works for txt files.

        lp()
        -Lists all folders and files in the current
        directory.

        search(string='',display_section=100)
        -Search for a string. Can have a set amount of
        characters displayed on both sides of the string.
        display_section is characters on both sides
        displayed.

        bugs()
        -Displays a list of current bugs in the code
        

        help()
        -How did this get here

        ''')

    def __str__(self):
        return '---------File Name: ' + str(self.FileName) + '\n' +\
               '---------Main cwd: ' + str(self.MainCwd) + '\n' +\
               '---------Current cwd: ' + str(self.cwd) + '\n' +\
               '---------Current path: ' + str(self.path) + '\n' +\
               '---------Time Stamp: ' +\
               str(self.InitializeTimeStamp) + '\n' +\
               '---------Version: v' + str(self.version) + '\n' +\
               '---------Version Log: ' + '\n'
               
        

    
        


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
        Welcome to PyNotes V0.3.09.1
        
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
        --------------------

        for help, type py.help()
        """)
        for i in range(4):
            print()
    titleDisplay()


startUp()
py = PyNotes()


#This is only if you have subdirectories in your files
#folder

def quickstart(path, system=False, file=None):
    global py
    
    py = PyNotes()
    py.cd()
    py.cd('Files')
    py.cd(path)
    if not system:
        pass
    if system:
        #this is reading it twice
        py.sf(file, show_text=False) #this fixes it
        py.EditFile()
    
    

def notes():
    
    
    #Wed Oct 28 08:34:13 2015
    day = time.asctime()[:3]
    hour = time.asctime()[11:13]
    minute = time.asctime()[14:16]
    str_time = time.asctime()[11:16]
    
    day = day.lower()
    hour = int(hour)
    minute = int(minute)


    def convert_time(time='08:00'):
        time_hour = int(time[0:2])
        time_min = int(time[3:])

        minutes = 0
        minutes += (time_hour * 60) + time_min

        return minutes
        

    def is_in_time(days=['mon', 'wed', 'fri'],
                   starttime='08:00',
                   endtime='08:50',
                   minutes_before_start=30):
        
        start_minutes = convert_time(starttime)
        current_minutes = convert_time(str_time)
        end_minutes = convert_time(endtime)
        
        for d in days:
            if day == d:
                if current_minutes >= (start_minutes - minutes_before_start) and \
                   current_minutes <= end_minutes:
                    return True
                else:
                    return False

    #classes
    MATH = False
    ECON = False
    PHIL = False
    HMXP = False

    #Math
    if is_in_time(['mon', 'wed'],'09:30','10:45',20):
        MATH = True
    #Economics
    elif is_in_time(['tue', 'thu'],'14:00','15:15',20):
        ECON = True
    #Philosophy
    elif is_in_time(['wed'],'14:00','15:15',20):
        PHIL = True
    #Human Experience
    elif is_in_time(['tue', 'thu'],'17:00','18:15',20):
        HMXP = True

    #Start Notes
    if MATH:
        quickstart('MATH', True, 'Math101.txt')
    elif ECON:
        quickstart('ECON', True, 'Econ103.txt')
    elif PHIL:
        quickstart('PHIL', True, 'Phil101.txt')
    elif HMXP:
        quickstart('HMXP', True, 'Hmxp102.txt')
    else:
        print("you are not in class right now.")
        print("use: quickstart(path) to see notes.")
        


    
    
    

