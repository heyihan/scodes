# https://projecteuler.net/problem=12

def all_factors(n):
    if n == 0:
        return []
    if n == 2:
        return [1]

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
    factors.append(n)
    return factors

def sum(n):
    return n*(n+1)/2

def factor2Count(n):
    result = 0
    while n > 0 and  n%2 == 0:
        result += 1
        n = n/2
    return  result

count = 1
countOf2 = 0

for i in range(1, 100000):
    n = i + 1
    factors = all_factors(n)
    countOfN = len(factors)
    countOf2N = factor2Count(i*n)
    allcount = (countOfN*count*countOf2N/(countOf2N+1))
    if i%1000 == 0:
        print(i, countOfN, countOf2N, count, allcount, factors)
    if allcount > 500:
        print(i, countOfN, countOf2N, count, allcount, factors)
        print(i, i*n/2)
        break
    count = countOfN

