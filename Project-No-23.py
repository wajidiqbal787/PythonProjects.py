# QUESTION NO 23:
# Write a Python program that:
# Displays a header for a Student Grading Program.
# Asks the user to enter marks between 0 and 100.
# Based on the marks entered, displays the grade according to the following criteria:

# 90–100 → Grade A+
# 80–89 → Grade A
# 70–79 → Grade B
# 60–69 → Grade C
# 50–59 → Grade D
# 0–50 → Grade F

# If the marks are outside the range 0 to 100, display "Invalid Marks".



print("\n--------------- Student Grading Program ---------------")

marks = int(input("Enter Marks 0 To 100:   \n"))

if marks >= 90 and marks <= 100:
    print("Grade A+")
elif marks >= 80 and marks <= 89:
    print("Grade A")
elif marks >= 70 and marks <= 79:
    print("Grade B")
elif marks >= 60 and marks <= 69:
    print("Grade C")
elif marks >= 50 and marks <= 59:
    print("Grade D")
elif marks >= 0 and marks <= 50:
    print("Grade F")
else:
    print("Invalid Marks")