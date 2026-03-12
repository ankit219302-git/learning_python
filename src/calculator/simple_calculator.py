x = int(input("x: "))
y = int(input("y: "))
operation = input("Operation (+,-,/,x): ")

if operation == "+":
    print("The sum is:", x + y)
elif operation == "-":
    print("The difference is:", x - y)
elif operation == "/":
    print("The division quotient is:", x / y)
elif operation == "x":
    print("The product is:", x * y)
else:
    print("Invalid operation")