import dis

'''
Comprehensions are often faster than normal loops, and the reason becomes obvious when you inspect the bytecode.
There are multiple types of comprehensions:

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1. List Comprehensions
List comprehensions allow for the creation of lists in a single line, improving efficiency and readability. They follow a specific pattern to transform or filter data from an existing iterable.

Syntax:
[expression for item in iterable if condition]

expression: Operation applied to each item.
item: Variable representing the element from the iterable.
iterable: The source collection.
condition (optional): A filter to include only specific items.

Example: Generating a list of even numbers
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [num for num in a if num % 2 == 0]
print(res)

Output -
[2, 4, 6, 8]
Explanation: This creates a list of even numbers by filtering elements from a that are divisible by 2.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Dictionary comprehension
Dictionary Comprehensions are used to construct dictionaries in a compact form, making it easy to generate key-value pairs dynamically based on an iterable.

Syntax:
{key_expression: value_expression for item in iterable if condition}

key_expression: Determines the dictionary key.
value_expression: Computes the value.
iterable: The source collection.
condition (optional): Filters elements before adding them.

Example 1: Creating a dictionary of numbers and their cubes
res = {num: num**3 for num in range(1, 6)}
print(res)

Output -
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
Explanation: This creates a dictionary where keys are numbers from 1 to 5 and values are their cubes.

Example 2: Mapping states to capitals
a = ["Texas", "California", "Florida"] # states
b = ["Austin", "Sacramento", "Tallahassee"] # capital
res = {state: capital for state, capital in zip(a, b)}
print(res)

Output -
{'Texas': 'Austin', 'California': 'Sacramento', 'Florida': 'Tallahassee'}
Explanation: zip() function pairs each state with its corresponding capital, creating a dictionary.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
3. Set comprehensions
Set Comprehensions are similar to list comprehensions but result in sets, automatically eliminating duplicate values while maintaining a concise syntax.

Syntax:
{expression for item in iterable if condition}

expression: The operation applied to each item.
iterable: The source collection.
condition (optional): Filters elements before adding them.

Example: Extracting unique even numbers
a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
res = {num for num in a if num % 2 == 0}
print(res)

Output -
{2, 4, 6}
Explanation: This creates a set of even numbers from a, automatically removing duplicates.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
4. Generator comprehensions
Generator Comprehensions create iterators that generate values lazily, making them memory-efficient as elements are computed only when accessed.

Syntax:
(expression for item in iterable if condition)

expression: Operation applied to each item.
iterable: The source collection.
condition (optional): Filters elements before including them.

Example: Generating even numbers using a generator
res = (num for num in range(10) if num % 2 == 0)
print(list(res))

Output -
[0, 2, 4, 6, 8]
Explanation: This generator produces even numbers from 0 to 9, but values are only computed when accessed.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Reference - https://www.geeksforgeeks.org/python/comprehensions-in-python/
'''

def list_loop_version():
    result = []
    for i in range(5):
        result.append(i*i)
    return result

'''
This is an example of list comprehension.
It is a concise, single-line syntax in Python used to create new lists from existing iterables (like lists, strings, or ranges). 
It serves as a readable and often faster alternative to traditional loops.
'''
def list_comprehension_version():
    return [i*i for i in range(5)]

if __name__ == "__main__":
    print()
    print("--------------Bytecode for list_loop_version()--------------\n")
    dis.dis(list_loop_version)
    print()

    print()
    print("--------------Bytecode for list_comprehension_version()--------------\n")
    dis.dis(list_comprehension_version)
    print("\n-------------------------------------------------------------------------------------")

    # Output -
    # --------------Bytecode for list_loop_version()--------------
    #
    # 101           RESUME                   0
    #
    # 102           BUILD_LIST               0
    #               STORE_FAST               0 (result)
    #
    # 103           LOAD_GLOBAL              1 (range + NULL)
    #               LOAD_CONST               1 (5)
    #               CALL                     1
    #               GET_ITER
    #       L1:     FOR_ITER                22 (to L2)
    #               STORE_FAST               1 (i)
    #
    # 104           LOAD_FAST                0 (result)
    #               LOAD_ATTR                3 (append + NULL|self)
    #               LOAD_FAST_LOAD_FAST     17 (i, i)
    #               BINARY_OP                5 (*)
    #               CALL                     1
    #               POP_TOP
    #               JUMP_BACKWARD           24 (to L1)
    #
    # 103   L2:     END_FOR
    #               POP_TOP
    #
    # 105           LOAD_FAST                0 (result)
    #               RETURN_VALUE
    #
    #
    # --------------Bytecode for list_comprehension_version()--------------
    #
    #  112           RESUME                   0
    #
    #  113           LOAD_GLOBAL              1 (range + NULL)
    #                LOAD_CONST               1 (5)
    #                CALL                     1
    #                GET_ITER
    #                LOAD_FAST_AND_CLEAR      0 (i)
    #                SWAP                     2
    #        L1:     BUILD_LIST               0
    #                SWAP                     2
    #                GET_ITER
    #        L2:     FOR_ITER                 7 (to L3)
    #                STORE_FAST_LOAD_FAST     0 (i, i)
    #                LOAD_FAST                0 (i)
    #                BINARY_OP                5 (*)
    #                LIST_APPEND              2
    #                JUMP_BACKWARD            9 (to L2)
    #        L3:     END_FOR
    #                POP_TOP
    #        L4:     SWAP                     2
    #                STORE_FAST               0 (i)
    #                RETURN_VALUE
    #
    #   --   L5:     SWAP                     2
    #                POP_TOP
    #
    #  113           SWAP                     2
    #                STORE_FAST               0 (i)
    #                RERAISE                  0
    # ExceptionTable:
    #   L1 to L4 -> L5 [2]
    #
    # -------------------------------------------------------------------------------------
    #
    #
    # ----Explanation----
    #
    # Notice this part in loop bytecode:
    # LOAD_ATTR                3 (append + NULL|self)
    # Python must look up the append method every iteration.
    # That adds overhead.
    #
    # Now, notice this part in list comprehension bytecode:
    # LIST_APPEND              2
    # This is a special optimized opcode (operation code).
    # It avoids method lookup, hence is faster.
    #
    #
    # --Key Takeaway--
    # List comprehensions are faster because:
    #
    # normal loop → method calls
    # list comprehension → specialized opcode
    #
    # Specifically:
    # append()  vs  LIST_APPEND
