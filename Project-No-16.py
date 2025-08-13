# QUESTION NO 16:
# Write a Python program that:
# Displays a header for a Mortgage Calculator.
# Asks the user to enter their salary.
# If the salary is greater than or equal to 25,000:
# Display a congratulatory message with the salary, indicating that the user is eligible for a mortgage.
# Ask the user for their credit score.
# If the credit score is greater than 800, display an interest rate of 4%.
# Otherwise, display an interest rate of 6%.
# If the salary is less than 25,000, display a message with the salary stating that the user is not eligible for a mortgage.




print("\n------------ Welcome To Mortgage Calculator ------------")

salary = int(input("What is your Salary? \n"))

if salary >= 25000:
    print(f"Your Salary is {salary} Congratulations, You are Eligible To Mortgage.")
    credit_score = int(input("What is your credit score? \n"))
    if credit_score > 800:
        print("Interest Rate: 4%")

    else:
        print("Interest Rate: 6%")

else:
    print(f"Your Salary is {salary} Sorry You are not Eligible To Mortgage.")