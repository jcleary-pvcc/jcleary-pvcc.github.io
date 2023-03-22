#-------------------------------------------------------------------------------
# Name:        tempconvert
# Purpose:     To convert temperature in celsius to fahrenheit
#
# Author:      Joshua Cleary
#
# Created:     21/03/2023
# Note: I made this in pyscripter, instead of IDLE
#-------------------------------------------------------------------------------

#Defines
c_temp = 0
f_temp = 0

another_temp = True
while another_temp == True:
        c_temp = int(input("Enter the degrees Celsius you want to convert: "))

        #Calculates the temperature in fahrenheit.
        f_temp = (c_temp * 1.8) + 32

        #display result
        print("Celsius  :" + str(c_temp))
        print("Fahrenheit: " + str(f_temp))

        #decides if the program should continue.
        yesno = input("\nWould you like to convert another Celsius temperature? (Y/N): ")
        if yesno == "n" or yesno == "N":
            another_temp = False
        else:
            print("Continuing....")
