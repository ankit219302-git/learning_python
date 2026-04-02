import csv
from csv import DictWriter

'''
If the file is opened simply using open() function, 
then it is necessary to close() the file after use to prevent any memory leaks.

However, if it opened in a 'with' statement and used within 'with' block,
then file is automatically closed once 'with' block's scope ends,
'''

def write_file(file_path):
    with open(file_path, "w") as file:
        name = input("Enter name: ")
        number = input("Enter number: ")

        writer = DictWriter(file, fieldnames=["Name", "Number"])
        writer.writeheader()        # This will write header in between entries if file is opened in append mode
        writer.writerow({"Name": name, "Number": number})


def append_file(file_path):
    with open(file_path, "a") as file:
        name = input("Enter name: ")
        number = input("Enter number: ")

        writer = DictWriter(file, fieldnames=["Name", "Number"])
        # This will write header in between entries whenever file is appended with values
        # writer.writeheader()
        writer.writerow({"Name": name, "Number": number})


def print_file_contents(file_path):
    print("\nReading file.....\n")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]} : {row[1]}")
    except FileNotFoundError:
        print("File not found!!")


choice = input("Do you want to overwrite (w) or append (a) file. Press any other key to read: ")

if choice.lower() == "w":
    write_file("resources/phonebook_dict.csv")
elif choice.lower() == "a":
    append_file("resources/phonebook_dict.csv")
else:
    print_file_contents("resources/phonebook_dict.csv")
