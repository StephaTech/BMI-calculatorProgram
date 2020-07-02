#Stephany Lais de Araujo Souza
#Email: stephatecth@gmail.com
#To discover your body mass index,
# just select your Height, Weight, Waist and Gender and click "Calculate"
print("Thi program calculates the BMI of a person")
##at variables I need to use some ###exception ###
name= input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))#meters


bmi = round(weight/(height ** 2), 2)# **power of
#bmi =(weight/(height ** 2))#power of

'''if bmi < 25:
    print("The name of the person: {}")
    print("{} is underweight by {} BMI".format(name,bmi))
else:
    print("{} is overweight by {} BMI".format(name,bmi))'''
print("The name of the person:{} \nThe age of the person:{} \nThe BMI of the person:{} ".format(name, age, bmi))
