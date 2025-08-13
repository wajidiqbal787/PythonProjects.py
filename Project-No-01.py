# QUESTION NO 01:
# Write a Python program that prints a greeting header and displays a person's name, age, and role in two different ways:
# First, by using string concatenation.
# Second, by using an f-string with a newline before the role.

print("\n--------------- Greeting ---------------")
name = "Wajid Iqbal"
age = "3467"
role = "Python Developer"
info = "My Name is " + name + " I am " + age + " years Old and My Role is " + role + "."
infoo = f"My Name is {name} I am {age} years Old \nand My Role is {role}."
print(info)
print(infoo)