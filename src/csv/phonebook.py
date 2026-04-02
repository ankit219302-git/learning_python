import csv

'''
If the file is opened simply using open() function, 
then it is necessary to close() the file after use to prevent any memory leaks.

However, if it opened in a 'with' statement and used within 'with' block,
then file is automatically closed once 'with' block's scope ends,
'''

def write_file(file_path):
    file = open(file_path, "a")

    name = input("Enter name: ")
    number = input("Enter number: ")

    writer = csv.writer(file)
    writer.writerow([name, number])
    file.close()


def print_file_contents(file_path):
    try:
        print("\nReading file.....\n")
        contacts = {}
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                contacts[row[0]] = row[1]
                print(f"{row[0]} : {row[1]}")
        print()
        print(contacts)  # Dictionary used just for learning and is not needed since printing can be done using reader itself
    except FileNotFoundError:
        print("File not found!!")


choice = input("Do you want to write to file (y/n): ")

if choice.lower() == "y":
    write_file("resources/phonebook.csv")
else:
    print_file_contents("resources/phonebook.csv")
