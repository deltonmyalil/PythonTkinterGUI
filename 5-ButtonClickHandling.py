from tkinter import *

root = Tk()

def toDoWhenClicked():
    print("You clicked me")

button1 = Button(root, text = "click here", command = toDoWhenClicked()) #command is assigned to the function name that should be invoked when you click it
button1.pack()

root.mainloop()

'''note that it is command = toDoWhenClicked
        and not command = toDoWhenClicked()
                if this is the case, the function will be invoked by default without clicking
'''