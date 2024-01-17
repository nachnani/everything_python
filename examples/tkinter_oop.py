from tkinter import *

class Demo:

    def __init__(self, root1):
        frame = Frame(root1)
        frame.pack()

        self.printbutton = Button(frame,text="Click Here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack()

    def printmessage(self):
        print("Button Clicked!")


root = Tk()

d = Demo(root)

root.mainloop()