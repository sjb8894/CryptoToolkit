# Russian Peasant Algorithm

def main():
    a = int('0x1E', 16)
    b = int('0x37', 16)

    z = 0
    aes = int("0x11B", 16)
    while a > 0:
        if a % 2 == 1:
            z = z ^ b
        b = b << 1  # binary shift left
        a = a >> 1  # binary shift right

    res = z % aes

    print(hex(res))


main()