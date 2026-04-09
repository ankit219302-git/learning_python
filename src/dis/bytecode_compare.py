import dis

from src.dis import compare
from src.dis.compare import square1, square2, increment1, increment2

'''
Because Python VM is stack-based, 
some code styles generate fewer bytecode instructions than others, 
which can slightly affect performance.
'''

print()
print("--------------Bytecode for square1() function in 'src.dis.compare'--------------\n")
dis.dis(square1)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print()

print()
print("--------------Bytecode for square2() function in 'src.dis.compare'--------------\n")
dis.dis(square2)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print()

print()
print("--------------Bytecode for increment1() function in 'src.dis.compare'--------------\n")
dis.dis(increment1)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print()

print()
print("--------------Bytecode for increment2() function in 'src.dis.compare'--------------\n")
dis.dis(increment2)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print()

print()
print("--------------Bytecode for entire compare module--------------\n")
dis.dis(compare)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print("\n-------------------------------------------------------------------------------------")
