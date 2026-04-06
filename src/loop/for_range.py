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
