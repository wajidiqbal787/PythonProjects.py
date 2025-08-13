# QUESTION NO 20:
# Write a Python program that:
# Displays a header for a Burger Shop.
# Asks the user to choose a burger size — M, N, or L.
# Asks if the user wants to add mushrooms (Yes or No).
# Asks if the user wants to add cheese (Yes or No).

# Calculates the bill as follows:

# Burger size:
# M → $5
# N → $8
# L → $10

# Mushrooms:
# If burger size is L → add $2
# Otherwise → add $1
# Cheese → add $1
# Displays the final bill.




print("\n--------------- Welcome To Burger Shop ---------------")
size = input("What size burger do you want? M, N or L \n")
add_mashroom = input("Do You Want Mashroom? Yes or No \n")
add_cheese = input("Do You Want Cheese? Yes or No \n")

bill = 0

if size == "M":
    bill += 5
elif size == "N":
    bill += 8
else:
    bill += 10

if add_mashroom == "Yes":
    if size == "L":
        bill += 2
else:
    bill += 1

if add_cheese == "Yes":
    bill += 1

print(f"Your Final Bill is {bill}")