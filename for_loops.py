# For Loops
"""
for item in "Python":
    print(item)

for item in ['Mosh', 'John', 'Sarah']:
    print(item)

for item in [1, 2, 3, 4]:
    print(item)

for item in range(10):
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total:{total}")
"""

# Nested Loop
"""
for x in range(4):
    for  y in range(3):
        print(f"({x}, {y})")

# Challenge
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
"""

# Lists
"""
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']  
names[0] = 'Jon'
print(names[2:])
print(names)

# Write a program to find the largest number in a list
numbers = [10, 6, 2, 8, 4, 3]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
"""

# 2D Lists
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#matrix[0][1] = 20
#print(matrix[0][1])
for row in matrix:
     for item in row:
         print(item)
"""

# List Methods
"""
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers.index(5))
print(50 in numbers)
numbers.insert(0, 10)
numbers.remove(5)
numbers.pop()
print(numbers)
numbers.clear()
print(numbers)

# Write a program to remove the duplicates in a list.
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
"""

# Tuples
"""
numbers = (1, 2, 3)
print(numbers[0])

# Unpacking
coordinates = (1, 2, 3)
coordinates[0] * coordinates[1] * coordinates[2]
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates # This is unpacking
print(x)
"""

# Dictionaries
"""
# Key-Value Pairs
# Name : John Smith
# Email : John@gmail.com
# Phone : 1234
customer = {
    "Name" : "John Smith",
    "Age" : 30,
    "is_verified" : True
}
print(customer["Name"])
print(customer.get("Birthday", "Jan 1, 1992"))
print(customer)

phone = input("Phone: ")
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}
output = ""
for char in phone:
    output += digits_mapping.get(char, "!") + " "
print(output)
"""
message = input("> ")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)