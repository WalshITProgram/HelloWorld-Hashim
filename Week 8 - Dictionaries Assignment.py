# Hashim Saqib
# IT410 - Dictionaries Assignment (builds on the Condition Statements program)

# Requirement 1: A single list with all of the employee data in the order provided
employee_data = [1121, "Jackie Grainger", 22.22,
                 1122, "Jignesh Thrakkar", 25.25,
                 1127, "Dion Green", 28.75, False,
                 24.32, 1132, "Jacob Gerber",
                 "Sarah Sanderson", 23.45, 1137, True,
                 "Brandon Heck", 1138, 25.84, True,
                 1152, "David Toma", 22.65,
                 23.75, 1157, "Charles King", False,
                 "Jackie Grainger", 1121, 22.22, False,
                 22.65, 1152, "David Toma"]

# Requirement 2: Sort the data into three lists: employee numbers, names, and hourly wages
# Requirement 3: Use "not in" so no duplicate data is added to the new lists
employee_numbers = []
employee_names = []
hourly_wages = []

for item in employee_data:
    # A value is a name (string) if converting it to a string does not change it
    if item == str(item):
        if item not in employee_names:
            employee_names.append(item)
    # Skip the True/False values from the unknown spreadsheet column
    elif item != True and item != False:
        # Employee numbers are whole numbers over 1000; wages are smaller decimal numbers
        if item > 1000:
            if item not in employee_numbers:
                employee_numbers.append(item)
        else:
            if item not in hourly_wages:
                hourly_wages.append(item)

print("Employee numbers: " + str(employee_numbers))
print("Employee names: " + str(employee_names))
print("Hourly wages: " + str(hourly_wages))

# Requirement 4: Multiply each wage by 1.3 to include benefits and store it in total_hourly_rate
total_hourly_rate = []
for wage in hourly_wages:
    total_hourly_rate.append(wage * 1.3)

print("Total hourly rates: " + str(total_hourly_rate))

# Requirement 4 (continued): Warn if the maximum total hourly rate is over 37.30
max_rate = max(total_hourly_rate)
if max_rate > 37.30:
    print("Warning: someone's salary may be a budget concern.")

# Requirement 5: Add any total hourly rate between 28.15 and 30.65 to underpaid_salaries
underpaid_salaries = []
for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

print("Underpaid salaries: " + str(underpaid_salaries))

# Requirement 6: Calculate a raise in dollars for each original hourly wage and store it in company_raises
company_raises = []
for wage in hourly_wages:
    if wage >= 22 and wage < 24:
        raise_amount = wage * 0.05
    elif wage >= 24 and wage < 26:
        raise_amount = wage * 0.04
    elif wage >= 26 and wage < 28:
        raise_amount = wage * 0.03
    else:
        raise_amount = wage * 0.02
    company_raises.append(raise_amount)

print("Company raises (in dollars): " + str(company_raises))

# Requirement 7: A complex condition with four truth tests on one line
# Behavior: If the company has more than 5 employees, AND the lowest hourly wage is at least
# 22 dollars, AND no one's total hourly rate is over 40 dollars, AND David Toma is on the
# employee list, then print that payroll is within normal limits. Otherwise, print that
# payroll needs to be reviewed.
if len(employee_names) > 5 and min(hourly_wages) >= 22 and max(total_hourly_rate) <= 40 and "David Toma" in employee_names:
    print("Payroll is within normal limits.")
else:
    print("Payroll needs to be reviewed.")

# ---------------------------------------------------------------------------
# NEW THIS WEEK: Combine the lists into a database-like list of dictionaries
# ---------------------------------------------------------------------------

# The sorting loop above adds each employee's number, name, and wage in the same order,
# so the same index position in every list belongs to the same employee.
# For example, index 0 in each list is Jackie Grainger's information.

# Start with an empty list that will hold one dictionary per employee
employee_database = []

# Loop through every index position in the lists
for index in range(len(employee_numbers)):
    # Build one dictionary for this employee, with one key-value pair per line
    employee = {
        "employee_number": employee_numbers[index],
        "employee_name": employee_names[index],
        "hourly_wage": hourly_wages[index],
        "total_hourly_rate": total_hourly_rate[index],
        "company_raise": company_raises[index],
    }

    # Add this employee's dictionary to the database list
    employee_database.append(employee)

# Print out the final list of employee dictionaries
print(employee_database)
