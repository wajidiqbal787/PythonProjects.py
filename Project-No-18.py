# QUESTION NO 18:
# Write a Python program that:
# Displays a header for a BMI Calculator.
# Asks the user to enter their height (in metres) and weight (in kilograms).
# Calculates the BMI using the formula:
    
# BMI = weight / height**2

# and rounds it to two decimal places.
# Based on the BMI value, displays one of the following messages:
# BMI < 18.5 → Underweighted
# BMI < 25 → Normal
# BMI < 30 → Overweighted
# Otherwise → Obese




print("\n------------ BMI Calculator --------------")

height = float(input("Enter Your Height: \n"))
weight = float(input("Enter Your Weight: \n"))

BMI = round(weight / height**2, 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, You are Underweighted")
elif BMI < 25:
    print(f"Your BMI is {BMI}, You are Normal")
elif BMI < 30:
    print(f"Your BMI is {BMI}, You are Overweighted")
else:
    print(f"Your BMI is {BMI}, You are Obese")