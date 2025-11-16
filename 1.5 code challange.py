Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

from datetime import datetime

# Get user input for student ID and age
student_id = input("MicWin2135: ")
age = int(input("35: "))

# Print student ID
print(student_id)

# Calculate and print the age in 5 years
age_in_5_years = age + 5
print(f"Your age in 5 years: {age_in_5_years}")

# Calculate and print the doubled age
doubled_age = age * 2
print(f"Your age doubled: {doubled_age}")

# Print the current date and time
current_datetime = datetime.now()
print(f"Current date and time: {current_datetime}")
