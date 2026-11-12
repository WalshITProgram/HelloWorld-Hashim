# Hashim Saqib
# IT410 - Variables and Simple Data Types Assignment

# Requirement 1: Store my first name in all lowercase letters
first_name = "hashim"

# Requirement 2: Store my last name in all uppercase letters
last_name = "SAQIB"

# Requirement 3: Print a greeting with the first name in uppercase and the last name in lowercase
print("Hello, " + first_name.upper() + " " + last_name.lower())

# Requirement 4: Print two newlines
print("\n")

# Requirement 5: Print the quote with quotation marks at the beginning and the end
quote_mark = '"'
quote = "Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi"
print(quote_mark + quote + quote_mark)

# Requirement 6: Store two decimal numbers as variables
number_one = 7.5
number_two = 2.5

# Requirement 7: Store the addition, subtraction, multiplication, and division results as variables
addition_result = number_one + number_two
subtraction_result = number_one - number_two
multiplication_result = number_one * number_two
division_result = number_one / number_two

# Requirement 8: Print each of the four results on its own line
print(str(number_one) + " plus " + str(number_two) + " equals " + str(addition_result))
print(str(number_one) + " minus " + str(number_two) + " equals " + str(subtraction_result))
print(str(number_one) + " times " + str(number_two) + " equals " + str(multiplication_result))
print(str(number_one) + " divided by " + str(number_two) + " equals " + str(division_result))

# Requirement 9: Store the current month as a string and the day of the month as a number
month = "November"
day = 12

# Requirement 10: Print today's date on a new line, tabbed over two times
print("\n\t\tToday is day " + str(day) + " of the month of " + month + ".")
