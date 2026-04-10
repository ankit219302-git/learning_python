import time

'''
Built-in functions are much faster than user-defined Python functions. 
The reason lies in how CPython (Python interpreter) executes them internally.

Built-ins does not execute Python bytecode.
Instead it calls C code directly inside the CPython interpreter.

So the execution becomes:
    Python → C function → result
No Python stack frame needed.
That’s why built-ins are fast.

Built-ins avoid:
- Python bytecode interpretation
- function frame creation
- stack manipulation
- dynamic type overhead
Instead they run native machine code in C.

Putting everything together:
Python source code
        ↓
compiled to bytecode
        ↓
Python Virtual Machine executes instructions
        ↓
when built-in functions appear
        ↓
jump into optimized C implementation
'''

def num_sum(num_list):
    val = 0
    for num in num_list:
        val += num
    print(f"User-defined sum = {val}")

if __name__ == "__main__":
    nums = list(range(10000))
    print("\n")
    start_time = time.time()
    num_sum(nums)
    print(f"Time taken for user-defined sum function : {time.time() - start_time} seconds")

    print("\n")
    start_time = time.time()
    print(f"Built-in sum = {sum(nums)}")
    print(f"Time taken for built-in sum function : {time.time() - start_time} seconds")
