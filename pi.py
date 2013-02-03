import math
import sys
from time import *
import random

##########
# About: #
##########
# Created by Chris Morris (http://chrismorris.org)
# Follow the project at https://github.com/ChrisMorrisOrg/Pi-in-Py
INFO_TITLE = "Pi-in-Py"
INFO_VERSION = "v0.5"
INFO_RELEASE_DATE = "05-Jan-2013"
INFO_WEBSITE = "https://github.com/ChrisMorrisOrg/Pi-in-Py"




############################
# Force Python 3.x and above
if sys.version_info < (3,0):
    sys.exit("\n\033[1;38mERROR:\033[1;m Your Python interpreter is too old. \
Please consider upgrading to Python 3.x or greater.\n\
For more information, please visit " + INFO_WEBSITE + "\n")
############################




##############
# Fake Chat: #
##############
def fakeChat(text):
    # Set SPEED_VARIANCE to 0.001 for low variance, 10 for high variance
    SPEED_VARIANCE = 0.03
    x = 0
    rate = 1
    # Ensure clean input
    text = str(text)
    rate = int(rate)
    
    print("\033[1;34m", end="")
    while x < len(text):
        print(text[x:x+1], end="")
        sys.stdout.flush()
        sleep(math.sin(random.random()*SPEED_VARIANCE))
        x += rate
    print("\033[1;m", end="")




##################
# ColourfulShell: # https://gist.github.com/4450466
##################
# Colourise - colours text in shell. Returns plain if colour doesn't exist.
def colourise(colour, text):
    if colour == "black":
        return "\033[1;30m" + str(text) + "\033[1;m"
    if colour == "red":
        return "\033[1;31m" + str(text) + "\033[1;m"
    if colour == "green":
        return "\033[1;32m" + str(text) + "\033[1;m"
    if colour == "yellow":
        return "\033[1;33m" + str(text) + "\033[1;m"
    if colour == "blue":
        return "\033[1;34m" + str(text) + "\033[1;m"
    if colour == "magenta":
        return "\033[1;35m" + str(text) + "\033[1;m"
    if colour == "cyan":
        return "\033[1;36m" + str(text) + "\033[1;m"
    if colour == "gray":
        return "\033[1;37m" + str(text) + "\033[1;m"
    return str(text)

# Highlight - highlights text in shell. Returns plain if colour doesn't exist.
def highlight(colour, text):
    if colour == "black":
        return "\033[1;40m" + str(text) + "\033[1;m"
    if colour == "red":
        return "\033[1;41m" + str(text) + "\033[1;m"
    if colour == "green":
        return "\033[1;42m" + str(text) + "\033[1;m"
    if colour == "yellow":
        return "\033[1;43m" + str(text) + "\033[1;m"
    if colour == "blue":
        return "\033[1;44m" + str(text) + "\033[1;m"
    if colour == "magenta":
        return "\033[1;45m" + str(text) + "\033[1;m"
    if colour == "cyan":
        return "\033[1;46m" + str(text) + "\033[1;m"
    if colour == "gray":
        return "\033[1;47m" + str(text) + "\033[1;m"
    return str(text)




############
# Artwork: #
############
# Welcome Banner
def art_welcome():
    print("\n")
    print("\
******************************************      ***     \n\
******************************************   *********  \n\
********** " + colourise("yellow", "Welcome to " + INFO_TITLE + "!") + " **********  *********** \n\
****************" + colourise("yellow", " - " + INFO_VERSION + " - ") + "****************  *********** \n\
******************************************   *********  \n\
******************************************      ***     ")

def art_important():
    print("\
\n\n\
********************************************************\n\
********************" + colourise("red", " - IMPORTANT! -") + " ********************\n\
********************************************************")

def art_menu():
    print("\
\n\n********************************************************\n\
***********************" + colourise("yellow", " - MENU - ") + "***********************\n\
*********" + colourise("yellow", " Choose a method for approximating pi ") + "*********\n\
********************************************************")

def art_exit():
    print("\
******************************************      ***     \n\
******************************************   *********  \n\
*************** Good-pi... ***************  *********** \n\
******* ~ Have a delicious day! ~ ********  *********** \n\
******************************************   *********  \n\
******************************************      ***     \n\
\n" + INFO_WEBSITE + "  " + INFO_RELEASE_DATE + " ")

