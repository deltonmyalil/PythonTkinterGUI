#They grow with the size of the window when maximized, restored etc

from tkinter import *

root = Tk()

label1 = Label(root, text = "First", bg = "Red", fg = "White") #fg is for foreground or text color and bg is for background color
label1.pack(fill = X) #Fill in X axis ie horizontally when resized, Side is set to TOP by default

label2 = Label(root, text = "Second", bg = "Blue", fg = "White")
label2.pack(side = LEFT, fill = Y) #Fill in Y axis ie resize vertically, side has to be mentioned for fill to take effect
root.mainloop()