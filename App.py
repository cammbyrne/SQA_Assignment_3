#David Penfield, dep153

from BMI_Calculator import BMI_Calc
from BMI_Calculator import Get_Category
from Retirement_Tracker import Retire_Tracker
from Retirement_Tracker import The_Hard_Truth

while True:

    print("Which application would you like to run?")
    print("1) BMI Calculator")
    print("2) Retirement Tracker\n")

    ans = int(input("1 or 2: "))

    if ans == 1:

        print("\nPlease input your height in feet and inches.\n")

        feet = int(input("Feet: "))
        if feet == "x":
            break

        inches = int(input("Inches: "))
        if inches == "x":
            break

        pounds = int(input("\nPlease input your weight in pounds: "))
        if pounds == "x":
            break

        BMI = BMI_Calc(feet, inches, pounds)

        print("Your BMI is " + str(BMI) + ".")

        category = Get_Category(BMI)

        print("You are " + category + ".\n")

        input("Enter any value to continue: ")

    elif ans == 2:

        age = int(input("\nPlease input your age: "))
        if age == "x":
            break

        salary = int(input("\nPlease input your annual salary: "))
        if salary == "x":
            break

        saved = float(input("\nPlease input the percentage of annual salary you plan to save (format: 0.xx): "))
        if saved == "x":
            break

        goal = int(input("\nPlease input your retirement savings goal: "))
        if goal == "x":
            break

        age_met = Retire_Tracker(age, salary, saved, goal)

        print("\nYou are projected to meet your retirement goal by the age of " + str(age_met) + ".")

        success = The_Hard_Truth(age_met)

        if success:
            print("Congratulations! You will successfully be able to retire!\n")

        else:
            print("You will NEVER retire.\n")

        input("Enter any value to continue: ")
