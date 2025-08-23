# QUESTION NO 27:
# Write a Python program that calculates the final payable amount for a purchase after applying discounts based on customer type and coupon availability.

# The program should take three inputs:
# Total purchase amount in Rupees (must be a positive number).
# Customer type — one of the following: Regular, Premium, or VIP.
# Coupon availability — Yes or No.
# If the purchase amount is less than Rs. 1000, no discount should be applied based on customer type.

# If the purchase amount is Rs. 1000 or more, apply the following discounts:
# Regular: 5% discount
# Premium: 10% discount
# VIP: 20% discount
# If the customer has a coupon, apply an additional 5% discount on the already discounted price.
# Display the final amount to be paid, formatted to two decimal places.
# Validate all inputs, and display appropriate error messages for invalid inputs.





# User Input
try:
    amount = float(input("Enter Total Purchase Amount: "))
except ValueError:
    print("Invalid amount, Enter Only Number.")
    exit()

customer_type = input("Customer Type (Regular/Premium/VIP): ").strip().lower()
coupon = input("Have You Any Coupon? (Yes/No): ").strip().lower()

# Valid Values
valid_customers = ['regular', 'premium', 'vip']
valid_coupons = ['yes', 'no']

# Input validation
if amount < 0:
    print("Invalid amount. Negative value is not allowed.")
elif customer_type not in valid_customers:
    print("Invalid customer type.")
elif coupon not in valid_coupons:
    print("Invalid coupon input.")
else:
    # Base discount
    if customer_type == 'regular':
        discount = 0.05 if amount >= 1000 else 0
    elif customer_type == 'premium':
        discount = 0.10 if amount >= 1000 else 0
    elif customer_type == 'vip':
        discount = 0.20 if amount >= 1000 else 0

    # Discount Apply
    discounted_price = amount * (1 - discount)

    # Coupon Extra Discount
    if coupon == 'yes':
        discounted_price *= 0.95  # extra 5% off

    # Final output
    print(f"Final amount to pay: Rs. {discounted_price:.2f}")
