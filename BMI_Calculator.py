# Calculate a person's body mass index
# Takes weight
# Takes height in two variables

def BMI_Calc(feet, inches, pounds):

    kilos = pounds * 0.45

    height_in_inches = (feet * 12) + inches
    meters = height_in_inches * 0.025

    BMI = kilos / (meters * meters)

    return round(BMI, 1)

# Returns a person's BMI category
# Takes BMI

def Get_Category(BMI):

    if BMI <= 18.5:
        return "underweight"

    elif BMI <= 24.9:
        return "a normal weight"

    elif BMI <= 29.9:
        return "overweight"

    else:
        return "obese"
