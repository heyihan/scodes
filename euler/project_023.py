# https://projecteuler.net/problem=23

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

def is_sum_of_abundant(n, meta):
    for i in range(1, n):
        if 2*i <= n and meta[i] == True and meta[n-i] == True:
            return True
    return False

arr = [False for i in range(0, 28124)]

for i in range(1, 28124):
    factors = proper_factors(i)
    if sum(factors) > i:
        arr[i] = True

sum = 0
for i in range(1, 28124):
    if is_sum_of_abundant(i, arr) == False:
        sum = sum + i

print(sum)


