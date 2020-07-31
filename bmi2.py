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
    #Bname = str(myTextl1.get())
    #Bage = int(myTextl2.get())
    BMI = str('%.2f' %(BWeight / (BHeight * BHeight)))
    #lblBMIResult.config(text= Bname + Bage+',years old:your current BMI is'+ BMI)
    #lblBMIResult.config(text="{} is {},years old:your current BMI is {}").format(Bname,Bage,BMI)
    lblBMIResult.config(text="{} is {},years old:your current BMI is {}".format(myTextl1,myTextl2,BMI))
    #lblBMIResult.config(text="{} is {},years old:your current BMI is {}".format(myTextl1,myTextl2,BMI))
    #lblBMIResult(text=Bname+BMI)

########variables##############
var1 = DoubleVar()
var2 = DoubleVar()
#var3 = myTextl1Var()
#var4 = myTextl2()


############FRAMES###############
Tops = Frame(root,width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)

#f0 = Frame(root,width=1350, height=50, bd=8, relief="raise")
#f0.pack(row=0, column = 0)#creating a label widget


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
                fg="#000000", font=('arrial', 24,'bold'),
                bg="light green", relief = 'raise', width = 52, height = 0)
lblTitle.pack()
######
myLabel1 = Label(Tops, text="Enter your name:")#.grid(row=0, column = 0)#creating a label widget
myTextl1 = Entry(Tops,textvariable = var3,bd=5)#.grid(row=0, column = 1)

myLabel2 = Label(Tops, text="Enter your age")#.grid(row=1, column = 0)

myTextl2 = Entry(Tops,textvariable = var4,bd=5)#.grid(row=1, column = 1)

myLabel1.pack(side=LEFT)
myTextl1.pack(side=LEFT)
myLabel2.pack(side=RIGHT)
myTextl2.pack(side=RIGHT)
#########################SCALE OF WEIGHT#################
lblWeight =Label(fla, text ="Select Weight in Kilogramas ", font=('arial', 20, 'bold'), bd=20).grid(row = 0, column=0)
Bodyweight = Scale(fla,variable =var1, from_ = 1, to =500, length=880, tickinterval=30, orient= HORIZONTAL)
Bodyweight.grid(row = 1, column=0)
##############T##################

###################TEXT###########################
lblheight = Label(f1b, text= "Enter Height in Meters Square", font =('arial',20, 'bold'), bd=20).grid(row = 0, column =0)
txtheight = Entry(f1b, textvariable = var2, font=('arial', 16, 'bold'),bd=16, width=22, justify='center')
txtheight.grid(row = 1,column=0)
##############RESULT OUTPUT####################
lblBMIResult = Label(f1b, padx =16, pady=16, bd=16,
                     fg="#000000", font=('arial',30),
                     bg="light green", relief ='sunk', width = 34, height = 1)
lblBMIResult.grid(row =2, column=0)
####################TABLE######################
lblBMITable = Label(f2,font=('arial',20,'bold'), text="BMI Table").grid(row = 0, column = 0)
txtlblBMITable = Text(f2, height = 12, width = 38, bd=16, font=('arial',12,'bold'))
txtlblBMITable.grid(row=1,column=0)
#########################TABLE OPTIONS##########################
txtlblBMITable.insert(END,'Meaning \t\t'+ "BMI \n\n")
txtlblBMITable.insert(END,'Underweight \t\t'+ "<=18.5\n\n")
txtlblBMITable.insert(END,'Normal weight \t\t'+ "18.5-24,9\n\n")
txtlblBMITable.insert(END,'Overweight \t\t'+ "25-29,9\n\n")
txtlblBMITable.insert(END,'Obesity \t\t'+ ">=30\n\n")
####################BUTTON##################################
btnBMI = Button(f2, text="Enter to \ncheck your \nBMI",padx=8,pady=8,bd=12, width = 21,
                font=('arial',20, 'bold'), height=3, command=BMI_Call)
btnBMI.grid(row = 2,column=0)


root.mainloop()#shows the main panel
