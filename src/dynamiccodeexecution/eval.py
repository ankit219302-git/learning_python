# eval() is like exec() except eval() is designed to process a single expression and return its value.
# eval() only accepts an expression.
# An expression is something that evaluates to a value (e.g., 2 + 2 or abs(-5)).
# More simply, in Python, an expression is whatever you can have as the value in a variable assignment:
#       a_variable = (anything you can put within these parentheses is an expression)
# We cannot use assignments (like x = 5) or loops inside eval().

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
expression = 'a + b'
result = eval(expression)

print(f"Sum of {a} and {b} = {result}")
