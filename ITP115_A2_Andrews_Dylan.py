# Dylan Andrews, dmandrew@usc.edu
# ITP 115, Spring 2020
# Assignment 1
# This program creates a Harry Potter vending machine that determines change and gives a discount

def main():


    print("Please select an item from the vending machine:") # displays vending machine options
    print(" a) Butterbeer: 58 knuts")
    print(" b) Quill: 10 knuts")
    print(" c) The Daily Prophet: 7 knuts")
    print(" d) Book of Spells: 400 knuts")
    choice = input("> ") # user selects which one they want

    if choice == "a" or choice == "A": # sets price and choice variables based on selection
        finalChoice = "Butterbeer"
        totalCost = 58
    elif choice == "b" or choice == "B":
        finalChoice = "Quill"
        totalCost = 10
    elif choice == "c" or choice == "C":
        finalChoice = "The Daily Prophet"
        totalCost = 7
    elif choice == "d" or choice == "D":
        finalChoice = "Book of Spells"
        totalCost = 400
    else: # if no valid selection is made, defaults to butterbeer
        print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts")
        totalCost = 58
        finalChoice = "Butterbeer"

    instagram = input("Will you share this on Instagram? (y/n): ")  # user inputs if they would like to share on instagram

    if instagram == "Y" or instagram == "y": # offers discount based on instagram option
        totalCost = totalCost - 5
        print("Thanks! You get 5 knuts off your purchase.")
        coupon = "(cost including coupon of 5 knuts)"
    elif instagram == "N" or instagram == "n":
        coupon = "(with coupon of 0 knuts)"
    else:
        print("You have enter an invalid option. No coupon will be used")
        coupon = "(with coupon of 0 knuts)"

    knutPayment = int(input("How many knuts are you paying with?: ")) # user inputs how much of each respective coin their paying with
    sicklePayment = int(input("How many sickles are you playing with?: "))
    galleonPayment = int(input("How many galleons are you paying with?: "))
    totalPayment = knutPayment + (sicklePayment * 29) + (galleonPayment * 493)
    extra = totalPayment - totalCost # total change needed


    changeGalleon = extra // 493 # calculations for change in galleons, sickles, and knuts
    changeSickle = (extra - (changeGalleon * 493)) // 29
    changeKnuts = (extra - (changeGalleon * 493) - (changeSickle * 29))


    # prints out all of the proper information
    print("You bought a " + finalChoice + " for " + str(totalCost) + " knuts " + coupon + " and paid with " + str(galleonPayment) + " galleon(s), " + str(sicklePayment) + " sickle(s), and " + str(knutPayment) + " knut(s).")
    print("Here is your change (" + str(extra) + " knut(s)):")
    print("Galleon(s): " + str(changeGalleon))
    print("Sickle(s): " + str(changeSickle))
    print("Knut(s): " + str(changeKnuts))



main()