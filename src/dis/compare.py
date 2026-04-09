def square1(num):
    return num * num

def square2(num):
    return num ** 2     # Calculate x power of a number in python

def increment1(num):
    num += 1
    return num

def increment2(num):
    num = num + 1
    return num

if __name__ == "__main__":
    x = int(input("Enter a number: "))
    choice = int(input("Enter square function to run (1/2): "))
    print(
        f"Square of {x} = {square1(x)}" if choice == 1
        else f"Square of {x} = {square2(x)}" if choice == 2
        else "Invalid choice!!"
    )
