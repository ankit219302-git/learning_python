# List of dictionaries (each dictionary entry has 2 key-value pairs)
phonebook = [
    {"name": "Gojo", "number": "+91 8291111111"},
    {"name": "Saitama", "number": "+91 8291111112"},
    {"name": "Levi", "number": "+91 8291111113"},
    {"name": "L", "number": "+91 8291111114"}
]

print("--------With List of dictionaries--------", end="\n\n")

'''
Option 1 for searching phone book numbers
'''

print("!! Option 1 !!")

input_name = input("Enter name to search in phonebook: ")
for entry in phonebook:
    if input_name.lower() == entry["name"].lower():
        print(f"{input_name} FOUND in phonebook with number {entry["number"]}")
        break
else:
    print(f"{input_name} NOT FOUND in phonebook")

print()

'''
Option 2 for searching phone book numbers
'''

print("!! Option 2 !!")

input_name = input("Enter name to search in phonebook: ")
'''
[record["name"].lower() for record in phonebook] is an example of list comprehension.
It is a concise, single-line syntax in Python used to create new lists from existing iterables (like lists, strings, or ranges). 
It serves as a readable and often faster alternative to traditional loops.
'''
if input_name.lower() in [record["name"].lower() for record in phonebook]:
    # Here number can't be printed without looping because we don't have access to record variable
    print(f"{input_name} FOUND in phonebook")
else:
    print(f"{input_name} NOT FOUND in phonebook")

phonebook_lowercase = {record["name"].lower(): record["number"] for record in phonebook}
if input_name.lower() in phonebook_lowercase:
    print(f"{input_name} FOUND in phonebook with number {phonebook_lowercase[input_name.lower()]}")
else:
    print(f"{input_name} NOT FOUND in phonebook")

print()
print("--------With Python dictionary--------", end="\n\n")

# This is what a dictionary in Python looks like
phonebook_dict = {
    "Gojo": "+91 8291111111",
    "Saitama": "+91 8291111112",
    "Levi": "+91 8291111113",
    "L": "+91 8291111114"
}

'''
Option 1 for searching phone book numbers
'''

print("!! Option 1 !!")

name = input("Enter name to search in phonebook: ")
for contact_name in phonebook_dict:
    if name.lower() == contact_name.lower():
        print(f"{name} FOUND in phonebook with numer {phonebook_dict[contact_name]}")
        break
else:
    print(f"{name} NOT FOUND in phonebook")

print()

'''
Option 2 for searching phone book numbers
'''

print("!! Option 2 !!")

name = input("Enter name to search in phonebook: ")
if name.lower() in {k.lower(): v for k, v in phonebook_dict.items()}:
    # Here number can't be printed without looping because we don't have access to lowercase converted dict
    print(f"{name} FOUND in phonebook")
else:
    print(f"{name} NOT FOUND in phonebook")

# If you want to print the number, convert the dict to lowercase and store in a variable
phonebook_dict_lowercase = {k.lower(): v for k, v in phonebook_dict.items()}
if name.lower() in phonebook_dict_lowercase:
    print(f"{name} FOUND in phonebook with number {phonebook_dict_lowercase.get(name.lower())}")
else:
    print(f"{name} NOT FOUND in phonebook")
