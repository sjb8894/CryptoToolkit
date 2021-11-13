def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def main():
    a = 342
    b = 4353
    print(gcd(a, b))

main()