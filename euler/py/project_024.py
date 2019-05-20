# https://projecteuler.net/problem=24

def n_x(n):
    ret = 1
    for i in range(2, n+1):
        ret = ret * i
    return ret

def n_2_nx(n):
    k = 1
    while n > n_x(k):
        k = k + 1
    if n == n_x(k):
        return k, 0, 0
    kx = n_x(k-1)
    cnt = n/kx
    if n%kx == 0:
        return k, cnt-1, n%kx
    return k, cnt, n%kx

def find_nth(n):
    arr = [i for i in range(0,10)]

    r = n
    p = 0
    while True:
        k, cnt, r = n_2_nx(r)
        print(k, cnt, r)
        if k == 1:
            break
        p = 10-k
        if cnt > 0:
            tmp = arr[p+cnt]
            for i in range(0,cnt):
                arr[p+cnt-i] = arr[p+cnt-i-1]
            arr[p] = tmp
            p = p+1
        if r == 0:
            arr = arr[:p] + arr[p:][::-1]
            break

    return arr

print(1000000, find_nth(1000000))
for i in range(1, 30):
    print(i, find_nth(i))
