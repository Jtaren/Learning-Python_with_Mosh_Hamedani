# we check in a patient named john Smith. He's 20 years old and is a new patient.
"""
full_name = "John Smith"
age = 20
is_new = True
print(full_name)
"""
# Ask two questions: person's name and favourite color. Then, print a message like "Mosh likes blue
"""
name = input("What is your name? ") 
favourite_color = input("What is your favourite color? ")
print(name + ' likes ' + favourite_color)
"""  

# Type conversion
"""
Birth_year = input("Birth year: ")
print(type(Birth_year))
Birth_year = int(Birth_year)
age = 2024 - Birth_year
print(age)
"""
# Ask a user their weight (in pounds), convert it to kilograms and print on the terminal
"""
weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
"""

# Strings
"""
course = "Python's for 'Beginners'"
print(course)
print(course[0])
print(course[-2])
print(course[0:3])
"""

# Formatted Strings
"""
first = "John"
last = "Smith"
message = first + ' [' + last + ']  is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)
"""

# String Methods
"""
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('P'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
"""

# Arithmetic Operations
"""
print(10 // 3)
print(10 % 3)
print(10 ** 3)
x = 10
x = x + 3
x += 3  # Augmented Assignment operator
x -= 3
print(x)
"""

# Operator Precedence
"""
x = 10 + 3 * 2
print(x)
"""
# Math functions
"""
x = 2.9
print(round(x))
print(abs(2.9))
 
import math
print(math.ceil(2.9))
print(math.floor(2.9)) # Check other python3 math module
"""

# If Statements
# If it's a hot day
    # It's a hot day
    # Drink plenty of water
# Otherwise if it's cold
    # It's a cold day
    # Wear warm clothes
# Otherwise
    # It's a lovely day

"""
is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Enjoy your day")
"""

# Price of a house is $1M.
# If buyer has good credit,
    # they need to put down 10%
# Otherwise
    # they need to put down 20%
# Print the down payment

"""
price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")
"""

# Logical Operators

