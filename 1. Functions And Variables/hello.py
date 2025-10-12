# name = input("What is your name? ").strip().title()
# print("hello, " + name)
# print("hello, ", end = '')
# print(name)
# name = name.strip().title()
# print(f"hello, {name}")
# Positional parameters
# Named parameters


def main():
    name = input("What is your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)

main()