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
"""
# If applicant has high income AND good credit eligible for loan
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
# If applicant has high income OR good credit eligible for loan
has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")

# AND: both
# OR: at least one
# NOT:

# If applicant good credit doesn't have a criminal record

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
"""

# Comparison Operators
"""
# If temperature is greater than 30
    # it's a hot day
# Othherwise if it's less than 10
    # it's a cold day
# Otherwise
    # It's neither hot nor cold

temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# If name is less than 3 characters long 
    # name must be at least 3 characters
# otherwise if it's more than 50 characters long
    # name can be a maximum of 50 characters
# otherwise
    # name looks good!

name = "Jkkkk"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be at maximum of 50 characters")
else:
    print("Name looks good!")
"""

# Weight Converter
"""
# weight: 72
# (L)bs or (K)g: k
# You are 160.0 pounds

weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
"""

# while loops
"""i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")

i = 1
while i <= 5:
    print('*' * i) 
    i = i + 1

# Guessing Game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")
"""
# Car Game
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that!")
