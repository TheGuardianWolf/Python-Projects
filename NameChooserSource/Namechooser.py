#import required random module
from random import randrange

from Namelist import *

#GUI Program
import tkinter

lastnamechosen="999999"

class simpleapp_tk(tkinter.Tk):
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        button = tkinter.Button(self,text=u"Draw Name", command=self.RandomSelection)
        button.grid(column=10,row=0)

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,anchor="w", fg="black", bg="white")
        label.grid(column=0,row=0,columnspan=10,sticky="EW")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        #Selection

        self.update()
        self.geometry("300x25")  

    def RandomSelection(self):
        global lastnamechosen
        length=len(names)
        randomiser=int(randrange(0,len(names)))
        while randomiser == lastnamechosen:
            randomiser=int(randrange(0,len(names)))
        if (randomiser == len(names)and randrange(0,50)> 1):
            randomiser=int(randrange(0,len(names)))
        lastnamechosen=randomiser
        self.labelVariable.set(names[randomiser])
        


if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Name Chooser')
    app.mainloop()
