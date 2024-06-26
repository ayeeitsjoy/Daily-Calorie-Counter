# Calorie counter based on gender, age, height, and weight
# This simple project determines the user's daily calorie intake based on the information provided.
# Information scaling is based on an article published by Verywell Fit written by Shereen Lehman titled 'How Many Calories Do I Need Each Day?'

def calculate_calories(gender, age, height, weight):
    """
    Calculate daily calorie intake based on gender, age, height, and weight.
    
    Parameters:
    gender (str): Gender of the user ('M' for male, 'F' for female)
    age (int): Age of the user in years
    height (int): Height of the user in centimeters
    weight (int): Weight of the user in kilograms
    
    Returns:
    int: Daily calorie intake
    """
# 'calculate_calories' calculates the daily calories intake based on the users information. It will use different formaulas based on gender. if gender isn't reconignzed it will return as error
    if gender == "M" or gender == "Male":
        cals_intake = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    elif gender == "F" or gender == "Female":
        cals_intake = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
    else:
        return "Incorrect information, please try again."

    return int(cals_intake)

# greeting the user. Prompts to enter valid gender. Collects user information with valid integers. If invalid error message stops process
#calls 'calculate_calories' function with teh users input to print results
def main():
    print("Hi! Welcome to the Calorie Counter.")
    
    user_gender = input("To get started, please let me know your gender. (M/F): ").upper()
    print()

    if user_gender not in ['M', 'F']:
        print("Invalid gender input. Please enter 'M' for Male or 'F' for Female.")
        return

    try:
        user_age = int(input("Age: "))
        user_height = int(input("Height (cm): "))
        user_weight = int(input("Weight (kg): "))
    except ValueError:
        print("Please enter valid numbers for your age, height, and weight.")
        return

    print("---------------")
    print("---------------")

    result = calculate_calories(user_gender, user_age, user_height, user_weight)
    print(f"You will need {result} calories per day for a balanced diet")
##### checks if script is being ran directly; it calls the 'main' function to execute the program
if __name__ == "__main__":
    main()
