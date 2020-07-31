from tkinter import *

root = Tk()

#Creating a Label Widget
'''myLabel1 = Label(root, text="Enter your name:")
myLabel2 = Label(root, text="Enter your age:")

myLabel1.grid(row=0, column = 0)
myLabel2.grid(row=1, column = 0)

myTextl1 = Label(root, text="Answer")
myTextl1.grid(row=0, column = 1)

myTextL2 = Label(root, text="Answer")
myTextL2.grid(row=1, column = 1)'''

###########################
myLabel1 = Label(root, text="Enter your name:")#.grid(row=0, column = 0)#creating a label widget
myLabel2 = Label(root, text="Enter your age:")#.grid(row=1, column = 0)

myTextl1 = Entry(root)#.grid(row=0, column = 1)
myTextL2 = Entry(root)#.grid(row=1, column = 1)

myLabel1.pack()
myLabel2.pack()
myTextl1.pack()
myTextL2.pack()





#myLabel.pack()# Shoving it onto the sreen

root.mainloop()






