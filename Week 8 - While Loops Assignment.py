# Hashim Saqib
# IT410 - Employee Records Assignment (builds on the User Input Assignment)

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

# The list that will hold one dictionary for each employee
employees = []

# Outer loop: keep adding employees until there are 5
while len(employees) < 5:
    print("\nEnter information for employee #" + str(len(employees) + 1))

    # ---------------- Employee ID ----------------
    # Rules: required, numbers only, 7 or fewer digits
    # Keep asking until a valid ID is entered
    valid = False
    while not valid:
        employee_id = input("Enter the Employee ID: ").strip()
        valid = True

        if employee_id == "":
            print("Error: Employee ID is required. Please try again.")
            valid = False
        elif len(employee_id) > 7:
            print("Error: Employee ID must be 7 or fewer digits. Please try again.")
            valid = False
        else:
            # Check every character to make sure it is a digit
            for character in employee_id:
                if character not in digits:
                    valid = False
            if not valid:
                print("Error: Employee ID must be a number. Please try again.")

    # ---------------- Employee Name ----------------
    # Rules: required, mostly letters, no forbidden characters
    # Keep asking until a valid name is entered
    valid = False
    while not valid:
        employee_name = input("Enter the employee's name: ").strip()
        valid = True

        if employee_name == "":
            print("Error: Employee name is required. Please try again.")
            valid = False
        else:
            # Check for any forbidden characters
            for character in name_forbidden:
                if character in employee_name:
                    valid = False

            # Count the letters to make sure the name is mostly letters
            letter_count = 0
            for character in employee_name:
                if character.lower() in letters:
                    letter_count = letter_count + 1
            if letter_count <= len(employee_name) / 2:
                valid = False

            if not valid:
                print("Error: Name must be mostly letters with no special characters. Please try again.")

    # ---------------- Employee Email Address ----------------
    # Rules: required, mostly letters and numbers, no forbidden characters, must contain @
    # Keep asking until a valid email is entered
    valid = False
    while not valid:
        employee_email = input("Enter the employee's email address: ").strip()
        valid = True

        if employee_email == "":
            print("Error: Email address is required. Please try again.")
            valid = False
        else:
            # Check for any forbidden characters
            for character in email_forbidden:
                if character in employee_email:
                    valid = False

            # An email address needs an @ sign
            if "@" not in employee_email:
                valid = False

            # Count letters and numbers to make sure the email is mostly alphanumeric
            alphanumeric_count = 0
            for character in employee_email:
                if character.lower() in letters or character in digits:
                    alphanumeric_count = alphanumeric_count + 1
            if alphanumeric_count <= len(employee_email) / 2:
                valid = False

            if not valid:
                print("Error: Email address is not valid. Please try again.")

    # ---------------- Employee Address ----------------
    # Rules: NOT required, but if entered it must be mostly letters and numbers
    # with no forbidden characters. Keep asking until it is valid or left blank.
    valid = False
    while not valid:
        employee_address = input("Enter the employee's address (press Enter to skip): ").strip()
        valid = True

        if employee_address != "":
            # Check for any forbidden characters
            for character in address_forbidden:
                if character in employee_address:
                    valid = False

            # Count letters and numbers to make sure the address is mostly alphanumeric
            alphanumeric_count = 0
            for character in employee_address:
                if character.lower() in letters or character in digits:
                    alphanumeric_count = alphanumeric_count + 1
            if alphanumeric_count <= len(employee_address) / 2:
                valid = False

            if not valid:
                print("Error: Address contains characters that are not allowed. Please try again.")

    # ---------------- Greeting Message ----------------
    message = "Hello, " + employee_name + ". Your Employee ID is " + employee_id
    message = message + ", and your email address is " + employee_email + "."
    if employee_address == "":
        message = message + " You did not provide an address."
    else:
        message = message + " Your address is " + employee_address + "."
    print(message)

    # ---------------- Store the Employee ----------------
    # Build one dictionary for this employee, with one key-value pair per line
    if employee_address == "":
        employee_address = "Not provided"

    employee = {
        "employee_id": employee_id,
        "name": employee_name,
        "email": employee_email,
        "address": employee_address,
    }

    # Add this employee's dictionary to the list
    employees.append(employee)

    # ---------------- Add Another Employee? ----------------
    # Ask if the user wants to add another employee (only if there is room for more)
    if len(employees) < 5:
        another = input("Would you like to add another employee? (yes/no) ").strip().lower()
        if another != "yes":
            break

# Print out the final list of employee dictionaries
print("\nEmployee records:")
print(employees)
