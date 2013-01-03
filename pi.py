# Imports
import sys
from time import sleep
import math

# Intro
def intro():
    print("\n")
    print("******************************************      ***     ")
    print("******************************************   *********  ")
    print("**********\033[1;33m Welcome to Pi-in-Py! \033[1;m**********  *********** ")
    print("****************\033[1;33m - v0.2 - \033[1;m****************  *********** ")
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
    menu = ['Divide-Add-Divide-Subtract...', 'Madhava']
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
            sys.exit("See you soon! :-)\n\n")

        if x == '1':
            iteratively()
        if x == '2':
            madheva()



# Iterative method to calculate Pi
def iteratively():
    print("\n\n\033[1;36m********************************************************")
    print("*********** - 1. Divide-Add-Divide-Subtract - **********")
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

    input("\nReturn?")




# Main:

# Welcome the user
intro()

while True:
    menu()
