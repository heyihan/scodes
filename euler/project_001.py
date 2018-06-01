# https://projecteuler.net/problem=1

sum = 0

for n in range(1, 1000):
    if n%3==0 or n%5==0:
        #print(n)
        sum += n

print("sum", sum)
