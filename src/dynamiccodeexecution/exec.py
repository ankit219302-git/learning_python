initial_sum = 10
# Could be a normal string instead of an f-string
code_block = f'''
def calculate_series_sum(series_range):
    series_sum = {initial_sum}
    for num in range(series_range + 1):
        series_sum += num
    return series_sum
'''
# One might think that the above code can be made simpler by directly
# incrementing & returning the initial_sum inside calculate_series_sum(series_range).
# Something like this -
#
# initial_sum = 10
# code_block = f'''
# def calculate_series_sum(series_range):
#     for num in range(series_range + 1):
#         initial_sum += num
#     return initial_sum
# '''
#
# However, this code block will throw error since the variable initial_sum
# is not visible inside the function 'calculate_series_sum(series_range)'.
# Because we are assigning a value to it inside the function, Python treats it as a local variable.
# However, we never initialized it inside the function — it only exists in the global scope.
#
# If we want the function to use the variable from the outside world,
# one way is by explicitly telling Python it is global.
#
# initial_sum = 10
# code_block = f'''
# def calculate_series_sum(series_range):
#     global initial_sum        # Tells Python to look outside the function
#     for num in range(series_range + 1):
#         initial_sum += num
#     return initial_sum
# '''

num_range = 100
# The exec() function in Python is a built-in utility used for the dynamic execution of Python code that always returns None.
# It can take a string or a code object and run it as a set of Python statements.
# Unlike eval(), which only handles single expressions,
# exec() can run complex code including loops, function definitions, class definitions, and imports.
# SHOULD NOT BE USED GENERALLY as it is highly dangerous when used with untrusted input.
# Because it can run arbitrary code, a malicious user could let's say
# provide a string that deletes files (e.g., import os; os.system('rm -rf *')), or access sensitive data.
exec(code_block)
print(f"Series sum from 0 to {num_range} (with added initial sum : {initial_sum}) = {calculate_series_sum(num_range)}")
