# Write a Python program to check if a given positive integer is a power of two

import math

# User generated number
user_num = 0;

# Ask the user for a number
while True:
    try:
        user_num = int(input("Please enter an integer: "))
    except ValueError as error:
        print("Please enter a valid integer. Error:", str(error))
    except Exception as error:
        print("An unexpected error occured:", str(error))
    else:
        break 
    finally:
        pass

if math.log(user_num, 2).is_integer():
    print("The number is a power of 2")
else:
    print("The number is NOT a power of 2")