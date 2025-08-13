# QUESTION NO 06:
# Write a Python program that:
# Displays a header for a Gross Pay Project.
# Asks the user to enter the number of hours worked and the hourly rate.
# Converts both inputs to floating-point numbers.
# Calculates and displays the gross pay by multiplying hours with rate.

print("GROSS PAY PROJECT")
hour = input("Enter Hours: \n")
rate = input("Enter Rate: \n")
newhour = float(hour)
newrate = float(rate)

print(f"{newhour * newrate}")