def art_iteratively():
    print(colourise("cyan",
"\n\n\
********************************************************\n\
*********** - 1. Divide-Subtract-Divide-Add - **********\n\
********************************************************\n\
************ 4 * (1 - 1/3 + 1/5 - 1/7 + ...) ***********\n\
********************************************************"))

def art_madheva():
    print(colourise("cyan",
"\n\n\
********************************************************\n\
********************* - 2. Madheva - *******************\n\
********************************************************\n\
**** sqrt(12) * (1/1*3^0 - 1/1*3^1 + 1/1*3^2 - ...) ****\n\
********************************************************"))

def art_euler():
    print(colourise("cyan",
"\n\n\
********************************************************\n\
********************* - 3. Euler - *********************\n\
********************************************************\n\
******** (20 * arctan(1/7)) + (8 * arctan(3/79)) *******\n\
********************************************************"))

def art_fibonacci():
    print(colourise("red", "    _ , ") + colourise("magenta", "      ") + colourise("blue", "       ") + colourise("magenta", "      __   ") + colourise("red", "      __  ") + colourise("magenta", "   ___                           "))
    print(colourise("red", "  ,- - _") + colourise("magenta", "-_, _-") + colourise("blue", "_ _,,  ") + colourise("magenta", "   ,-||-,  ") + colourise("red", "    /  -, ") + colourise("magenta", " -   -_, ") + colourise("blue", "  ,- _~. ") + colourise("magenta", "  ,- _~.") + colourise("red", " _-_, "))
    print(colourise("red", " _||_   ") + colourise("magenta", " //   ") + colourise("blue", " -/  ) ") + colourise("magenta", "  ('|||  ) ") + colourise("red", "   ||   ) ") + colourise("magenta", "(  ~/||  ") + colourise("blue", " (' /|   ") + colourise("magenta", " (' /|  ") + colourise("red", "   // "))
    print(colourise("red", "' ||    ") + colourise("magenta", " ||   ") + colourise("blue", "~||_<  ") + colourise("magenta", " (( |||--))") + colourise("red", "  ~||---) ") + colourise("magenta", "(  / ||  ") + colourise("blue", "((  ||   ") + colourise("magenta", "((  ||  ") + colourise("red", "   || "))
    print(colourise("red", "  ||    ") + colourise("magenta", "~||   ") + colourise("blue", " || \\\ ") + colourise("magenta", " (( |||--))") + colourise("red", "  ~||---, ") + colourise("magenta", " \/==||  ") + colourise("blue", "((  ||   ") + colourise("magenta", "((  ||  ") + colourise("red", "  ~|| "))
    print(colourise("red", "  |,    ") + colourise("magenta", " ||   ") + colourise("blue", " ,/--||") + colourise("magenta", "  ( / |  ) ") + colourise("red", "  ~||  /  ") + colourise("magenta", " /_ _||  ") + colourise("blue", " ( / |   ") + colourise("magenta", " ( / |  ") + colourise("red", "   || "))
    print(colourise("red", "_-/    ") + colourise("magenta", "_-_,   ") + colourise("blue", "_--_-' ") + colourise("magenta", "   -____-  ") + colourise("red", "   |, /   ") + colourise("magenta", "(  - \\, ") + colourise("blue", "  -____-  ") + colourise("magenta", " -____- ") + colourise("red", "_-_, "))
    print(colourise("red", "        ") + colourise("magenta", "     ") + colourise("blue", "(       ") + colourise("magenta", "           ") + colourise("red", " -_-  --~ ") + "                                ")
    print(colourise("red", "*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#"))
    print(colourise("magenta", "#*#*#*#*#*#*#*#*#*#*#*#*#*#*# - F. Fibonacci - *#*#*#*#*#*#*#*#*#*#*#*#*#*"))
    print(colourise("blue", "*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#"))
    print(colourise("magenta", "#*#*#*#*#*#*#*#*#*#*#*#*#*# F_n = F_n-1 + F_n-2 #*#*#*#*#*#*#*#*#*#*#*#*#*"))
    print(colourise("red", "*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#"))

def art_newton():
    print(colourise("cyan",
"\n\n\
********************************************************\n\
********************* - 4. Newton - ********************\n\
********************************************************\n\
 2 * (1+ (1/3 * (1 + (2/5) * (1 + (3/7) * (1 + ...))))) \n\
********************************************************"))




