# Ask the user for an input

while True:
    try:
        # Ask user for name and age
        username = str(input("What is your name? "))
        age = int(input("What is your age? "))
    except ValueError as error:
        print("Invalid username or age. Deatils: ", str(error))
    except Exception as error:
        print("Indeterminate error. Deatils: ", str(error))
    else:
        # Print a message to the user
        print("Hello, %s of %d years!" % (username, age))
        break
    finally:
        print("Cycle ended.")



num1 = 12
num2 = 14
if num1 > num2:
    print("greater")
elif num1 < num2:
    print("lesser")
else:
    print("equal")

# For loops
fruits = ["apples", "oranges", "bannanas", "watermellons"]
for fruit in fruits:
    print(fruit)

for letter in fruits[0]:
    print(letter)

for i in range(len(fruits)):
    print(fruits[i])
else:
    print("Finished")

for fruit in ["apples", "oranges", "bannanas", "watermellons"]:
    print(fruit)