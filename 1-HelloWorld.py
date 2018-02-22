from tkinter import *

root = Tk() #created an object root of the builtIn class Tk
label1 = Label(root,text = "Hello Universe") #created a label1 using method Label with object of Tk and text HEllo as parameters
label1.pack() #packed the label inside the window
root.mainloop() #So that the winndow will run in a loop until closed