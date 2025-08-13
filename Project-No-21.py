# QUESTION NO 21:
# Write a Python program that:
# Displays a header for Gross Pay with Overtime.
# Asks the user to enter the number of hours worked and the hourly rate.
# If the hours worked are less than 40, calculate the pay as:

# Pay = hours × rate

# If the hours worked are more than or equal to 40, calculate overtime pay:
# First 40 hours at the normal rate
# Overtime hours at 1.5 times the normal rate
# Round the final pay to two decimal places and display it.




print("\n--------------- Gross Pay With Overtime ---------------")

hours = float(input("Enter Hours: \n"))
rate = float(input("Enter Rate: \n"))

if hours < 40:
    pay = round(hours * rate ,2)


else:
    overtime = hours - 40
    pay = round(40 * rate + overtime * rate * 1.5,2)

    print(f"Pay: {pay}")
