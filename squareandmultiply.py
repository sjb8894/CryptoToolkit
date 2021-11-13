
# z=x^c mod n

print("Enter numbers in format (Answer = x^c mod n):")

x = int(input("\nEnter x: "))
c = int(input("Enter c: "))
n = int(input("Enter n: "))

c = '{0:b}'.format(c)

answer = 1
length = len(c)

for i in range(0, length):
    answer = (answer * answer) % n
    if c[i] == "1":
        answer = (answer * x) % n

print("\nz = %d" % answer)
