# Hashim Saqib
# IT410 - User Input and While Loops Assignment: Employee Information

# Characters used to check what a value is made of
letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

# Characters that are not allowed in each field (stored as lists)
name_forbidden = ["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+",
                  ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
email_forbidden = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+",
                   ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
address_forbidden = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_", "=", "+",
                     "<", ">", "?", ";", ":", "[", "]", "{", "}"]

# Flag: stays True while everything is valid. As soon as one answer is invalid,
# it becomes False and the program stops asking questions.
active = True

# ---------------- Employee ID ----------------
# Rules: required, numbers only, 7 or fewer digits
employee_id = input("Enter your Employee ID: ").strip()

if employee_id == "":
    print("Error: Employee ID is required.")
    active = False
elif len(employee_id) > 7:
    print("Error: Employee ID must be 7 or fewer digits.")
    active = False
else:
    # Check every character to make sure it is a digit
    for character in employee_id:
        if character not in digits:
            active = False
    if not active:
        print("Error: Employee ID must be a number.")

# ---------------- Employee Name ----------------
# Rules: required, mostly upper and lower case letters, no forbidden characters
if active:
    employee_name = input("Enter your name: ").strip()

    if employee_name == "":
        print("Error: Employee name is required.")
        active = False
    else:
        # Check for any forbidden characters
        for character in name_forbidden:
            if character in employee_name:
                active = False

        # Count the letters to make sure the name is mostly letters
        letter_count = 0
        for character in employee_name:
            if character.lower() in letters:
                letter_count = letter_count + 1
        if letter_count <= len(employee_name) / 2:
            active = False

        if not active:
            print("Error: Employee name must be mostly letters and cannot contain special characters.")

# ---------------- Employee Email Address ----------------
# Rules: required, mostly letters and numbers, no forbidden characters, must contain @
if active:
    employee_email = input("Enter your email address: ").strip()

    if employee_email == "":
        print("Error: Email address is required.")
        active = False
    else:
        # Check for any forbidden characters
        for character in email_forbidden:
            if character in employee_email:
                active = False

        # An email address needs an @ sign
        if "@" not in employee_email:
            active = False

        # Count letters and numbers to make sure the email is mostly alphanumeric
        alphanumeric_count = 0
        for character in employee_email:
            if character.lower() in letters or character in digits:
                alphanumeric_count = alphanumeric_count + 1
        if alphanumeric_count <= len(employee_email) / 2:
            active = False

        if not active:
            print("Error: Email address is not valid.")

# ---------------- Employee Address ----------------
# Rules: NOT required, but if provided it must be mostly letters and numbers
# with no forbidden characters
if active:
    employee_address = input("Enter your address (press Enter to skip): ").strip()

    if employee_address != "":
        # Check for any forbidden characters
        for character in address_forbidden:
            if character in employee_address:
                active = False

        # Count letters and numbers to make sure the address is mostly alphanumeric
        alphanumeric_count = 0
        for character in employee_address:
            if character.lower() in letters or character in digits:
                alphanumeric_count = alphanumeric_count + 1
        if alphanumeric_count <= len(employee_address) / 2:
            active = False

        if not active:
            print("Error: Address contains characters that are not allowed.")

# ---------------- Final Message ----------------
# Only print the message if every answer was valid
if active:
    message = "Hello, " + employee_name + ". Your Employee ID is " + employee_id
    message = message + ", and your email address is " + employee_email + "."
    if employee_address == "":
        message = message + " You did not provide an address."
    else:
        message = message + " Your address is " + employee_address + "."
    print(message)
