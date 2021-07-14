# Write a Python program to check if a given positive integer is a power of four

import math

while True:
    try:
        user_num = int(input("Type a positive integer"))
        if user_num < 0:
            raise Exception("Not a positive integer")
        break
    except ValueError:
        print("Invalid numeric input.")
    except Exception as error:
        print(str(error))

if math.sqrt(user_num) == math.sqrt(user_num):
    print("The number is a perfect square.")
else:
    print("The number is NOT a perfect square.")

print(4.0 == 4)