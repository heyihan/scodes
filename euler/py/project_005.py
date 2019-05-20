# https://projecteuler.net/problem=5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(1,6))

result = 1
for i in range(2, 21):
    g = gcd(result, i)
    result = result * (i/g)
    print(i, g, result)

print(result)

