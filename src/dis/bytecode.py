import dis

from src.csv import phonebook
from src.csv.phonebook import write_file

'''
dis module in python is the 'disassembler'.
'''
print()
print("--------------Bytecode for write_file() function in 'src.csv.phonebook'--------------\n")
dis.dis(write_file)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print()

print()
print("--------------Code info for write_file() function in 'src.csv.phonebook'--------------\n")
print(dis.code_info(write_file))
print()

print()
print("--------------Bytecode for entire 'src.csv.phonebook' module--------------\n")
dis.dis(phonebook)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print("\n-------------------------------------------------------------------------------------")
