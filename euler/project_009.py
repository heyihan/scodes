# https://projecteuler.net/problem=9

succ = False

for a in range(1, 333):
    for b in range(a+1, 500):
        c = 1000 - a -b
        if c <= b:
            break
        if a*a + b*b == c*c:
            succ = True
            break
    if succ:
        break

print(a, b, c, a*b*c)

