# compile() is a lower-level function that prepares code for execution without actually running it.
# It converts a string into a "code object" (bytecode) that can later be fed into eval() or exec().
#
# In addition to compiling source code to bytecode,
# compile supports compiling Abstract Syntax Trees (parse trees of Python code) into code objects;
# and source code into Abstract Syntax Trees
# [the ast.parse is written in Python and just calls compile(source, filename, mode, PyCF_ONLY_AST)];
# these are used for example for modifying source code on the fly, and also for dynamic code creation,
# as it is often easier to handle the code as a tree of nodes instead of lines of text in complex cases.
#
# Why is it easier -
# - Modifying code "on the fly": It is incredibly hard to reliably change code by editing strings (e.g., using string.replace).
#   It’s much safer to convert the code to a tree, swap a "Plus" node for a "Minus" node,
#   and then compile that modified tree back into bytecode.
# - Dynamic creation: If you are building a tool that generates code (like a macro or a data-science library),
#   it is easier to programmatically assemble a "tree of nodes"
#   than it is to manage indentation, colons, and parentheses in a long text string.


# The compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1) built-in can be used
# to speed up repeated invocations of the same code with exec or eval by compiling the source into a code object beforehand.
#
# The mode parameter controls the kind of code fragment the compile function accepts and the kind of bytecode it produces.
# The choices are 'eval', 'exec' and 'single'.


# 'eval' mode expects a single expression, and will produce bytecode that when run will return the value of that expression:
#   >>> dis.dis(compile('a + b', '<string>', 'eval'))
#       0           RESUME                   0
#
#       1           LOAD_NAME                0 (a)
#                   LOAD_NAME                1 (b)
#                   BINARY_OP                0 (+)
#                   RETURN_VALUE
print("\n---------- compile() with eval ----------")
a = 274
b = 806
eval_compiled_code = compile('a + b', '<string>', 'eval')
print(eval(eval_compiled_code))
print(exec(eval_compiled_code))         # This will print None as exec always returns None


# 'exec' accepts any kinds of python constructs from single expressions to whole modules of code,
# and executes them as if they were module top-level statements. The code object returns None:
#   >>> dis.dis(compile('a + b', '<string>', 'exec'))
#       0           RESUME                   0
#
#       1           LOAD_NAME                0 (a)
#                   LOAD_NAME                1 (b)
#                   BINARY_OP                0 (+)
#                   POP_TOP                               <- discard result
#                   RETURN_CONST             0 (None)     <- return None
print("\n---------- compile() with exec ----------")
c = 274
d = 806
operation = "*"
code_string = '''
while True:
    if operation == "+":
        print(c + d)
        break
    elif operation == "-":
        print(c - d)
        break
    elif operation == "*":
        print(c * d)
        break
    elif operation == "/":
        print(c / d)
        break
    print("Invalid Input")
    break
'''
exec_compiled_code = compile(code_string, '<string>', 'exec')
# Even though the above code contains multiple statements,
# compiling it with 'exec' mode into a code object can enable us to use it with eval(); the eval function will return None.
# This is sort of a way around the eval's single expression usage restriction,
# however, it is not intended to be used like that.
eval(exec_compiled_code)
exec(exec_compiled_code)


# 'single' is a limited form of 'exec' which accepts a source code
# containing a single statement (or multiple statements separated by ';')
# If the last statement is an expression statement, the resulting bytecode
# also prints the repr (string representation) of the value of that expression to the standard output.
#   >>> dis.dis(compile('a + b', '<string>', 'single'))
#       0           RESUME                   0
#
#       1           LOAD_NAME                0 (a)
#                   LOAD_NAME                1 (b)
#                   BINARY_OP                0 (+)
#                   CALL_INTRINSIC_1         1 (INTRINSIC_PRINT)        <- print to standard output once bytecode is executed
#                   POP_TOP
#                   RETURN_CONST             0 (None)                   <- return None.
#
# An 'if-elif-else' chain, a 'loop with else', and 'try with its except, else and finally' blocks are considered single statements.
# A source fragment containing 2 top-level statements is an error for the 'single'.
print("\n---------- compile() with single ----------")
multi_statement_single_compiled_code = compile(
    'print(f"{list(i for i in range(10))}"); print(list(f"Test {j}" for j in range(5))); print()', '<string>', 'single'
)
eval(multi_statement_single_compiled_code)
exec(multi_statement_single_compiled_code)

e = 274
f = 806
single_statement_single_compiled_code = compile(
    'e / f', '<string>', 'single'
)
# The below executions doesn't need print() statement with 'single'
# as 'single' mode, by default, prints the values
# if the last statement is an expression statement.
eval(single_statement_single_compiled_code)
exec(single_statement_single_compiled_code)
