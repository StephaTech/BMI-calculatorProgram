# BMI-calculatorProgram
Created a Python program to calculate Body Mass Index (BMI) Calculator. To determine whether a person is overweight or obese, you can use a measure called the body mass index (BMI).
 
Introduction

By recent estimates, large numbers of people in Ireland and other countries are overweight and a significant number are obese. This causes increases in illnesses such as diabetes and heart disease. To determine whether a person is overweight or obese, you can use a measure called the body mass index (BMI). The website of safefood provides one of many BMI calculators you will find online at http://www.safefood.eu/Healthy-Eating/Weight-Loss/BMI-calculator.aspx. Use it to calculate your own BMI. 

There is extensive information about BMI on this Wikipedia web page 
https://en.wikipedia.org/wiki/Body_mass_index
#############################################################################
The objective of this assignment is to program a BMI calculator using Python.

##Create a BMI calculator Program Description## 


The program should allow the user to enter a person’s name (a string).

The program should allow the user to choose whether to enter the values as Imperial or Metric measurements.

If the user chooses to use imperial measurements the height should be entered as feet and inches. The weight should be entered as stones and pounds. The program should convert the entered values to metric equivalents and display them.

If the user chooses to use metric measurements the height should be entered as centimetres. The weight should be entered as kilograms. The program should convert the entered values to imperial equivalents and display them.


The program should then calculate the BMI and display the result.  The program should also display further information telling the user if the persons BMI indicates if they are underweight, normal, overweight or obese using the values shown in this table. 

##BMI VALUES##
Underweight->less than 18.5
Normal (heathy weight)->between 18.5 and 24.9
Overweight->between 25 and 29.9
Obese->30 or greater

##BMI Formulae##
BMI is calculated using either of the following formulae:
English Imperial BMI Formula
##########OR################
BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
Metric BMI Formula
BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))

You only need to use one of the above as your program will contain all the values in both the imperial and metric systems.
The program should ensure that the user enters valid (numeric /positive / appropriate range) values only. If the user enters incorrect values the program should request new values.

Save the name, height and weight, and date/time for each person into a CSV file 
Functionality
The program should have all functionality described in this document.  It must be written in Python 
and can have either a text or TK graphical user interface.
  ##A GUI interface
  ####OR######
  ##A text exampe:
######Enter your Weight#########
Stones__  Pounds__  or KGs__
####Enter Your Height####
Feet__  Inches__  or CM__ 

Type in your weight either in stones, pounds or kilograms and your height either in feet, inches or centimetres.
Exception Handling:
The application should have sufficient exception handling to ensure robust operation.
It should not fail if the user enters inappropriate values.


