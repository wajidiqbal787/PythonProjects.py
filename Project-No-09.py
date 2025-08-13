# QUESTION NO 09:
# Write a Python program that:
# Displays a welcome header for a Trip Cost Calculator.
# Asks the user to enter:
# Number of days they will stay in a hotel.
# Price per night for the hotel.
# Flight price.
# Rental car daily price (enter 0 if not needed).
# Any other expenses.
# Calculates the total trip cost by adding:
# Hotel cost (days × hotel price)
# Flight price
# Car rental cost (days × rental car price)
# Other expenses
# Rounds the total cost to two decimal places.
# Displays the total cost in a clear format with a $ sign.




print("\n---------- Welcome To The Trip Cost Calculator----------")
days = int(input("How many days will you stay in hotel? \n "))
hotel_price = float(input("How much does hotel price? \n $"))
flight_price = float(input("How much does flight price? \n $"))
rental_car = float(input("If you need a car please enter price otherwise enter 0? \n $"))
other_expenses = int(input("Enter other expenses? \n $"))
total_cost = round(days * hotel_price + flight_price + days * rental_car + other_expenses, 2)

print(f"Total Cost: ${total_cost}")

print("\n-----Welcome To The Trip Cost Calculator-----\n")
days = int(input("How many days will you stay in hotel? \n "))
hotel_price = float(input("How much does hotel price? \n $"))
flight_price = float(input("How moch does flight price? \n $"))
rental_car = float(input("if you need a car please enter price otherwise enter 0? \n $"))
other_expenses = int(input("Enter other expenses? \n $"))

total_cost = round(days * hotel_price + flight_price + days * rental_car + other_expenses, 2)

print(f"Total cost: ${total_cost}")
