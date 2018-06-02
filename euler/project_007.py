# https://projecteuler.net/problem=7

def devided_by(n, primes):
    for i in primes:
        if i*i > n:
            break
        if n%i == 0:
            return True
    return False

def find_nth_prime(n):
    if n <= 0:
        return 0
    primes = []
    i = 2
    while n > 0:
        if not devided_by(i, primes):
            primes.append(i)
            n -= 1
        i += 1
    return primes[-1]

print(1, find_nth_prime(1))
print(6, find_nth_prime(6))
print(8, find_nth_prime(8))
print(10, find_nth_prime(10))
print(100, find_nth_prime(100))
print(1000, find_nth_prime(1000))

print(10001, find_nth_prime(10001))

