from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title", "This is the message")

response = tkinter.messagebox.askquestion("Question1", "Do you like Coffee?")
if response == 'yes':
    print("Here is your coffee")
else:
    print("Here is your tea")

root.mainloop()