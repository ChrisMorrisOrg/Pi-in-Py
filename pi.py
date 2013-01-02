# Iterative method to calculate Pi
def iteratively(x):
    x = int(x)
    y = 0
    total = 0.0
    for i in range(1, x*2, 2):
        if y%2 == 0:
            total += (1.0/i)
            print("total: (1/" + str(i) + ") + ..." + "\t| Pi: " + str(4*(total)))
        else:
            total -= (1.0/i)
            print("total: (1/" + str(i) + ") - ..." + "\t| Pi: " + str(4*(total)))
        y += 1

# Main:
print("******************************************")
print("******************************************")
print("********** Welcome to Pi in Py! **********")
print("**************** - v0.1 - ****************")
print("******************************************")
print("******************************************\n")


print("************* - IMPORTANT! - *************")
print("->Use ctrl+C to end the program at any time")
print("->This program does not use the most efficient method for calculating Pi and may slow down your computer considerably as well as drain your battery. Please *save all important data before proceeding*, and then start with a small number of iterations.")
print("->100,000 should get to 5-digit accuracy")
print("->Other methods for calculating Pi will be added in future revisions. You can follow the mini-project at: https://github.com/ChrisMorrisOrg/Pi-in-Py")

print("\n\n\nSee how close you can get to 3.1415926536!\n")

# Ask the user how many times they want to iterate
iteratively(input("How many times do you want to iterate? (More iterations = higher precision.)\nEnter number: "))



