# QUESTION NO 10:
# Write a Python program that:
# Displays a welcome message for a Body Mass Index (BMI) Calculator.
# Asks the user to enter their weight in kilograms and height in metres.
# Calculates the BMI using the formula:
# BMI = weight / height**2
# Displays the BMI rounded to two decimal places.

print("Welcome To Body Mass Index Calculator")
weight = float(input("Enter Weight In KiloGrams? \n"))
height = float(input("Enter Height In Metres? \n"))
BMI = weight / height**2

print(f"Your BMI is {BMI:.2f}")
