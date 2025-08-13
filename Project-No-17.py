# QUESTION NO 17:
# Write a Python program that:
# Displays a header for an Even and Odd Program.
# Asks the user to enter an integer number.
# Checks whether the number is even or odd using the modulus operator (%).
# Displays "Even Number" if the number is even, otherwise displays "Odd Number".


print("\n------------ Even And Odd Program ------------ ")

number = int(input("Enter Integer Numbers: \n"))

if number % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

    