#############
# Messages: #
#############
def msg_important():
    print("-> Use ctrl+C to end the program at any time")
    print("-> Note that calculating pi may slow down your computer\n    and drain your battery.")
    print("-> Please \033[1;1msave all important data before proceeding\033[1;m, and\n    always start with a small number of iterations.")
    print("-> The larger the amount of iterations you choose, the\n    more precise the approximation will be.")
    print("-> More methods for approximating pi will be added in\n    future revisions.")
    print("-> Follow or contribute to the mini-project at:\n    github.com/ChrisMorrisOrg/Pi-in-Py")



#############
# Sections: #
#############
# Intro
def intro():
    art_welcome()
    sleep(1.5)

    art_important()
    msg_important()
    
    print("\nSee how close you can get to 3.1415926536!")
    sleep(1)


# Menu
def menu():
    x = 0
    # List of menu items
    menu = ['Divide-Subtract-Divide-Add...', 'Madhava', 'Euler', 'Newton']
    menu = list(enumerate(menu, start=1))
    while x == 0:
        art_menu()
        
        # Print the numbered menu items.
        for option in menu:
            print(str(option[0]) +  ". " +  str(option[1]))
        print("I. Information")
        print("Q. Quit")

        x = input("\nEnter a menu item: ").lower()
        print("\n")


        # Route the user to their request
        if 'q' in x or 'exit' in x:
            art_exit()
            sys.exit("\n\n")
        if x == '1':
            iteratively()
        if x == '2':
            madheva()
        if x == '3':
            euler()
        if x == '4':
            newtonIntro()
        if x == 'i':
            information()


# Iterative method to calculate Pi
def iteratively():
    x, y, total = "", 0, 0.0
    art_iteratively()


    # User must enter a number
    while not x.isdigit():
        x = input("How many times do you want to iterate? (More = slower)\nEnter a number: ")

    # Cast input String to int
    x = int(x)

    # Start the timer
    start_time = time()

    # The algorithm
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
    art_madheva()
    x, y, total = "", 0, 0.0

    # User must enter a number
    while not x.isdigit():
        x = input("How many times do you want to iterate? (More = slower)\nEnter a number: ")

    # Cast input String to int
    x = int(x)

    # Start the timer
    start_time = time()

    # The algorithm
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
    art_euler()
    # Start the timer
    start_time = time()

    print("\nFinal approximation @ iteration #1:")

    # The calculation
    total = (20*math.atan(1/7)) + (8*math.atan(3/79))
    print("total: (20*atan(1/7)) + (8*atan(3/79))\t| Pi: " + str(total))

    # Stop the timer
    print("\nFinished in", time() - start_time, "seconds")

    # Ask the user if they want to return to the main menu
    input("\nReturn?")


# Easter egg: Fibonacci numbers
def fibonacci():
    art_fibonacci()
    x, a, b, y = "", 0, 1, 0

    # User must enter a number
    while not x.isdigit():
        x = input(
"\nHow many times do you want to iterate? (More = slower)\n\n\
Tip: Try numbers between 1000 and 3000, then scroll\n\
through the numbers to see an amazing pattern\n" + colourise("red", "WARNING!")\
+ " This may make your screen flash quickly!\n\n\
Enter a number: ")

    # Cast input String to int
    x = int(x)

    # Start the timer
    start_time = time()

    # The algorithm
    while y < x:
        # Colourise each number red-magenta-blue-magenta...
        if y % 4== 0:
            print(colourise("red", b), end=" ")
        if y % 4 == 1 or y % 4 == 3:
            print(colourise("magenta", b), end=" ")
        if y % 4 == 2:
            print(colourise("blue", b), end=" ")
        a, b, y = b, a+b, y+1


    # Stop the timer
    print("\nFinished in", time() - start_time, "seconds")

    # Ask the user if they want to return to the main menu
    input("\nReturn?")


# Newton - Intro page
def newtonIntro():
    art_newton()
    x = ""

    # User must enter a number
    while not x.isdigit() or int(x) >= 995:
        x = input("How many times do you want to recurse? (More = slower)\nEnter a number less than 995: ")

    # Cast input String to int
    x = int(x)

    # Start the timer
    start_time = time()

    # Call the recursive algorithm
    print(str("\nRecursion #" + str(x) + ": " + str(2*newton(1, 3, x, True))))

    # Stop the timer
    print("\nFinished in", time() - start_time, "seconds")

    # Ask the user if they want to return to the main menu
    input("\nReturn?")


