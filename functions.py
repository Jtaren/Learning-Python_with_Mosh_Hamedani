# Functions
"""def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard')
# print("Start")
greet_user("John")
greet_user("Mary")
print("Finish")
"""
 
"""
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
print("Start")
greet_user("John", "Smith")
print("Finish")
"""

"""
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
print("Start")
greet_user(last_name="Smith", first_name="John")
print("Finish")
"""

"""
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
print("Start")
greet_user("John", "Smith")
calc_cost(total=50, shipping=5, discount=0.1)
print("Finish")
"""

"""
def square(number):
    return number * number

result = square(3)
print(result)
"""

"""
def emoji_converter(message):
    
    words = message.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
result = emoji_converter(message)
print(result)
"""

