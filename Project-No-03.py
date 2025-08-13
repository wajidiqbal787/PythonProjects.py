# QUESTION NO 03:
# Write a Python program that:
# Asks the user for their name.
# Stores "Photography" in a variable named hobby.
# Prints a header line with the text.
# Displays a personalized welcome message using an f-string, including:
# "Hello, <name>!.😄"
# "Welcome To The World Of Python Programming. 😲"
# "It is great to know that you love Photography. 🥰"
# "Get Ready To Build Something Amazing Today. 👻"

#Welcome To Message Generator
#Step No 01: Ask For User details
name = input("What is your name? \n")
hobby = "Photography"

#Step No 02: Generate A Peronalized Welcome Message
print("\n ----- Welcome To Message Generator -----")
print(f"Hello, {name}!.😄")
print(f"Welcome To The World Of Python Programming. 😲")
print(f"It is great to know that you love {hobby}. 🥰")
print(f"Get Ready To Build Something Amazing Today. 👻")