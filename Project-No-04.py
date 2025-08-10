# Personalized Greeting Program

# Step No 01: Ask For User Details

name = str(input("What is your Name? \n"))
age = int(input("What is your Age? \n"))
role = str(input("What is your Role? \n"))
education = str(input("What is your Education? \n"))
color = str(input("Which is your favourite color? \n"))

# Step No 02: Generate A Personalized Greeting Message

print("\n -------- Welcome To Greeting Message --------")
print(f"Hello, {name}! 👋")
print(f"Your age is {age}, You Are Still Young. 😍")
print(f"Your Education is {education}, You are well educated. 😎")
print(f"Your Favorite color is {color}, You are colorful. 🤩")
print(f"Now You are Ready to Start your Python Adventure. 👻")