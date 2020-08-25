#Author: Max Ferney
#Date Created: 8.12.2015
#Date Created(GUI): 2.14.2017
#Date Modified: 2.16.2017
#Version: 2.0.02
#Description: Organize and take notes with PyNotes!
#Bugs: 0

#http://code.activestate.com/recipes/578569-text-editor-in-python-33/

from tkinter import *
from tkinter.filedialog   import asksaveasfilename
from tkinter.simpledialog import askstring
from tkinter.messagebox import askokcancel
import tkinter.scrolledtext as ScrolledText

################################################################################

class SimpleEditor():

    def __init__(self, parent=None, file=None): 
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Save',  command=self.onSave).pack(side=LEFT)
        Button(frm, text='Cut',   command=self.onCut).pack(side=LEFT)
        Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
        Button(frm, text='Find',  command=self.onFind).pack(side=LEFT)
        Quitter(frm).pack(side=LEFT)
        super().__init__()
        self.text['font'] = 'courier', 9, 'normal'
        self.target = ''

    def onSave(self):
        filename = asksaveasfilename(defaultextension='.txt',
                                     filetypes=(('Text files', '*.txt'),
                                                ('Python files', '*.py *.pyw'),
                                                ('All files', '*.*')))
        if filename:
            with open(filename, 'w') as stream:
                stream.write(self.gettext())

    def onCut(self):
        self.clipboard_clear()
        self.clipboard_append(self.text.get(SEL_FIRST, SEL_LAST))
        self.text.delete(SEL_FIRST, SEL_LAST)

    def onPaste(self):
        try:
            self.text.insert(INSERT, self.selection_get(selection='CLIPBOARD'))
        except TclError:
            pass

    def onFind(self):
        self.target = askstring('SimpleEditor', 'Search String?',
                                initialvalue=self.target)
        if self.target:
            where = self.text.search(self.target, INSERT, END, nocase=True)
            if where:
##                print(where)
##                self.text.tag_remove(SEL, '1.0', END)
                pastit = '{}+{}c'.format(where, len(self.target))
                self.text.tag_add(SEL, where, pastit)
                self.text.mark_set(INSERT, pastit)
                self.text.see(INSERT)
                self.text.focus()

################################################################################

class ScrolledText(Frame):

    def __init__(self, parent=None, text='', file=None):
        super().__init__(parent)
        self.pack(expand=YES, fill=BOTH)
        self.makewidgets()
        self.settext(text, file)

    def makewidgets(self):
        sbar = Scrollbar(self)
        self.text = Text(self, relief=SUNKEN, wrap=WORD)
        sbar['command'] = self.text.yview
        self.text['yscrollcommand'] = sbar.set
        sbar.pack(side=RIGHT, fill=Y)
        self.text.pack(side=LEFT, expand=YES, fill=BOTH)

    def settext(self, text='', file=None):
        if file:
            with open(file, 'r') as stream:
                text = stream.read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()

    def gettext(self):
        return self.text.get('1.0', END + '-1c')

################################################################################

class Quitter(Frame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)

    def quit(self):
        if askokcancel('Verify exit', 'Really quit?'):
            self._root().destroy()

################################################################################

if __name__ == '__main__':
    SimpleEditor(file=sys.argv[1] if len(sys.argv) > 1 else None).mainloop()



















##import tkinter
##from tkinter import *
##import tkinter.scrolledtext as ScrolledText
##import tkinter.filedialog as tkFileDialog
##import tkinter.messagebox as tkMessageBox
##
##root = tkinter.Tk(className=" Just another Text Editor")
##textPad = ScrolledText.ScrolledText(root, width=100, height=80)
##
### create a menu & define functions for each menu item
##
##def open_command():
##        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
##        if file != None:
##            contents = file.read()
##            textPad.insert('1.0',contents)
##            file.close()
##
##def save_command():
##    file = tkFileDialog.asksaveasfile(mode='w',defaultextension=".txt")
##    if file != None:
##    # slice off the last character from get, as an extra return is added
##        data = textPad.get('1.0', END+'-1c')
##        file.write(data)
##        file.close()
##        
##def exit_command():
##    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
##        root.destroy()
##
##def about_command():
##    label = tkMessageBox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve \n Now owned by Max Ferney")
##        
##
##def dummy():
##    print("I am a Dummy Command, I will be removed in the next step")
##
##    
##
##menu = Menu(root)
##root.config(menu=menu)
##filemenu = Menu(menu)
##menu.add_cascade(label="File", menu=filemenu)
##filemenu.add_command(label="New", command=dummy)
##filemenu.add_command(label="Open...", command=open_command)
##filemenu.add_command(label="Save", command=save_command)
##filemenu.add_separator()
##filemenu.add_command(label="Exit", command=exit_command)
##helpmenu = Menu(menu)
##menu.add_cascade(label="Help", menu=helpmenu)
##helpmenu.add_command(label="About...", command=about_command)
##
###
##textPad.pack()
##root.mainloop()
