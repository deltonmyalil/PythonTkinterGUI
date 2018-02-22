from tkinter import *

def function1():
    print("Menu item clicked")

root = Tk()
myMenu = Menu(root)
root.config(menu = myMenu)

submenu = Menu(myMenu)
myMenu.add_cascade(label = "File", menu = submenu)
submenu.add_command(label = "Project", command = function1)
submenu.add_command(label = "Save", command = function1)
submenu.add_separator()
submenu.add_command(label = "quit", command = root.quit) #root.quit exits the window

newmenu = Menu(myMenu)
myMenu.add_cascade(label = "Edit", menu = newmenu)
newmenu.add_cascade(label = "Undo", command = function1)

root.mainloop()