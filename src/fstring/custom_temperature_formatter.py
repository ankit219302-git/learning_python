"""
How f-Strings Work Internally :

When Python sees:
f"{value:specifier}"

it internally does:
format(value, "specifier")

which calls:
value.__format__("specifier")

So objects can customize how they appear by implementing the __format__() method.
"""

class Temperature:
    def __init__(self, temp_celsius):
        self.temp_celsius = temp_celsius
    def __format__(self, format_spec):
        if format_spec == "c":
            return f"{self.temp_celsius}°C"
        elif format_spec == "f":
            return f"{self.temp_celsius * 9 / 5 + 32}°F"
        else:
            raise ValueError(f"Invalid format: {format_spec}. Only Celsius(c) and Fahrenheit(f) supported.")
