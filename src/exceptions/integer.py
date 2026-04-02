'''
---- Checking if the input is an integer ----

Option 1: Using string function
'''
# n = input("Enter an integer: ")
# if n.isnumeric():
#     print("Integer")
# else:
#     print("Not an integer")

'''
---- Checking if the input is an integer ----

Option 2: Catching the exception and printing unwanted case message in except block
'''
# try:
#     n = int(input("Enter an integer: "))
#     print("Integer")
# except ValueError:
#     print("Not an integer")

'''
---- Checking if the input is an integer ----

Option 3: Catching the exception and printing desired case message in else
'''


def print_hash(hash_count):
    if hash_count > 0:
        print("#" * hash_count)     # This prints '#' hash_count times
    else:
        print("Cannot print '#'", hash_count, "times")


try:
    n = int(input("Enter an integer: "))
    print_hash(n)
except ValueError as ve:
    print("Not an integer")
    print("---------------Input Error Details---------------\n", ve)
    print("-------------------------------------------------")
else:
    print("Integer")
