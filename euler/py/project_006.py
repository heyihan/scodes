# https://projecteuler.net/problem=6

def sum_of_square(n):
    sum = 0
    while n > 0:
        sum += n*n
        n -= 1
    return sum

def square_of_sum(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    return sum*sum

sum = sum_of_square(100)
square = square_of_sum(100)

print(sum, square, square-sum)
