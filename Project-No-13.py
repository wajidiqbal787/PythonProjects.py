# QUESTION NO 13:
# Write a Python program that:
# Displays a header for Calculating a Person’s Age.
# Asks the user to enter their birth year and the current year.
# Calculates the person’s age by subtracting the birth year from the current year.
# Displays the calculated age in a clear format.


print("\n----------- Calculate a persons Age----------")
birth_year = int(input("Enter your Birth Year: \n"))
current_year = int(input("Enter Your Current Year: \n"))
age = current_year - birth_year
print(f"Your age is {age}.")
