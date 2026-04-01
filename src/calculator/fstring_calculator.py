import datetime

'''
---- Python f-String Format Cheat Sheet ----
    {value:[fill][align][sign][width][.precision][type]}

    Example:
    f"{value:*>+10.2f}"

    1.  '*' is the custom fill character to pad the value with. If no value is provided, space is used as default padding.
    2.  '>' is the alignment to be done
            <	Left align (like string.ljust() - left justified)
            >	Right align	(like string.rjust() - right justified)
            ^	Center align (like string.center())
    3.  '+' is the sign behaviour to be adopted
            +	Always show sign
            -	Only show negative sign (default)
            space	Show space for positive numbers
    4.  '10' is the minimum field width that the value need to occupy including the padded fill, sign and precision.
        If the specified width is less than the actual value that needs to be displayed, 
        then the value is displayed completely, even if it exceeds the specified width.
    5.  '.2' is the precision - the number of decimal places to be used
    6.  'f' is the type (float in this case) in which the value is to be depicted
            f	Float
            d	Integer
            b	Binary
            o	Octal
            x	Hex (lower)
            X	Hex (upper)
            %	Percentage
'''

x = int(input("x: "))
y = int(input("y: "))
operation = input("Operation [+,-,/,x,%(modulus)]: ")
# :.{number_value}f forces the output to format as a rounded (if needed) floating point number upto {number_value} decimal places
# Python has floating point imprecision which is observed post 15 decimal places
# Similarly, if :.0f is used it will forcefully remove any decimal representation even when dealing with float values
if operation == "+":
    print(f"The sum is: {(x + y):.13f}")        # This forces the output to print as a floating point number till 13 decimal places
elif operation == "-":
    diff = x - y
    print(f"The difference is: <{diff:/^ 12.1f}>")      # Display '12' width diff as a 'float' type, padded with '/', having precision '1', and sign as 'space' for positive numbers
elif operation == "/":
    print(f"The division quotient is: {(x / y):.19f}")      # Forced floating point number printing till 19 decimal places
elif operation == "x":
    print(f"The product is: {x * y}")
elif operation == "%":
    print("The modulus is:", x % y)
else:
    print("Invalid operation")

print()
newline_unicode = f"Newline unicode: {ord('\n')}"
print(f"---Newline: {'\n'}---")
print(newline_unicode)
# Date fstring formatting
today = datetime.datetime.today()
print(f"Today is : {today:%B %d, %Y}")
