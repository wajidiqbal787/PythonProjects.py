# Question No 08: Write a program which prompts the user for a celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature. Formula: (C x 9/5) + 32 = F

print("\n------------ Temperature Converter ------------ ")
celsius = int(input("Enter Temperature In Celsius: \n"))
Fahrenheit = int(celsius * 9/5 + 32)
print(f"{celsius} celsius = {Fahrenheit} Farenheit")