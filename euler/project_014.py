# https://projecteuler.net/problem=14

def collatz_count(n, arr):
    if n<len(arr) and arr[n] > 0:
        return arr[n]
    if n == 1:
        arr[n] = 1
        return 1

    if n%2 == 0:
        cnt = collatz_count(n/2, arr)+1
    else:
        cnt = collatz_count(3*n+1, arr)+1
    if n < len(arr):
        arr[n] = cnt
    return cnt

arr = [0 for i in range(0, 1000000)]

max = 0
n = 0
for i in range(2, 1000000):
    cnt = collatz_count(i, arr)
    if cnt > max:
        max = cnt
        n = i

print(max, n)
