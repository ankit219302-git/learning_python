# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hello(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
"""

if __name__ == '__main__':

This line is one of the most important patterns in Python. 
It controls whether a file runs as a program or behaves as a module.

🥊 Case 1 — File Is Run Directly

Example:
python hello.py

In this case Python sets:
__name__ = "__main__"

So this condition becomes true:
if __name__ == "__main__":
and the code inside runs.

Example:
def print_hello(name):
    print(f"Hello, {name}")
if __name__ == "__main__":
    print_hello("PyCharm")

Output:
Hello, PyCharm

🥊 Case 2 — File Is Imported

Example:
from hello_world.hello import print_hello
print_hello("World")

Now Python sets:
__name__ = "hello_world.hello"

So this condition becomes false:
if "main" == "__main__"
Therefore the code inside the block does NOT run.

Output:
Hello, World

If you remove the check:
def print_hello(name):
    print(f"Hello, {name}")
print_hello("PyCharm")

Then this code 'print_hello("PyCharm")' runs every time the file is imported.

Example:
from hello_world.hello import print_hello
print_hello("World")

Output:
Hello, PyCharm
Hello, World

"""
if __name__ == '__main__':
    print_hello('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
