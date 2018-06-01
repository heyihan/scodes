# https://projecteuler.net/problem=2

sum = 0
a, b = 1, 2

while b < 4 * 1000 * 1000:
    if b%2 == 0:
        print(b)
        sum += b
    a, b = b, a+b

print("sum", sum)
