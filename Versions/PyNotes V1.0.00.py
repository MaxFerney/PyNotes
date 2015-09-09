''' GUI VERSION OF PYNOTES
    This program was originally created
    off of the program pychatGUI.py
    it has been modified, but is used for
    the same purpose as PyNotes. This is
    just the GUI version... That is all...
'''

#Author: Max Ferney
#Date Created: 8.12.2015
#Date Modified: 9.02.2015
#Version: 1.0.00
#Description: Organize and take notes with PyNotes!

print("input name:\n")
name = input('\t')

print("\nclear on enter?(yes/no)")
auto_clear_ask = input('\t')
if auto_clear_ask.lower() == "yes" or auto_clear_ask.lower() == "y":
    auto_clear = True
else:
    auto_clear = False



##print("\nAuto-Update?(yes/no)")
##AU = {"state":False,"AUI":5}
##auto_update_ask = input('\t')
##if auto_update_ask.lower() == "yes" or auto_update_ask.lower() == "y":
##    AU["state"] = True
##    
##    print("\ntime interval(in seconds, min=2, max=20, and default=5)[WIP and not working at moment]:")
##    AUI_ask = input('\t')
##    if int(AUI_ask) < 2 or int(AUI_ask) > 20:
##        AU["AUI"] = 5
##    else:
##        AU["AUI"] = int(AUI_ask)
##    
##else:
##    AU["state"] = False

AU = {"state":False,"AUI":5}
##print("\ngroup chat:")
##c_file_ask = input()
##if c_file_ask == None:
##    c_file = c_file_ask
print()
#from game_menu import GameMenu

import sys
import os
import time
##import pygame
from tkinter import *
root = Tk()
class App(Frame):
    name=""
    autoClear = False
    c_file = 'test'
    chats = []
    chat_buttons = []
    #chat_menus = []
    
##    autoUpdate = False
##    AUI = 5
##    start = 0
##    elapsed = 0
    
    text = None
    def __init__(self, name,
                 autoClear=True,       #autoUpdate=False,AUI=5,
                 master=None):          #all new variables directly before this
        Frame.__init__(self, master)
        self.pack()

        
##        start_group = 'test'
##        if self.c_file == 'DEBUG' or self.c_file == '':
##            self.c_file = 'test'

        
        self.UFL()
        
        self.name = name
        self.autoClear = autoClear
##        self.autoUpdate = autoUpdate
##        self.AUI = AUI

        self.readF()

        self.entrythingy = Entry()
        self.entrythingy.pack()
##        self.entrythingy["yscrollcommand"] = self.text

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("") #this is a variable
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

        
        ''' manually clear text '''
        self.hi_there = Button(self)
        self.hi_there["text"]       = "Clear"
        self.hi_there["fg"]         = "red"
        self.hi_there["command"]    = self.clear_text

        self.hi_there.pack({"side": "left"})

        ''' refresh '''
        self.refresh = Button(self)
        self.refresh["text"]    = "Refresh"
        self.refresh["fg"]      = "green"
        self.refresh["command"] = self.update
        
        self.refresh.pack({"side": "left"})

        ''' Quit '''
        self.QUIT = Button(self)
        self.QUIT["text"] = "Leave Chat"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.leave_chat

        self.QUIT.pack({"side": "left"})

        ''' New Chat '''
        self.NewChat = Button(self)
        self.NewChat["text"] = "New Chat"
        self.NewChat["fg"] = "blue"
        self.NewChat["command"] = self.Make_Chat

        self.NewChat.pack({"side": "left"})
        
        ''' Chats '''
##        self.UFL()
        for c in self.chats:
            
            if c["name"]==self.c_file:
                c["joined"]=True
                c["color"]="green"
                #self.c_file = c["name"]
                
            else:
                c["joined"]=False
                c["color"]="red"
            
            self.chat_buttons.append(self.chat_button(c))
                    
        for cb in self.chat_buttons:
            index = self.chat_buttons.index(cb)
            if cb["text"] == "DEBUG":
                self.chat_buttons[index].configure(state=DISABLED)
            cb.pack({"side": "bottom", "pady": 5})


##        ''' Menu Bar '''
##        menubar = Menu(root)
##
##        self.menu_buttons(self.chats).add_cascade(label="Chats", menu=MENU)
##        menubar.add_cascade(label="chats", menu=self.menu_buttons(self.chats))
##        menubar.add_cascade(label="Chats", menu=MENU)
##            

##        ''' Scroll Bar '''
##        if self.text_window:
##            self.scrlbar = ScrolledText(self, text=self.text)
##            self.scrlbar["yscrollcommand"] = None
##            self.scrlbar.pack({"side": "right",
##                               "expand": True,
##                               "in":master,
##                               "fill":"y",})

