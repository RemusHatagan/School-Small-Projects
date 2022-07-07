
# Subprograms explained 2

# This program is an example of a "Function"
# A function contains a "return" statement / value

a = int(input("Enter a number >>> "))
b = int(input("Enter another number >>> "))

def adding(a, b):  # Parameters are used ( a and b )
    answer = 0
    answer = a + b
    return answer
    
adding(a, b)   # Call with parameters

x = adding(a, b)
print(x)

