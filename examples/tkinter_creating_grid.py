from tkinter import *

root = Tk()
for x in range(3):
    for y in range(3):
        frame = Frame(root)
        frame.grid(row = x, column = y)
        button = Button(frame,text=f"Row {x+1}\n Column {y+1}")
        button.pack(padx = 5, pady = 5)


root.mainloop()