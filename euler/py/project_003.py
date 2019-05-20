# https://projecteuler.net/problem=3

n = 600851475143
max = 0

i = n
while i > 1:
    f = 2
    while i >= f:
        if i%f == 0:
            i = i/f
            break
        f += 1
    print(f, i)
    if f > max:
        max = f

print("max", max)
