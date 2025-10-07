# x = int(input("What is x? "))
# y = int(input("What is y? "))
# x = float(input("What is x? "))
# y = float(input("What is y? "))
# z = int(x) + int(y)
# z = round(x + y,2)
# z = x/y
# print(f"{z:,}")
# print(f"{z:.2f}")


def main():
    x = int(input("What's x? "))
    print(f"{x} squared is", square(x))


def square(n):
    return pow(n, 2)

main()