# For loop
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# While loop
count = 0
while count < 5:
    print(count)  # Output: 0 1 2 3 4
    count += 1

# Break and continue in loops
for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0 1 2

for i in range(5):
    if i == 3:
        continue
    print(i)  # Output: 0 1 2 4

# Using try, except, and finally
try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("That's not a valid number!")
finally:
    print("This block is executed no matter what.")
