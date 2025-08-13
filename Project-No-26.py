# QUESTION NO 26:
# Write a Python program that:
# Displays a header for University Admission Eligibility With Multiple Criteria.

# Asks the user to enter:
# Age (integer)
# Mathematics marks (float, 0–100)
# English marks (float, 0–100)
# Physics marks (float, 0–100)
# Sports quota status (Yes or No)
# Calculates the total marks = Math + English + Physics.

# Applies the following admission rules:
# If age is less than 18 or greater than 25 → "Invalid Age For Admission".

# If sports quota is "Yes":
# Total marks ≥ 150 → "Admission Granted Under Sports Quota".
# Otherwise → "Admission Denied Under Sports Quota Due To Lower Marks".

# If sports quota is "No":
# Each subject must have ≥ 50 marks and total marks ≥ 200 → "Admission Granted".
# Otherwise → "Admission Denied Due To Lower Total Marks".
# If sports quota input is neither "Yes" nor "No" → "Invalid Input For Sports Quota Status".




print("\n--------------- University Admission Eligiblity With Multiple Criteria ---------------")
age = int(input("Enter Your Age: \n"))
Math = float(input("Enter Your Mathematics Marks (0 To 100): \n"))
English = float(input("Enter Your English Marks (0 To 100): \n"))
Physics = float(input("Enter Your Physics Marks (0 To 100): \n"))
sports_quota = input("Are You Sports Quota Candidate? (Yes/No): \n")

total_marks = Math + English + Physics

if age < 18 or age > 25:
    print("Invalid Age For Admission.")

else:
    if sports_quota == "Yes":
        if total_marks >= 150:
            print("Admission Granted Under Sports Quota.")
        
        else:
            print("Admission Denied Under Sport Quota Due To Lower Marks.")
        

    elif sports_quota == "No":
        if Math >= 50 and English >= 50 and Physics >= 50 and total_marks >= 200:
            print("Admission Granted.")

        else:
            print("Admissiom Denied Due To Lower Total Marks.")

    else:
        print("Invalid Input For Sports Quota Status")