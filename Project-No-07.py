# QUESTION NO 07:
# Write a Python program that:
# Asks the user to enter two numbers (as floating-point values).
# Performs addition, subtraction, multiplication, and division on the numbers.
# Ensures that division by zero is handled with an appropriate message instead of causing an error.
# Displays the results of all operations in a clear format.




# SIMPLE CALCULATOR

# Step No 01: Get User Input For Two Numbers

number01 = float(input("Enter First Number: \n"))
number02 = float(input("Enter Second Number: \n"))

# Perform Arthmatic Operations

addition = (number01) + (number02)
subtraction = (number01) - (number02)
multiplication = (number01) * (number02)
divide = (number01) / (number02) if number02 != 0 else "Cannot By Divide 0"

# Display The Result

print("\n------------ Calculator Results ----------")
print(f"Addition: {number01} + {number02} = {addition}")
print(f"Subtraction: {number01} - {number02} = {subtraction}")
print(f"Multiplication: {number01} * {number02} = {multiplication}")
print(f"Division: {number01} / {number02} = {divide}")
