choice = input("Do you agree? [yes(y)/no(n)] ")
# if choice == "Y" or choice == "y":
#     print("Agreed")
# elif choice == "N" or choice == "n":
#     print("Not Agreed")
# else:
#     print("Invalid input")

choice = choice.lower()
if choice in ["y", "yes"]:
    print("Agreed")
elif choice in ["n", "no"]:
    print("Not Agreed")
else:
    print("Invalid input")
