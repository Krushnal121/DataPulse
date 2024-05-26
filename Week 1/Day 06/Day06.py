# custom_module.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# main.py
import custom_module

print(custom_module.add(5, 3))  # Output: 8
print(custom_module.subtract(5, 3))  # Output: 2

# Practicing the learned concepts
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if is_even(num)]
print(even_numbers)  # Output: [2, 4, 6]
