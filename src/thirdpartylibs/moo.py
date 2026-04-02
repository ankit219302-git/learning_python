import cowsay
from cowsay import CHARS

name = input("What is your name? ")
cowsay.draw(f"Hello, {name}", CHARS["ghostbusters"], True)
