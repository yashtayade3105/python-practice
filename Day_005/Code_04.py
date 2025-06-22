# Boolean

marks = int(input("Enter your marks : "))
is_passed = marks >= 40
print("Did Student passed? ", is_passed)
# Boolean operations
is_passed_and_high_marks = is_passed and marks > 75
is_passed_or_high_marks = is_passed or marks > 75
print("Did Student passed and has high marks? ", is_passed_and_high_marks)
print("Did Student passed or has high marks? ", is_passed_or_high_marks)

# Another example
age = int(input("Enter your age : "))
is_adult = age >= 18
print("Are you an adult?", is_adult)
