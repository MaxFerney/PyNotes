import os
import time

#used for creating Version Log text files

class VersionLogger:
    version = "0.0.00"
    text = ""
    current_date = time.asctime()
    file = ''

    def __init__(self, version, file='VersionLog.txt'):
        self.version = version
        self.file = file

    def UpdateVersion(self):
        new_version = input("new version: ")
        
    
    
    def inputs():
	done = False
	string = ''
	t = ''
	while string != 'done':
            string = input('*')
	    if string.lower() == 'done':
		done = True
		break
	    t += string + '\n'
	return t



