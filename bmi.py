from tkinter import*#standard GUI(Graphical User Interface)package

root = Tk()
root.geometry("1350x650+0+0")
root.resizable(0,0)
root.title("BMI Calculator")

var1 = DoubleVar()
var2 = DoubleVar()

Tops = Frame(root,width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)
f1 = Frame(root, width=600, height = 600, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width = 300,height = 700, bd=8, relief="raise")
f2.pack(side=RIGHT)

fla = Frame(f1, width =600, height =200, bd=20, relief="raise")
fla.pack(side=TOP)
f1b = Frame(f1, width = 600, height = 200, bd=20, relief ="raise")
f1b.pack(side=TOP)
#########################TITLE######
lblTitle=Label(Tops, text="       BMI Calculator Program  ",padx=16,pady=16,bd=16,
                fg="#000000", font=('arrial', 54,'bold'),
                bg="light green", relief = 'raise', width = 32, height = 1)
lblTitle.pack()
##############SCALE OF WEIGHT
lblheight =Label(fla, text ="Select Weight in Kilogramas ", font=('arial', 20, 'bold'), bd=20).grid(row = 0, column=0)
Bodyweight = Scale(fla,variable =var1, from_ = 1, to =500, length=880, tickinterval=30, orient= HORIZONTAL)
Bodyweight.grid(row = 1, column=0)
###################TEXT
lblheight = Label(f1b, text= "Enter Height in Meters Square", font =('arial',20, 'bold'), bd=20).grid(row = 0, column =0)
txtheight = Entry(f1b, textvariable = var2, font=('arial', 16, 'bold'),bd=16, width=22, justify='center')
txtheight.grid(row = 1,column=0)
##############
lblBMIResult = Label(f1b, padx =16, pady=16, bd=16,
                     fg="#000000", font=('arial',30,'bold'),
                     bg="light green", relief ='sunk', width = 34, height = 1)
lblBMIResult.grid(row =2, column=0)
####################
lblBMITable = Label(f2,font=('arial',20,'bold'), text="BMI Table").grid(row = 0, column = 0)
txtlblBMITable = Text(f2, height = 12, width = 38, bd=16, font=('arial',12,'bold'))
txtlblBMITable.grid(row=1,column=0)


root.mainloop()#shows the main panel
