# QUESTION NO 15:
# Write a Python program that:
# Displays a header for a Mortgage Calculator.
# Asks the user to enter their salary.
# If the salary is greater than or equal to 20,000, display a message indicating that the salary is normal.
# Otherwise, display a message stating that the user is not eligible for a mortgage.



print("\n------------ Welcome To Mortgage Calculator ------------")
salary = int(input("What is your Salary? \n"))

if salary >= 20000:
    print("Congratulations You Are Eligible For Mortgage.")


else:
    print("Sorry, You are not Eligible To Mortgage.")
