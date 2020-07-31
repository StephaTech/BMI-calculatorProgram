#piece of code from
# DJ Oamen 04 august 2016
# youtube: https://www.youtube.com/watch?v=23_93SXvCpc#
from tkinter import*#standard GUI(Graphical User Interface)package
import csv
import time
from datetime import datetime
root = Tk()
root.geometry("1350x700+0+0")
root.resizable(0,0)
root.title("BMI Calculator")
###############################Function to save CSV#####################################################################
def  save_data_csv(): #Function


    with open('bmi_calculator_store.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date-Time,Name,Height,Weight"])
        writer.writerow([datetime.today().strftime('%Y-%m-%d-%H:%M:%S'),name_var.get(),height_var.get(),weight_var.get()])

    return

###########Function#####################################################################################################
def BMI_Call( bd=8, relief="raise"):#Function

    BHeight = float(height_var.get())
    BWeight = float(weight_var.get())


    if BHeight %2 ==0:
        lblBMIResult.config(text="Please, enter a valid numeric/positive/appropriate range value.")

    else:
        if BHeight <= 0:
            lblBMIResult.config(text="Please, enter a valid number  greater than 0.")
        else:
            BMI = str('%.2f' % (BWeight / (BHeight * BHeight)))
            lblBMIResult.config(text="{} is {},years old:your current BMI is {}".format(name_var.get(), age_var.get(), BMI))
            save_data_csv()
########variables#######################################################################################################
weight_var = DoubleVar()
weight_value = weight_var.get()
height_var = DoubleVar()
height_value = height_var.get()

############FRAMES######################################################################################################
Tops = Frame(root,width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)

f0 = Frame(root,width=500, height = 60, bd=8, relief="raise")
f0.pack()#creating a label widget

f1 = Frame(root, width=600, height = 600, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width = 300,height = 700, bd=8, relief="raise")
f2.pack(side=RIGHT)

fla = Frame(f1, width =600, height =200, bd=20, relief="raise")
fla.pack(side=TOP)
f1b = Frame(f1, width = 600, height = 200, bd=20, relief ="raise")
f1b.pack(side=TOP)
#########################TITLE##########################################################################################
lblTitle=Label(Tops, text="       BMI Calculator Program  ",padx=16,pady=16,bd=16,
                fg="#000000", font=('arrial', 24,'bold'),
                bg="light green", relief = 'raise', width = 52, height = 0)
lblTitle.pack()
#################LABEL AND TEXT#########################################################################################
name_label = Label(f0, text="Enter your name:").grid(row=0, column = 0)#creating a label widget
name_var = StringVar()
#name_value = name_var.get()
name_entry = Entry(f0, textvariable = name_var, bd=5).grid(row=0, column = 1)

age_label = Label(f0, text="Enter your age:").grid(row=1, column = 0)
age_var = StringVar()
#age_value = age_var.get()
age_entry = Entry(f0, textvariable = age_var, bd=5).grid(row=1, column = 1)
########################CHECK BOX Unit##################################################################################
myUnit1 = Label(f0, text="Units:").grid(row=0, column = 3)
Checkbutton(f0, text='Metric').grid(row=1, column = 3)
Checkbutton(f0, text='Imperial').grid(row=2, column = 3)

#########################SCALE OF WEIGHT################################################################################
lblWeight =Label(fla, text ="Select Weight in Kilogramas ", font=('arial', 20, 'bold'), bd=20).grid(row = 0, column=0)
Bodyweight = Scale(fla, variable =weight_var, from_ = 1, to =500, length=880, tickinterval=30, orient= HORIZONTAL)
Bodyweight.grid(row = 1, column=0)
###################TEXT#################################################################################################
lblheight = Label(f1b, text= "Enter Height in Meters Square", font =('arial',20, 'bold'), bd=20).grid(row = 0, column =0)
txtheight = Entry(f1b, textvariable = height_var, font=('arial', 16, 'bold'), bd=16, width=22, justify='center')
txtheight.grid(row = 1,column=0)
##############RESULT OUTPUT LABEL#############################################################################################
lblBMIResult = Label(f1b, padx =16, pady=16, bd=16,
                     fg="#000000", font=('arial',30),
                     bg="light green", relief ='sunk', width = 34, height = 1)
lblBMIResult.grid(row =2, column=0)
####################TABLE###############################################################################################
lblBMITable = Label(f2,font=('arial',20,'bold'), text="BMI Table").grid(row = 0, column = 0)
txtlblBMITable = Text(f2, height = 12, width = 28, bd=16, font=('arial',12,'bold'))
txtlblBMITable.grid(row=1,column=0)
#########################TABLE OPTIONS##################################################################################
txtlblBMITable.insert(END,'Meaning \t\t'+ "BMI \n\n")
txtlblBMITable.insert(END,'Underweight \t\t'+ "<=18.5\n\n")
txtlblBMITable.insert(END,'Normal weight \t\t'+ "18.5-24,9\n\n")
txtlblBMITable.insert(END,'Overweight \t\t'+ "25-29,9\n\n")
txtlblBMITable.insert(END,'Obesity \t\t'+ ">=30\n\n")
####################BUTTON##############################################################################################
btnBMI = Button(f2, text="Enter to \ncheck your \nBMI",padx=8,pady=8,bd=12, width = 21,
                font=('arial',20, 'bold'), height=3, command=BMI_Call)
btnBMI.grid(row = 2,column=0)


root.mainloop()#shows the main panel








