phonebook_names = []
with open("resources/phonebook") as file:
    for entry in file:
        phonebook_names.append(entry.strip().lower())

'''
Option 1 for searching phone book
'''

input_name = input("Enter name to search in phonebook: ")
for name in phonebook_names:
    if input_name.lower() == name:
        print(f"Name {input_name} FOUND in phonebook")
        break
# else can be used with loops as well (break statement should be present though)
# if break statement is reached, then else block is not run, otherwise else block will be executed once loop ends
else:
    print(f"Name {input_name} NOT FOUND in phonebook")

print()

'''
Option 2 for searching phone book
'''

input_name = input("Enter name to search in phonebook: ")
if input_name.lower() in phonebook_names:
    print(f"Name {input_name} FOUND in phonebook")
else:
    print(f"Name {input_name} NOT FOUND in phonebook")
