from tkinter import *

root = Tk()
display = Entry(root)
display.grid(row=1, columnspan=6)
root.geometry("125x200")

counter = 1

for x in range(3):
    for y in range(3):
        button = Button(root, text=counter,width=3,height=3)
        button.grid(row=x+2,column=y)
        counter+=1

root.mainloop()
