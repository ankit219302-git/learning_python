from sys import argv

'''
While running - 
python greet_commandline.py
python argv by default has one value, i.e., 'greet_commandline.py'

While running -
python greet_commandline.py Ankit
python argv now has 2 values, i.e., 'greet_commandline.py' and 'Ankit'
'''
if len(argv) == 2:
    print(f"Hello, {argv[1]}!")
else:
    print("Hello, world!")
