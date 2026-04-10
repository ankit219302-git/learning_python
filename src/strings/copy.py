original = input("Enter string to copy: ")
copy = original

print(f"Original: {original}")
print(f"Copy: {copy}")
print(f"Capitalised Copy: {copy.capitalize()}")
print(f"Uppercase Copy: {copy.upper()}")
print(f"Title Copy: {copy.title()}")
# first, last = copy.split("/")     # split() by default splits by spaces
# print(f"Split Copy (First): {first}")
# print(f"Split Copy (Last): {last}")
split_copy = copy.split()
print(f"Split Copy: {split_copy}")      # Will print a list with all the split words as elements
print(f"Split Copy (In reverse with indices in multiples of 2): {split_copy[::-2]}")

# Output -
#
# Enter string to copy: Hi my name is Ankit. I like to play Football!!
# Original: Hi my name is Ankit. I like to play Football!!
# Copy: Hi my name is Ankit. I like to play Football!!
# Capitalised Copy: Hi my name is ankit. i like to play football!!
# Uppercase Copy: HI MY NAME IS ANKIT. I LIKE TO PLAY FOOTBALL!!
# Title Copy: Hi My Name Is Ankit. I Like To Play Football!!
# Split Copy: ['Hi', 'my', 'name', 'is', 'Ankit.', 'I', 'like', 'to', 'play', 'Football!!']
# Split Copy (In reverse with indices in multiples of 2): ['Football!!', 'to', 'I', 'is', 'my']