# Newton (recursive) method to calculate pi
def newton(x, i, y, showResults):
    # The algorithm
    # Print the final number reached if showResults = True
    if showResults:
        if y > 0:
            result = 1 + (x/i) * newton(x+1, i+2, y-1, True)
            print("Recursion #" + str(y-1) + ": " + str(2*newton(1, 3, y-1, False)))
            return result
        return 1
    # Don't print the final number
    else:
        if y > 0:
            return 1 + (x/i) * newton(x+1, i+2, y-1, False)
        return 1

# Play Game
def playGame():
    fakeChat("Well then, do you want to play a game?")
    userInput = input(" (y/n): ").lower()[:1]
    if userInput == 'n':
        fakeChat("That's upsetting. Are you sure?")
        userInput = input(" (yes/no): ").lower()[:1]
        while userInput == 'y':
            fakeChat("That's upsetting. Are you sure?")
            userInput = input(" (yes/no): ").lower()[:1]
    
    fakeChat("Yay! Let's play...\n")
    
    questions = ["What is 1+1?",
"What is the best number pin the world?",
"What is 6*(3^74)? (Work pit out in your head - or I \nwon't accept your answer!)",
"If pI have two apples and you take one away from me,\n does that make you a jerk?\nEnter 1 for yes, or 0 for yes.",
"So, how many sea shells does she really sell pi the\n seashore?",
"How many US dollars is Amerpica worth?",
"How many apples a day keep the doctor away?",
"How many letters are there pin the alphabet?",
"If pI have a pattern: 1, 1, 2, 3, 5, 8 ... which \nnumber comes next?",
"How many?",
"There are ___ days pin a standard year?"]
    
    fakeChat(random.choice(questions))
    userInput = input("\n\nEnter number: ")
    if userInput != "3.14159":
        fakeChat("Seriously? You're terrible at maths!\nWhy... How did you even find this app?\n")
        userInput = input("Return to main menu?")
    else:
        print(
colourise("red","WW      WW IIIII NN   NN NN   NN EEEEEEE RRRRRR  !!! \n") +
colourise("green","WW      WW  III  NNN  NN NNN  NN EE      RR   RR !!! \n") +
colourise("blue","WW   W  WW  III  NN N NN NN N NN EEEEE   RRRRRR  !!! \n") +
colourise("magenta"," WW WWW WW  III  NN  NNN NN  NNN EE      RR  RR      \n") +
colourise("cyan","  WW   WW  IIIII NN   NN NN   NN EEEEEEE RR   RR !!! "))
        sleep(1)
        fakeChat("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        fibonacci() # The Easter Bunny came this year!

# Information page
def information():
    print(colourise("cyan","\
                  ___           ___           ___     \n\
      ___        /\__\         /\  \         /\  \    \n\
     /\  \      /::|  |       /::\  \       /::\  \   \n\
     \:\  \    /:|:|  |      /:/\:\  \     /:/\:\  \  \n\
     /::\__\  /:/|:|  |__   /::\~\:\  \   /:/  \:\  \ \n\
  __/:/\/__/ /:/ |:| /\__\ /:/\:\ \:\__\ /:/__/ \:\__\\\n\
 /\/:/  /    \/__|:|/:/  / \/__\:\ \/__/ \:\  \ /:/  /\n\
 \::/__/         |:/:/  /       \:\__\    \:\  /:/  / \n\
  \:\__\         |::/  /         \/__/     \:\/:/  /  \n\
   \/__/         /:/  /                     \::/  /   \n\
                 \/__/                       \/__/    \n\n\
Created by Chris Morris.\n\
Website: www.ChrisMorris.org\n\
Send me Questions: Twitter @ChrisMorrisOrg\n\n\
Pi-in-Py was developed using Python.\n\
You can follow the project at: \n"\
+ INFO_WEBSITE + "\n\
If you'd like to contribute, feel free to send a pull \n\
request.\n"))

    # Ask the user if they want to return to the main menu
    userInput = input("\nReturn to main menu? (yes/no): ").lower()[:1]
    
    # If they say no, play a game
    if userInput == 'n':
        playGame()




#########
# Main: #
#########

# Welcome the user
intro()

# Open the menu, and keep it open until they quit
while True:
    menu()
