from tkinter import *

class MyButtons:
    def __init__(self,rootOne):
        frame = Frame(rootOne)
        frame.pack()

        self.printButton = Button(frame, text = "Click Here", command = self.printMessage)
        self.printButton.pack()

        self.quitButton = Button(frame, text = "Quit", command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printMessage(self):
        print("Button Clicked")

root = Tk()
b = MyButtons(root)
root.mainloop()