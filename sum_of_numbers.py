#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct 26, 2022
# A program which loops and calculates the sum of a
# inputted number from 0 until the user number.


def main():

    # Spacer
    print("")

    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # Basic info about the program
    print("A program that takes a number then calculates the sum of it.")

    # Receive the user number
    user_input_number = input("Input the number you wish to calculate: ")
    # Tries to catch any invalid inputs
    try:
        user_input_number = float(user_input_number)

    # Restarts the program is invalided input found
    except ValueError:
        print(f"Your input {user_input_number} is not valid (e.g 5)\n")
        return main()

    # Code to run to make sure the number is positive
    if user_input_number > 0:
        print("It is positive number!")
    else:
        print("Only input a positive number!")
        return main()

    # Calculates the sum of numbers from 0
    while loop_counter <= user_input_number:
        sum = sum + loop_counter
        print(f"Tracked {0} times through loop")
        loop_counter = loop_counter + 1

    # Spacer
    print("")

    # result to user
    print("The sum number from 0 to {} is: {}.".format(user_input_number, sum))


if __name__ == "__main__":
    main()
