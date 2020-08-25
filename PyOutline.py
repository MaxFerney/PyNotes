import os
import sys
import time
import textwrap

from data import Data
"""
used for outlining. this was originally
supposed to be a part of pynotes, but made it too long.
I decided to write it in an entirely different program.

"""

class Outliner(Data):



    def EditFile(self):
        self.readF()
        file = self.FileName
        #bp = str(input('input bullet point type: '))
        bp = ' '
        with open(file) as f:
            t = f.read()
        f.close()

        string = ' '
        pretext = ' '
        level = 0
        key_commands = ['done',
                        '-->', '<--',
                        '--.', ',--', #user typos
                        '__>', '<__', #user typos
                        'done']
        width = 55
        
##        i0 = i1 = i2 = i3 = i4 = i5 = 0
##        
##        indexes = [i0, i1, i2, i3, i4, i5]
##        currentI = indexes[0]
##        cindent = 0

        
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

        def PretextSpaces(LEVEL):
            spaces = '   '
            chrIndex = Levels[LEVEL]['cIndex']
            for s in range(Levels[LEVEL]['spaces']):
                spaces += ' '
            pretext = spaces+Levels[LEVEL]['bpList'][chrIndex] + '.'
            preLen = len(pretext)
            width = 55
            width -= preLen

        def textwrapper(STRING):
            lines = textwrap.wrap(STRING, width)
            new_string = ''
            for l in lines:
                index = lines.index(l)
                if index == len(lines)-1:
                    new_string += l + \
                                  '\n'
                else:
                    new_string += l + \
                                  '\n' + \
                                  pretext[:-preLen] + \
                                  ' '
            string = STRING = new_string

        
        lvl = level
        #Warning, this only goes up to about
        #20 items per indent, so no value should
        #be > 20
        #indent level goes to about 6 or so
        # I. A. 1. i. a. +

        ''' IDEAS '''
        """
        remake the list levels into a dictionary
        variable:
            LEVELS = {list, current index, [pretext]}
        
        """
        Levels = list()
        lvl0 = ['I', 'II', 'III', 'IV', 'V',
                'VI', 'VII', 'VIII', 'IX', 'X',
                'XI', 'XII', 'XIII', 'XIV', 'XV',
                'XVI', 'XVII', 'XVIII', 'XIX', 'XX']
        LEVEL_00 = {'bpList':lvl0, 'cIndex':0,
                    'spaces':0}
        Levels.append(LEVEL_00)
        lvl1 = ['A', 'B', 'C', 'D', 'E',
                'F', 'G', 'H', 'I', 'J',
                'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S']
        LEVEL_01 = {'bpList':lvl1, 'cIndex':0,
                    'spaces':3}
        Levels.append(LEVEL_01)
        lvl2 = ['01', '02', '03', '04', '05',
                '06', '07', '08', '09', '10',
                '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20']
        LEVEL_02 = {'bpList':lvl2, 'cIndex':0,
                    'spaces':5}
        Levels.append(LEVEL_02)
        lvl3 = ['i', 'ii', 'iii', 'iv', 'v',
                'vi', 'vii', 'viii', 'ix', 'x',
                'xi', 'xii', 'xiii', 'xiv', 'xv',
                'xvi', 'xvii', 'xviii', 'xix', 'xx']
        LEVEL_03 = {'bpList':lvl3, 'cIndex':0,
                    'spaces':8}
        Levels.append(LEVEL_03)
        lvl4 = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't']
        LEVEL_04 = {'bpList':lvl4, 'cIndex':0,
                    'spaces':11}
        Levels.append(LEVEL_04)
        lvl5 = []
        for i in range(20):
            lvl5.append('+')
        LEVEL_05 = {'bpList':lvl5, 'cIndex':0,
                    'spaces':13}
        Levels.append(LEVEL_05)

        
        preLen = len(pretext)
        
        print("""
            to end input: type 'done' or press Ctrl+c
            to indent: type '-->'
            to unindent: type '<--'
        """)


        #[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
        PretextSpaces(level)
        cindex = Levels
        while 1:
            
            try:
                
                spaces = '   '
                chrIndex = Levels[level]['cIndex']
                for s in range(Levels[level]['spaces']):
                    spaces += ' '
                pretext = spaces+Levels[level]['bpList'][chrIndex] + '.'
                    
                preLen = len(pretext)
                string = input(str(pretext))


                if string.lower() == 'done':
                    break
                
                elif string == '-->':
                    if level < 5:
                        level += 1
                        PretextSpaces(level)

                elif string == '<--':
                    if level > 0:
                        Levels[level]['cIndex'] = 0
                        level -= 1
                        PretextSpaces(level)
##                        
##                elif len(string) > width:
##                    lines = textwrap.wrap(string, width)
##                    new_string = ''
##                    for l in lines:
##                        index = lines.index(l)
##                        if index == len(lines)-1:
##                            new_string += l + \
##                                          '\n'
##                        else:
##                            new_string += l + \
##                                          '\n' + \
##                                          pretext[:-Levels[level]['spaces']] + \
##                                          ' '
##                    string = new_string
##                
                else:
                    if level < 5:
                        if chrIndex < 20:
                            Levels[level]['cIndex'] += 1
                            chrIndex = Levels[level]['cIndex']
                        else:
                            print('CANNOT GO FURTHER')
                    else:
                        print('CANNOT GO FURTHER')

                
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

        

        with open(file, 'w') as f:
            f.write(t)
        f.close()

        with open(file) as f:
            text = f.read()
            self.text = text
        f.close()

def quickstart():
    global a
    a = Outliner()
    a.cd('files/tests')
##    a.sf('OutlineTest.txt')

    
            
