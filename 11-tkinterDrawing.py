from tkinter import *

root = Tk()
canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

newline = canvas.create_line(0,0,50,100) # line from (0,0) to (100,100)
otherline = canvas.create_line(10,10,100,100, fill = "Green")

root.mainloop()
