#piece of code from
# DJ Oamen 04 august 2016
# youtube: https://www.youtube.com/watch?v=23_93SXvCpc#
from tkinter import*#standard GUI(Graphical User Interface)package

root = Tk()
root.geometry("1350x650+0+0")
root.resizable(0,0)
root.title("BMI Calculator")
###########METHOD###############
def BMI_Call():#Function
    BHeight = float(var2.get())
    BWeight = float(var1.get())
    BMI = str('%.2f' %(BWeight / (BHeight * BHeight)))
    lblBMIResult.config(text=BMI)#
########variables##############
var1 = DoubleVar()
var2 = DoubleVar()
############FRAMES###############
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
#########################TITLE##########################
lblTitle=Label(Tops, text="       BMI Calculator Program  ",padx=16,pady=16,bd=16,
                fg="#000000", font=('arrial', 54,'bold'),
                bg="light green", relief = 'raise', width = 32, height = 1)
lblTitle.pack()
##############SCALE OF WEIGHT##################
lblWeight =Label(fla, text ="Select Weight in Kilogramas ", font=('arial', 20, 'bold'), bd=20).grid(row = 0, column=0)
Bodyweight = Scale(fla,variable =var1, from_ = 1, to =500, length=880, tickinterval=30, orient= HORIZONTAL)
Bodyweight.grid(row = 1, column=0)
###################TEXT###########################
lblheight = Label(f1b, text= "Enter Height in Meters Square", font =('arial',20, 'bold'), bd=20).grid(row = 0, column =0)
txtheight = Entry(f1b, textvariable = var2, font=('arial', 16, 'bold'),bd=16, width=22, justify='center')
txtheight.grid(row = 1,column=0)
##############RESULT OUTPUT####################
lblBMIResult = Label(f1b, padx =16, pady=16, bd=16,
                     fg="#000000", font=('arial',30,'bold'),
                     bg="light green", relief ='sunk', width = 34, height = 1)
lblBMIResult.grid(row =2, column=0)
####################TABLE######################
lblBMITable = Label(f2,font=('arial',20,'bold'), text="BMI Table").grid(row = 0, column = 0)
txtlblBMITable = Text(f2, height = 12, width = 38, bd=16, font=('arial',12,'bold'))
txtlblBMITable.grid(row=1,column=0)
#########################TABLE OPTIONS##########################
txtlblBMITable.insert(END,'Meaning \t\t'+ "BMI \n\n")
txtlblBMITable.insert(END,'Normal weight \t\t'+ "19-24,9\n\n")
txtlblBMITable.insert(END,'Overweight \t\t'+ "25-29,9\n\n")
txtlblBMITable.insert(END,'Obesity level I\t\t'+ "30-34,9\n\n")
txtlblBMITable.insert(END,'Obesity level II\t\t'+ "35-39,9\n\n")
txtlblBMITable.insert(END,'Obesity level III\t\t'+">=40\n\n")
####################BUTTON##################################
btnBMI = Button(f2, text="Enter to \ncheck your \nBMI",padx=8,pady=8,bd=12, width = 21,
                font=('arial',20, 'bold'), height=3, command=BMI_Call)
btnBMI.grid(row = 2,column=0)


root.mainloop()#shows the main panel
