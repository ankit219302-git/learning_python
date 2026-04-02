phonebook_names = []
with open("resources/phonebook", "r") as file:
    for line in file:
        phonebook_names.append(line.strip())

input_name = input("Enter name to search in phonebook: ")
for name in phonebook_names:
    if input_name.lower() == name.lower():
        print(f"Name {input_name} FOUND in phonebook")
        break
else:
    print(f"Name {input_name} NOT FOUND in phonebook")