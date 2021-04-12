# Calculates how close a person is to their desired savings goal
# Takes age, salary, percentage saved, and savings goal

def Retire_Tracker(age, salary, saved, goal):

    annual_saving = salary * saved
    years = goal / annual_saving
    age_met = age + round(years)

    return age_met

# Determines if a person will be able to reach their goal before they pass away
# Takes the age the person's goal is projected to be met

def The_Hard_Truth(age_met):

    if age_met < 100:
        return True

    else:
        return False
