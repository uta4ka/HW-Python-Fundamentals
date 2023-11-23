import re

def is_valid_password(password):
    # Check the length of the password
    if len(password) < 6 or len(password) > 16:
        return False

    # Check for at least 1 lowercase letter
    if not re.search("[a-z]", password):
        return False

    # Check for at least 1 uppercase letter
    if not re.search("[A-Z]", password):
        return False

    # Check for at least 1 digit
    if not re.search("[0-9]", password):
        return False

    # Check for at least 1 special character from [S#@]
    if not re.search("[S#@]", password):
        return False

    return True

# Prompt the user for a password
password = input("Enter a password: ")

# Check password validity
if is_valid_password(password):
    print("Valid password.")
else:
    print("Invalid password. Please follow the password criteria.")