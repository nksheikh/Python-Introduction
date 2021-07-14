# Write a Python program to check if an integer is the power of another integer

import math

while True:
    try:
        user_num1 = int(input("Type your first positive integer: "))
        user_num2 = int(input("Type your second positive integer: "))
        if user_num1 < 1 or user_num2 < 1:
            raise Exception("Both numbers must be positive integers.")
        else:
            break
    except ValueError:
        print("Invalid numeric input(s).")
    except Exception as error:
        print(str(error))

if math.log(user_num1, user_num2).is_integer():
    print("The first number %d is a power of the second number %d" % (user_num1, user_num2))
elif math.log(user_num2, user_num1).is_integer():
    print("The first number %d is base of the second number %d" % (user_num1, user_num2))
else:
    print("Neither number is a power or base of the other.")