# https://projecteuler.net/problem=16

def reverse_str(s):
    return s[::-1]

def sum_str(a, b):
    if len(b) > len(a):
        return sum_str(b, a)

    reverseA = reverse_str(a)
    reverseB = reverse_str(b)

    i = 0
    add = 0
    result = []
    while i < len(a):
        o1 = int(reverseA[i])
        o2 = 0
        if i < len(b):
            o2 = int(reverseB[i])
        r = (o1+o2+add)%10
        add = (o1+o2+add)/10
        result.append(str(r))
        i = i + 1
    if add > 0:
        result.append(str(add))

    return reverse_str(''.join(result))

print("123", "124", sum_str("123", "124"))
print("123", "12499889888", sum_str("123", "12499889888"))

sum = "2"
for i in range(1, 1000):
    sum = sum_str(sum, sum)
    print(sum, len(sum));

addsum = 0
for c in sum:
    addsum = addsum + int(c)
print(sum, addsum)

