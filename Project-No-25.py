# QUESTION NO 25:
# Write a Python program that:
# Displays a header for Student Admission Eligibility Checker.

# Asks the user to enter:
# Student’s age (integer)
# Student’s marks (float)

# Whether the student has completed the prerequisite course (Yes or No)

# Applies the following rules:
# If age is less than 18 → display "Not Eligible: Age Must Be At Least 18".

# If prerequisite course is "Yes":
# Marks ≥ 85 → "Eligible For Scholarship Admission"
# Marks ≥ 70 → "Eligible For Regular Admission"
# Otherwise → "Not Eligible: Marks are Below Required Threshold"
# If prerequisite course is "No" → "Not Eligible: Please Complete Prerequisite Course".




print("\n------------ Student Admission Eligiblity Checker ------------")

age = int(input("Enter Student Age: \n"))
marks = float(input("Enter Student Marks: \n"))
prereq = input("If You Completed Prerequisite Couse enter Yes Otherwise enter No \n")

if age < 18:
    print("Not Eligible: Age Must Be Atleaste 18")

else:
    if prereq == "Yes":
        if marks >= 85:
            print("Eligible For Scholarship Admission")
        elif marks >= 70:
            print("Eligible For Regular Admission")
        else:
            print("Not Eligible: Marks are Below Required Threshold")
    else:
        print("Not Eligible: Please Complete Prerequisite Course")
