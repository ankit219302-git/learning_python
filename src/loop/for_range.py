def increment_and_print(stop_at=101):
    # Range function params -
    #   start: The first number we want (e.g., 1)
    #   stop: One value past the last number we want (e.g., 1 to stop at 0, or, 2 to stop at 1, etc.).
    #         101 in this case to stop at 100.
    #   step: Set to 1 to increment by 1
    for j in range(1, stop_at, 1):
        print('(', j, ')', sep= '', end=' ')
    print()

def decrement_and_print(start_at=100):
    # Reverse iteration can be done using below 2 ways -
    #
    # 1. Using the reversed() Function:
    #    The most readable and common way is to wrap our range object in the built-in reversed() function.
    #
    #    for i in reversed(range(5)):
    #       print(i)
    #    --> Output: 4, 3, 2, 1, 0
    #    This approach is often preferred because it is intuitive and clearly communicates that the intent is to iterate backward.
    #
    # 2. Using range() with a Negative Step:
    #    We can also manually set the start, stop, and step arguments within the range() function.
    #    start: The first number we want (e.g., 5)
    #    stop: One value past the last number we want (e.g., -1 to stop at 0, or, 0 to stop at 1, or, 1 to stop at 2, etc.)
    #    step: Set to -1 to decrement by 1
    #
    #    for i in range(5, -1, -1):
    #       print(i)
    #    --> Output: 5, 4, 3, 2, 1, 0
    for j in range(start_at, 0, -1):
        print('{', j, '}', sep='', end=' ')
    print()

if __name__ == '__main__':
    for i in [0, 1, 2]:
        print("test")

    print()

    for _ in [0, 1, 2]:     # This is just a convention followed to avoid i when not needed and not a necessity
        print("test without i")

    print()

    for _ in ["cat", "dog", "elephant"]:
        print("test with animal names")

    print()

    for _ in range(3):
        print("test with range & without i")

    print()

    before = input("Before: ")
    print("After: ", end="")
    for i in range(len(before)):
        print(before[i].upper(), end="")

    print()
    print("After (starting from 2nd index): ", end="")
    for i in range(2, len(before)):
        print(before[i].upper(), end="")

    print()
    #### SAMPLE OUTPUT FOR BELOW LOOP ####
    # Before: testing
    # After: TESTING
    # After (starting from 2nd index): STING
    # After (starting from -2 index): NGTESTING
    print("After (starting from -2 index): ", end="")
    for i in range(-2, len(before)):                    # This (-2) value can't be less than the input word length else out-of-bounds error will be thrown
        print(before[i].upper(), end="")

    print()
    print("After (increasing 2 indices at a time): ", end="")
    # This will increment the loop by 2 provided as the 3rd param of range function
    # 0 need not be given explicitly as the starting index is 0 by default
    for i in range(0, len(before), 2):
        print(before[i].upper(), end="")

    print("\n\n--------- range() with parameters test ---------")
    increment_and_print()
    decrement_and_print()
