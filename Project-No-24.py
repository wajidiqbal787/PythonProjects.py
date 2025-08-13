# QUESTION NO 24:
# Write a Python program that:
# Displays a header for Temperature Celsius to Fahrenheit.
# Asks the user to enter the temperature in Celsius.
# Converts the temperature to Fahrenheit using the formula:
    
# fahrenheit = celsius * 9 / 5 + 32
    
# Classifies the Fahrenheit temperature into categories:
# Below 32°F → Freezing
# 32°F to 50°F → Cold
# 51°F to 77°F → Warm
# Above 77°F → Hot
# Displays the converted temperature (rounded to two decimal places) along with its classification.




print("\n--------------- Temperature Celsius To Fahrenheit ---------------")

# Step 1: User input
celsius = float(input("Enter Temperature In Celsius: \n"))

# Step 2: Conversion formula
fahrenheit = celsius * 9 / 5 + 32

# Step 3: Display classification
if fahrenheit < 32:
    print(f"{fahrenheit:.2f}°F - Freezing")
elif 32 <= fahrenheit <= 50:
    print(f"{fahrenheit:.2f}°F - Cold")
elif 51 <= fahrenheit <= 77:
    print(f"{fahrenheit:.2f}°F - Warm")
else:
    print(f"{fahrenheit:.2f}°F - Hot")
