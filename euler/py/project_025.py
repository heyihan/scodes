# https://projecteuler.net/problem=25

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

f1 = "1"
f2 = "1"

i = 2

while True:
    i = i +1
    f3 = sum_str(f1, f2)
    print(i, f3)
    if len(f3) >= 1000:
        break
    f1 = f2
    f2 = f3