##        if autoUpdate:
##            self.start = time.time()
##            self.elapsed = time.time()-self.start
##            if self.elapsed>=AUI:
##                self.start = time.time()
##                self.update()
##                print(str(time.time()))

    


                
    ''' General Functions '''
    def upload_contents(self, string="", mode="user"):
        c_file = self.c_file
        # opens file and saves a text variable
        # this variable is the "old" text
        file = 'Files/'+str(c_file)+'.txt'
        with open(file) as f:
            t = f.read()
        f.close()

        #records text and adds to "old"
        t+=string
        t+="\n"
        
        #saves
        with open(file, 'w') as f:
            f.write(t)
        f.close()

        #text variable is now "read"
        with open(file) as f:
            text = f.read()
            self.text = text
        f.close()

        #updated AFTER text, so text is displayed with it
        if mode == "user":
            self.update()

            #automatically clears text, if clear_text is true
            if self.autoClear:
                self.clear_text()

        if mode == "join":
            self.update()
            #automatically clears text
            self.clear_text()
        
        if mode == "quit":
            self.update()
            self.quit()

    def clear_text(self):
        self.contents.set("")

    def readF(self):
        c_file = self.c_file
        text = self.text
        FileName = 'Files/' + str(c_file) + '.txt'

        
        with open(FileName, 'r') as f:
            text = f.read()
            self.text = text
        f.close()

    def update(self):
        c_file = self.c_file
        file = 'Files/'+str(c_file)+'.txt'
        with open(file) as f:
            display = f.read()
            self.text = display
        f.close()

        print("############UPDATED############")
        print(display)
        print()
        print("---notice---")
        print("When changing chats, make sure to go to main chat first, then your chat. " + \
              "\nYou must do this every time you switch.")


    def UFL(self):
        self.chats = list()
        cwd = os.getcwd()
        path = os.path.join(cwd, "Files\\")
        #print("------------FILES------------")
        for c in os.walk(path).__next__()[2]:
            #print(c)
            self.chats.append({"file":c,
                               "name":str(c)[:-4],
                               "joined":False,
                               "color":"red"})
            for ch in self.chats:
                if ch["name"]==self.c_file:
                    ch["joined"]=True
                    ch["color"]="green"
                    #self.c_file = ch["name"]
                else:
                    ch["joined"]=False
                    ch["color"]="red"

                    

    def chat_button(self, config):
        return Button(self,
                      text=str(config["name"]),
                      fg=str(config["color"]),
                      command=lambda: self.switch_chat(config))

##    def menu_buttons(self, cfglst):
##        menubar = Menu(root)
##        MENU = Menu(self, menubar, tearoff=0)
##        for cfg in cfglst:
##            MENU.add_command(label=str(cfg["name"]),
##                             command=lambda: self.change_chat(cfg))
##
##        return MENU
##        
        
        


    def switch_chat(self, config):
        
        for c in self.chats:
            self.change_color(config)
            index = self.chats.index(c)
            if self.chats[index]["joined"]:
####                if self.chats[index]["name"] == config["name"]:
####                    break
##                if self.chats[index]["name"] != "test":
##                    self.c_file = "test"
                
                
                string = "SYSTEM\tUSER: ["+self.name+"] HAS LEFT THE CHAT"
                self.upload_contents(string, "join")
                self.chats[index]["joined"] = False
                self.chats[index]["color"] = "red"
                
                self.c_file = config["name"]
                
                print("##########################")
                string = "SYSTEM\tUSER: ["+self.name+"] HAS JOINED CHAT: "+self.c_file     #config["name"]
                self.upload_contents(string, "join")
                config["joined"] = True
                config["color"] = "green"
                
        
        
    def change_chat(self, cfg):
        print("button", str(cfg["name"]))
        self.change_color(cfg)


        
    def change_color(self, cfg):
        for cb in self.chat_buttons:
            index = self.chat_buttons.index(cb)
            if cfg["name"] == cb["text"]:
                cfg["color"] = "green"
                cfg["joined"] = True
                self.chat_buttons[index].configure(fg=cfg["color"])
            else:
                cfg["color"] = "red"
                cfg["joined"] = False
                self.chat_buttons[index].configure(fg=cfg["color"])


    def Make_Chat(self):
        filewin = Toplevel(self)
        label = Label(self, text="Chat Name")
        E = Entry(self)
        
        label.pack()
        E.pack()
        
##        def doesExist():
##            for c in self.chats:
##                if c["file"]==file:
##                    return True
##                else:
##                    return False
##        if doesExist():
##            label.configure(text="Error: File Already Exists")
##            E.set("")
##            E = Entry(self)
##            file = str(E.get())+".txt"
            
        def create():
            file = E.get()+".txt"
            with open('Files/'+file, 'w') as f:
                f.write("Welcome to the "+str(file)[:-4]+" chat\n")
            f.close()
                
        Submit = Button(filewin, text="Create", command=create)
        Submit.pack()


        self.UFL()


    ''' chatting '''
    def leave_chat(self):
        string = "SYSTEM\tUSER: ["+self.name+"] HAS LEFT THE CHAT"
        self.upload_contents(string, "quit")

    def join_chat(self):
        string = "SYSTEM\tUSER: ["+self.name+"] HAS JOINED THE CHAT"
        self.upload_contents(string, "join")

    def print_contents(self, event):
        if self.contents.get() == '':
            self.update()
        else:
            string = self.name+": "+self.contents.get()
            self.upload_contents(string, "user")



    ''' return values '''
    def getText(self):
        return self.text

    def values(self):
        self.readF()
        #"auto clear":self.autoClear,
        #"auto update":self.autoUpdate,
        #"auto update interval":self.AUI
        return {"name":self.name,
                "c_file":self.c_file,
                "chats":self.chats}

    
        
        
##    def running(self, event):
##        start = time.time()
##        if not self.autoUpdate:
##            self.autoUpdate = True
##        while True:
##            if self.autoUpdate:
##                elapsed = time.time()-start
##                if elapsed>=self.AUI:
##                    elapsed = 0
##                    start = time.time()
##                    self.update()
##                    #print(str(time.time()))
##            if self.contents.get() == '':
##                break
##            else:
##                break
##            
##        self.autoUpdate = False
    


myapp = App(name, auto_clear)
stats = myapp.values()
height = (len(stats["chats"])*40) + 50
#
# here are method calls to the window manager class
#

strH = str(height)

winsize = "450x"+strH
myapp.master.title("Pychat")
myapp.master.geometry(winsize)
myapp.master.maxsize(1000, 800)

# start the program
myapp.join_chat()
myapp.mainloop()
try:
    root.destroy()
except TclError:
    myapp.leave_chat()
##    try:
##        myapp.leave_chat()
##    except NameError:
##        myapp.leave_chat()

#TclError


