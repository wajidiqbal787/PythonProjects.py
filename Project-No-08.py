# QUESTION NO 08:
# Write a Python program that:
# Asks the user to enter a temperature in Celsius.
# Converts the temperature to Fahrenheit using the appropriate formula.
# Displays the result in a clear format showing both Celsius and Fahrenheit values.


celsius = int(input("Enter Temperature In Celsius: \n"))
Fahrenheit = int(celsius * 9/5 + 32)
print(f"{celsius} celsius = {Fahrenheit} Farenheit")