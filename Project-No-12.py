# QUESTION NO 12:
# Write a Python program that:
# Displays a header for a Kilometers to Miles Converter.
# Asks the user to enter a distance in kilometers.
# Converts the distance to miles using the formula:
# Miles = Kilometers × 0.621371
# Displays the converted distance rounded to two decimal places along with the word “miles”.


print("\n---------- Kilo Metres To Miles Converter -----------")
KM = float(input("Enter Distance In KiloMeters? \n"))
formula = KM * 0.621371
print(f"Distance in Miles is {formula:.2f} miles.")