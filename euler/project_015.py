# https://projecteuler.net/problem=15

def c_n_k(n, k):
    arr = [0 for i in range(0,k+1)]
    for i in range(1, n+1):
        j = i
        while j > 0:
            if j == 1:
                val = i
            elif j == i:
                val = 1
            elif j <= k:
                val = arr[j-1] + arr[j]

            if j <= k:
                arr[j] = val
            j = j - 1
#        print(arr)
    return arr[k]

print(4, 2, c_n_k(4,2))
print(4, 3, c_n_k(4,3))
print(10, 3, c_n_k(10,3))
print(40, 20, c_n_k(40,20))
