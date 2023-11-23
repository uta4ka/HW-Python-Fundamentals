def get_day_of_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= number <= 7:
        return days[number - 1]
    else:
        return "Invalid input (Enter a number between 1 and 7)."

try:
    number = int(input("Enter a number (1-7) to get the day of the week: "))
    day = get_day_of_week(number)
    print(f"The day of the week is {day}.")
except ValueError:
    print("Error: Enter a valid number (1-7).")