from tkinter import *
root = Tk()
label1 = Label(root, text = "FirstName")
label2 = Label(root, text = "LastName")

entry1 = Entry(root)
entry2 = Entry(root)#Textfields are called entries in PythonTkinter

label1.grid(row = 0, column = 0) #use grid(row = i, column = j) instead of pack()
label2.grid(row = 1, column = 0)
entry1.grid(row = 0, column = 1)
entry2.grid(row = 1, column = 1)

root.mainloop()