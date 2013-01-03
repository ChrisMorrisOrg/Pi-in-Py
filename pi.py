# Imports
import sys
from time import *
import math

if sys.version_info < (3,0):
    sys.exit("\n\033[1;38mERROR:\033[1;m Your Python interpreter is too old. Please consider upgrading to Python 3.x or greater.\nFor more information, please visit https://github.com/ChrisMorrisOrg/Pi-in-Py\n")

# Intro
def intro():
    print("\n")
    print("******************************************      ***     ")
    print("******************************************   *********  ")
    print("**********\033[1;33m Welcome to Pi-in-Py! \033[1;m**********  *********** ")
    print("****************\033[1;33m - v0.3 - \033[1;m****************  *********** ")
    print("******************************************   *********  ")
    print("******************************************      ***     ")
    sleep(1.5)

    print("\n\n********************************************************")
    print("********************\033[1;31m - IMPORTANT! - \033[1;m********************")
    print("********************************************************")
    print("-> Use ctrl+C to end the program at any time")
    print("-> Note that calculating pi may slow down your computer\n    and drain your battery.")
    print("-> Please \033[1;1msave all important data before proceeding\033[1;m, and\n    always start with a small number of iterations (try 100).")
    print("-> The larger the amount of iterations you choose, the more precise the\n    approximation will be.")
    print("-> More methods for approximating pi will be added in\n    future revisions.")
    print("-> Follow or contribute to the mini-project at:\n    github.com/ChrisMorrisOrg/Pi-in-Py")

    print("\nSee how close you can get to 3.1415926536!")
    sleep(1)



# Menu
def menu():
    x = 0
    menu = ['Divide-Subtract-Divide-Add...', 'Madhava', 'Euler']
    menu = list(enumerate(menu, start=1))
    while x == 0:
        print("\n\n********************************************************")
        print("***********************\033[1;33m - MENU - \033[1;m***********************")
        print("*********\033[1;33m Choose a method for approximating pi \033[1;m*********")
        print("********************************************************")

        for option in menu:
            print(str(option[0]) +  ". " +  str(option[1]))
        print("Q. Quit")

        x = input("\nEnter a menu item: ").lower()
        print("\n")

        if 'q' in x or 'exit' in x:
            print("******************************************      ***     ")
            print("******************************************   *********  ")
            print("******** Good-pi, have a nice day! *******  *********** ")
            print("*************** Delicious! ***************  *********** ")
            print("******************************************   *********  ")
            print("******************************************      ***     ")
            print("\nhttps://github.com/ChrisMorrisOrg/Pi-in-Py  04-Jan-2013 ")
            sys.exit("\n\n")

        if x == '1':
            iteratively()
        if x == '2':
            madheva()
        if x == '3':
            euler()



# Iterative method to calculate Pi
def iteratively():
    print("\n\n\033[1;36m********************************************************")
    print("*********** - 1. Divide-Subtract-Divide-Add - **********")
    print("********************************************************")
    print("************ 4 * (1 - 1/3 + 1/5 - 1/7 + ...) ***********")
    print("********************************************************\033[1;m")

    x = ""

    # User must enter a number
    while not x.isdigit():
        x = input("How many times do you want to iterate? (More = slower)\nEnter a number: ")

    x = int(x)
    y = 0
    total = 0.0

    # Start the timer
    start_time = time()

    for i in range(1, x*2, 2):
        try:
            if y == x-1:
                print("\nFinal approximation @ iteration #" + str(x) + ":")

            if y%2 == 0:
                total += (1.0/i)
                print("total: (1/" + str(i) + ") - ..." + "\t| Pi: " + str(4*(total)))
            else:
                total -= (1.0/i)
                print("total: (1/" + str(i) + ") + ..." + "\t| Pi: " + str(4*(total)))
            y += 1
        except OverflowError:
            print("Can't continue calculating...")
            break

    # Stop the timer
    print("\nFinished in", time() - start_time, "seconds")

    # Ask the user if they want to return to the main menu
    input("\nReturn?")



# Madheva (iterative) method to calculate Pi
def madheva():
    print("\n\n\033[1;36m********************************************************")
    print("********************* - 2. Madheva - *******************")
    print("********************************************************")
    print("**** sqrt(12) * (1/1*3^0 - 1/1*3^1 + 1/1*3^2 - ...) ****")
    print("********************************************************\033[1;m")

    x = ""

    # User must enter a number
    while not x.isdigit():
        x = input("How many times do you want to iterate? (More = slower)\nEnter a number: ")

    x = int(x)
    y = 0
    total = 0.0

    # Start the timer
    start_time = time()

    for i in range(1, x*2, 2):
        try:
            if y == x-1:
                print("\nFinal approximation @ iteration #" + str(x) + ":")

            if y%2 == 0:
                total += (1.0/(i*math.pow(3,y)))
                print("total: (1/(" + str(i) + "*(3^" + str(y) + "))) - ..." + "\t| Pi: " + str(math.sqrt(12)*(total)))
            else:
                total -= (1.0/(i*math.pow(3,y)))
                print("total: (1/(" + str(i) + "*(3^" + str(y) + "))) + ..." + "\t| Pi: " + str(math.sqrt(12)*(total)))
            y += 1
        except OverflowError:
            print("Can't continue calculating...")
            break

    # Stop the timer
    print("\nFinished in", time() - start_time, "seconds")

    # Ask the user if they want to return to the main menu
    input("\nReturn?")



# Euler's method to calculate Pi
def euler():
    print("\n\n\033[1;36m********************************************************")
    print("********************* - 3. Euler - *******************")
    print("********************************************************")
    print("******** (20 * arctan(1/7)) + (8 * arctan(3/79)) *******")
    print("********************************************************\033[1;m")

    # Start the timer
    start_time = time()

    print("\nFinal approximation @ iteration #1:")

    total = (20*math.atan(1/7)) + (8*math.atan(3/79))
    print("total: (20*atan(1/7)) + (8*atan(3/79))\t| Pi: " + str(total))

    # Stop the timer
    print("\nFinished in", time() - start_time, "seconds")

    # Ask the user if they want to return to the main menu
    input("\nReturn?")





# Main:

# Welcome the user
intro()

# Open the menu
while True:
    menu()
