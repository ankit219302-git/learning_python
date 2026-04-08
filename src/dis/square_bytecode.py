import dis

from src.dis.square import square1, square2

print()
print("--------------Bytecode for square1() function in 'src.dis.square'--------------\n")
dis.dis(square1)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print()

print()
print("--------------Bytecode for square2() function in 'src.dis.square'--------------\n")
dis.dis(square2)     # dis() function in dis module lets us see the bytecode instructions that Python generates from code.
print("\n-------------------------------------------------------------------------------------")
