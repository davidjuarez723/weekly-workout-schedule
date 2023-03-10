import random

def week_day():
    user_input = input("What day of the week is it today?: ")
    options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    selected_day = {"user": user_input}
    return selected_day

def workout_plan(user):
    print(f"Today is {user}")
    if user == "Monday":
        return "Chest Workout"
    elif user == "Tuesday":
        return "Back Workout"
    elif user == "Wednesday":
        return "Leg Day"
    elif user == "Thursday":
        return "Arm Workout"
    elif user == "Friday":
        return "Core Workout and Cardio"
    elif user == "Saturday":
        return "Rest Day"
    elif user == "Sunday":
        return "Rest Day"
    else:
        return "Not a valid answer. Check spelling & remember to capitalize."
    
selected_day = week_day()
result = workout_plan(selected_day["user"])
print(result)