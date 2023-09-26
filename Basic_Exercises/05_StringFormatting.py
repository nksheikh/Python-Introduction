# String formattings
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# Strings and integers
name = "Nafiz"
age = 26
print("My name is: %s and I am %d years old." % (name, age))
print("That age is %x in lowercase hex and %X in uppercase hex." % (age, age))

# Floating points w/ specific decimal places
pi = 3.141592654
print("The approximate value of PI is: %.6f" % pi)

# Requires TUPLE not LIST
info = ("Nafiz", "Sheikh", "Suntrust", "Checking", 53500.25)
formatStr = "Hello, %s %s. Your %s %s account's current balance is: %.2f."
print(formatStr % info)