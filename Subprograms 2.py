def add_then_return(x, y):
    add_ints = x + y
    return add_ints

def main():
    a = int(input("Enter an integer >>> "))
    b = int(input("Enter another integer >>> "))
    print(add_then_return(a, b))

main()
