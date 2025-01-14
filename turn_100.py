# This program takes user input of age and name, then prints out the year they'll turn 100.
name = input("What is your name?")
age = input("How old are you?")
bday_passed = input("Have you had a birthday already this year? Please enter Y or N")

current_year = 2025

if bday_passed == "Y":
    print("Hello " + name + "! You will turn 100 in" + str(100 - int(age) + 2025) + ". May you live to see it...")
elif bday_passed == "N":
    print("Hello " + name + "! You will turn 100 in" + str(100 - int(age) + 2025 + 1) + ". May you live to see it...")
else:
    print("Invalid input")
