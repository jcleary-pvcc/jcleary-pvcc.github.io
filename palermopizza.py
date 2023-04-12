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
pizza_total = 0
pizza_size = 0
total = 0
total_plus_tax = 0
sales_tax_cost = 0
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
    global large_pizza_count, small_pizza_count, medium_pizza_count, xl_pizza_count, total, SALES_TAX, SMALL_PIZZA, MEDIUM_PIZZA, LARGE_PIZZA, EXTRA_LARGE_PIZZA, total_plus_tax, sales_tax_cost
    total = (large_pizza_count + LARGE_PIZZA) + (small_pizza_count * SMALL_PIZZA) + (medium_pizza_count * MEDIUM_PIZZA) + (xl_pizza_count * EXTRA_LARGE_PIZZA) 
    sales_tax_cost = total * SALES_TAX
    total_plus_tax = total + sales_tax_cost
    pizza_total = large_pizza_count + small_pizza_count + medium_pizza_count + xl_pizza_count



def display_results():
    print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Number of pizzas : ' + str(pizza_total))
    if small_pizza_count():
        print('Number of small pizzas : ' + str(small_pizza_count))
    if medium_pizza_count():
        print('Number of medium pizzas : ' + str(medium_pizza_count))
    if large_pizza_count():
        print('Number of large pizzas : ' + str(large_pizza_count))
    if xl_pizza_count():
        print('Number of extra-large pizzas : ' + str(xl_pizza_count))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Total             $ ' + format(total, '10,.2f'))
    print('Sales Tax         $ ' + str(sales_tax_cost, '10,.2f'))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Balance Owed      $: ' + str(total_plus_tax, '10,.2f'))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(str(datetime.datetime.now()))

#### main program call ####
main()
