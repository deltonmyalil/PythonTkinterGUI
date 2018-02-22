from tkinter import*
root = Tk()
newFrame = Frame(root) #NewFrame is in the root window
newFrame.pack()
nextFrame = Frame(root) #NextFrame is in the root window
nextFrame.pack(side = BOTTOM) #pack it at the bottom of the root, BOTTOM is a constant
button1 = Button(newFrame,text = "Click Here",fg = "Red") # fg means foreground color
button2 = Button(nextFrame,text = "Click Next", fg = "Blue")
button1.pack()
button2.pack()
root.mainloop()