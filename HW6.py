# Task 1 - Even numbers that are divisible by 2, odd numbers divisible by 3, and numbers not divisible by 2 and 3
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} is even and divisible by 2")
    elif num % 3 == 0:
        print(f"{num} is odd and divisible by 3")
    else:
        print(f"{num} is not divisible by 2 and 3")

# Task 2 - Check the login using a while loop
while True:
    login = input("Enter your login: ")
    if login == "First":
        print("Hello, First! Welcome.")
        break
    else:
        print("Error: Incorrect login. Please try again.")
This code uses a while loop to repeatedly prompt the user for a login. If the login is "First," it greets the user and exits the loop. If the login is different, it displays an error message and continues to prompt for the login until "First" is entered.





