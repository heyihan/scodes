# https://projecteuler.net/problem=21

def proper_factors(n):
    if n == 0 or n == 1:
        return []

    factors = [1]
    for i in range(2, n):
        if i*i > n:
            break
        if i*i == n:
            factors.append(i)
            break
        if n%i == 0:
            factors.append(i)
            factors.append(n/i)
    return factors

arr = [0 for i in range(0,10001)]

for i in range(1, 10000):
    factors = proper_factors(i)
    sum = 0
    for f in factors:
        sum = sum + f
    arr[i] = sum

sum = 0
for i in range(1, 10000):
    val = arr[i]
    val_2 = 0
    if val < 10000:
        val_2 = arr[val]
    else:
        factors = proper_factors(val)
        val_2 = 0
        for f in factors:
            val_2 = val_2 + f
    if val != i and val_2 == i:
        sum = sum + i
        print(i, val)
print(sum)
