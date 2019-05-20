# https://projecteuler.net/problem=4

def palindromic(n):
    reverse = 0
    i = n
    while i > 0:
        reverse = reverse*10 + i%10
        i = i/10
    #print(n, reverse)
    return reverse == n

max = 0
for i in range(100,1000):
    for j in range(100, i+1):
        if palindromic(i*j) and i*j > max:
            print(i, j, i*j)
            max = i*j
