# Python program for EEA

def eea(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = eea(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def main():
    val1 = input("Enter the value for a in (a, b): ")
    val2 = input("Enter the value for b in (a, b): ")

    gcd, x, y = eea(int(val1), int(val2))
    print(f'{val1}x + {val2}y = gcd({val1}, {val2})')
    print(f"x = {x}, y = {y}")


main()
