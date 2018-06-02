# https://projecteuler.net/problem=10
# https://en.wikipedia.org/wiki/Generating_primes

def find_primes_below(n):
    primes = []
    if n <= 1:
       return primes

    arr = [True for i in range(0, n)]

    i = 2
    while i < n:
        if arr[i]:
            if len(primes) < 1000 and len(primes)%100==0:
                print(i, len(primes))
            primes.append(i)
            j = i*i
            while j < n:
                if arr[j] and j%i == 0:
                    arr[j] = False
                j += 1
        i += 1
        j = 0
    return primes

def find_primes_below_2(n):
    primes = []
    if n <= 1:
        return primes

    arr = [i for i in range(2, n)]

    while len(arr) > 0:
        prime = arr[0]
        if prime * prime >= n:
            primes = primes + arr
            break
        if len(primes) < 1000 and len(primes)%100==0:
            print(prime, len(primes), len(arr))
        primes.append(prime)
        not_devided = []
        for i in arr[1:len(arr)]:
            if i%prime != 0:
                not_devided.append(i)
        arr = not_devided

    return primes

def devided_by(n, primes):
    for i in primes:
        if i*i > n:
            break
        if n%i == 0:
            return True
    return False

def find_primes_below_3(n):
    primes = []
    if n <= 1:
        return primes

    for i in range(2, n):
        if not devided_by(i, primes):
            primes.append(i)
            if len(primes)%10000==0:
                print(i, len(primes))

    return primes


print(10, find_primes_below(10))

#primes = find_primes_below(2*1000*1000)
#primes = find_primes_below_2(2*1000*1000)
primes = find_primes_below_3(2*1000*1000)
sum = 0
for i in primes:
    sum += i

print("sum", sum)

