import dis

'''
Because Python VM is stack-based, 
some code styles generate fewer bytecode instructions than others, 
which can slightly affect performance.
'''

def square1(num):
    return num * num

def square2(num):
    return num ** 2     # Calculate x power of a number in Python

def increment1(num):
    num += 1
    return num

def increment2(num):
    num = num + 1
    return num


if __name__ == "__main__":
    ultimate_choice = input("Do you want to perform calculations (Y/N): ")
    if ultimate_choice.lower() == "y":
        x = int(input("Enter a number to calculate square for: "))
        choice = int(input("Enter square function to run (1/2): "))
        print(
            f"Square of {x} = {square1(x)}" if choice == 1
            else f"Square of {x} = {square2(x)}" if choice == 2
            else "Invalid choice!!"
        )

        print()
        inc_num = int(input("Enter a number to increment: "))
        inc_choice = int(input("Enter increment function to use (1/2): "))
        print(
            f"Increment of {inc_num} = {increment1(inc_num)}" if inc_choice == 1
            else f"Increment of {inc_num} = {increment2(inc_num)}" if inc_choice == 2
            else "Invalid choice!!"
        )

    print()
    print("--------------Bytecode for square1() function--------------\n")
    dis.dis(square1)
    print()

    print()
    print("--------------Bytecode for square2() function--------------\n")
    dis.dis(square2)
    print()

    print()
    print("--------------Bytecode for increment1() function--------------\n")
    dis.dis(increment1)
    print()

    print()
    print("--------------Bytecode for increment2() function'--------------\n")
    dis.dis(increment2)
    print("\n-------------------------------------------------------------------------------------")
