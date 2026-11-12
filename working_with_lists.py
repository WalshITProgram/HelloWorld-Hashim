# Hashim Saqib
# IT410 - Working with Lists Assignment

# Requirement 1: A list of the courses I have taken at Walsh College, stored in lowercase
walsh_courses = ["it410", "it402", "it305", "it321", "eng210"]

# Requirement 2: Sort the list and print each course in uppercase with a message
walsh_courses.sort()
for course in walsh_courses:
    print("I have taken " + course.upper() + " at Walsh College.")

# Keep a copy of the courses I have already taken (used in requirement 4)
taken_courses = walsh_courses[:]

# Requirement 3: Add the courses I plan to take next term, re-sort, and print the list
walsh_courses.append("it415")
walsh_courses.append("it430")
walsh_courses.append("mgt350")
walsh_courses.sort()
print("This is my course of study with upcoming courses added:")
for course in walsh_courses:
    print(course.upper())

# Requirement 4: Remove the courses I have already taken and print each one I removed
print("I do not have to take these courses:")
for course in taken_courses:
    walsh_courses.remove(course)
    print(course.upper())

# Requirement 5: Print the courses left in the list, each on its own line
print("I plan to take the following courses next term")
for course in walsh_courses:
    print(course.upper())

# Requirement 6: A list of numbers from 1 to 1000 that are divisible by 6
numbers = list(range(6, 1001, 6))

# Requirement 7: Print the first 20 numbers in the list, each on its own line
print("Here are twenty numbers divisible by 6.")
for number in numbers[:20]:
    print(number)

# Requirement 8: Calculate the maximum number in the list and store it as a variable
max_number = max(numbers)

# Requirement 9: Print the maximum number with a message
print("The maximum value in the list is: " + str(max_number))

# Requirement 10: Sum the values from the 10th value to the 50th value in the list and print it
sum_of_values = sum(numbers[9:50])
print("Here is the sum of several values in the list: " + str(sum_of_values))

# Requirement 11: Overwrite the courses variable with the large list of numbers from requirement 6
walsh_courses = numbers
