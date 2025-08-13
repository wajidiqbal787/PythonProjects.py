# QUESTION NO 19:
# Write a Python program that:
# Displays a header for a Mortgage Calculator.
# Asks the user to enter:
# Loan amount
# Annual interest rate (percentage)
# Loan term in years
# Validates that all entered values are greater than 0, otherwise displays an error message for the specific invalid input.
# If all values are valid, calculates the monthly payment using the formula:

# r = annual_interest / 100 / 12
# n = Years * 12
# monthly_amount = loan_amount * r * (1 + r)**n / ((1 + r)**n - 1)

# Displays the monthly payment rounded to two decimal places.





print("\n--------------- MORTGAGE CALCULATOR ---------------")

# User Input:
loan_amount = float(input("Enter Loan Amount: \n"))
annual_interest = float(input("Enter Annual Interest Rate: \n% "))
Years = int(input("Enter Loan Term In Years: \n"))

# Validity Check:
if loan_amount <= 0:
    print("Error: The Loan Amount Must Be Greater Than 0")
elif annual_interest <= 0:
    print("Error: The Interest Rate Must Be Greater Than 0")
elif Years <= 0:
    print("Error: The Loan Term Must Be Greater Than 0")
else:
    # Mortgage calculation
    r = annual_interest / 100 / 12  # Monthly interest rate
    n = Years * 12  # Total number of monthly payments

    monthly_amount = loan_amount * r * (1 + r)**n / ((1 + r)**n - 1)

    print(f"Final Monthly Payment is ${monthly_amount:.2f}")



