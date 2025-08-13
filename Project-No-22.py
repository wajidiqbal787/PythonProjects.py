# QUESTION NO 23:
# Write a Python program that:
# Displays a header for a Leap Year Calculator.
# Asks the user to enter a year.
# Determines whether the given year is a leap year using the following rules:
# If the year is divisible by 4, then:
# If it is divisible by 100, then it must also be divisible by 400 to be a leap year.
# Otherwise, it is a leap year.
# If it is not divisible by 4, it is not a leap year.
# Displays an appropriate message indicating whether it is a leap year or not.



print("\n--------------- Leap Year Calculator ---------------")

year = int(input("Enter Year: \n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("No Leap Year")