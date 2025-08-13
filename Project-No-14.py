# QUESTION NO 14:
# Write a Python program that:
# Displays a header for a Discount Price Calculator.
# Asks the user to enter the original price of a product and the discount percentage.
# Calculates the discount amount and subtracts it from the original price to get the final price.
# Displays the final price after discount in a clear format with a $ sign.


print("\n--------------- Discount Price Calculator ---------------")
original_price = float(input("What is your Original Price of Product? \n $"))
discount_percentage = float(input("What is your Product Discount? \n %"))
calculate = original_price/100 * discount_percentage
final_price = original_price - calculate

print(f"Final Price After Discount is {final_price}$")

