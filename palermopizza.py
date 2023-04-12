#-------------------------------------------------------------------------------
# Name:        Palermo Pizza
# Purpose:      This program creates a receipt for a pizza from 
# "Palermo Pizza"
# Author:      Joshua Cleary
#
# Created:     27/03/2023
# Copyright:   (c) Joshu 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import datetime
# define Prices & Other Constants
SMALL_PIZZA = 9.99
MEDIUM_PIZZA = 12.99
LARGE_PIZZA = 14.99
EXTRA_LARGE = 17.99
SALES_TAX = 0.055

# define Alias Lists
SMALL_ALIAS = [ "SMALL", "Small", "S", "small", "s"]
MEDIUM_ALIAS = [ "MEDIUM", "Medium", "M", "medium", "m"]
LARGE_ALIAS = [ "LARGE", "Large", "L", "large", "l"]
EXTRA_LARGE_ALIAS = [ "EXTRA-LARGE", "Extra-Large", "XL", "extra-large", "xl", 
    "extra_large", "EXTRA_LARGE", "Extra_Large", "Extra-large", "Extra_large"
    "extra large", "EXTRA LARGE", "Extra Large", "Extra large"]

#define global variables
pizza_count = 0
pizza_size = 0
total = 0
large_pizza_count = 0
small_pizza_count = 0
medium_pizza_count = 0
xl_pizza_count = 0

############# define program functions #############
def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate another order? (Y/N): ")
        if yesno.upper() != "Y":
            another_order = False

def get_user_data():
    global pizza_size, pizza_count
    while more_pizzas:
        pizza_size = str(input("What size pizza do you want? (Small, Medium, Large, Extra-Large): "))
        pizza_count = int(input("How many of this size do you want? "))
        sort_variables()
        boolean = input("\nWould you like to order more of a different size? (Y/N): ")
        if boolean.upper() != "Y":
            more_pizzas = False

def sort_variables():
    global pizza_size, pizza_count, large_pizza_count, small_pizza_count, medium_pizza_count, xl_pizza_count, SMALL_ALIAS, MEDIUM_ALIAS, LARGE_ALIAS, EXTRA_LARGE_ALIAS
    if pizza_size in SMALL_ALIAS:
        small_pizza_count += pizza_count
    elif pizza_size in MEDIUM_ALIAS:
        medium_pizza_count += pizza_count
    elif pizza_size in LARGE_ALIAS:
        large_pizza_count += pizza_count
    elif pizza_size in EXTRA_LARGE_ALIAS:
        xl_pizza_count += pizza_count
    else
        Print("ERROR: INVALID INPUT(S), CHECK SPELLING AND TRY AGAIN")
    pizza_size = 0
    pizza_count = 0
    
def perform_calculations():
    global tuitionfee, capitalfee, institutionfee, activityfee, totalowed, balance
    if inout == 1:
        tuitionfee = numcredits * RATE_TUITION_IN
        capitalfee = 0
    else:
        tuitionfee = numcredits * RATE_TUITION_OUT
        capitalfee = numcredits * RATE_CAPITAL

    institutionfee = numcredits * RATE_INSTITUTION
    activityfee = numcredits * RATE_ACTIVITY
    totalowed = tuitionfee + capitalfee + institutionfee + activityfee
    balance = totalowed - scholarshipamt

def display_results():
    print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Number of credits : ' + str(numcredits))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Tuition           $ ' + format(tuitionfee, '10,.2f'))
    print('Capital Fee       $ ' + str(capitalfee))
    print('Institution Fee   $ ' + str(institutionfee))
    print('Activity Fee      $ ' + str(activityfee))
    print('Total             $ ' + str(totalowed))
    print('Scholarship       $ ' + str(scholarshipamt))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Balance Owed      $: ' + str(balance))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(str(datetime.datetime.now()))
    print("NOTE: PVCC Fee Rates: https://www.pvcc.edu/tuition-and-fees")

#### main program call ####
main()