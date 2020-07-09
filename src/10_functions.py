# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
# Define function with 1 parameter (number)
def is_even(num1):
# Check if number is even using modulo
    if num1 % 2 == 0:
# Return True if num is even
        return True
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
def is_even2(num2):
    if num2 % 2 == 0:
        print("Even!")
    else:
        print("Odd")

is_even2(num)
