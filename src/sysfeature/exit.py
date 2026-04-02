import sys

'''
While running - 
python exit.py
Below code will exit with status 1, since the length of argv will be 1

While running -
python exit.py Ankit
Below code will exit with status 0, since the length of argv will now be 2
While running -

To check status, run command - 
'echo $?'
'''
if len(sys.argv) != 2:
    print("Missing commandline argument")
    sys.exit(1)
print(f"Hello, {sys.argv[1]}!")
exit(0)
