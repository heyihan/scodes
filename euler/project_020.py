# https://projecteuler.net/problem=20

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

def str_x_n(s, n):
    if n == 0:
        return ""
    if n > 10:
        low = str_x_n(s, n%10)
        high = str_x_n(s, n/10)
        return sum_str(high+"0", low)

    reverse = reverse_str(s)

    add = 0
    result = []
    for c in reverse:
        m = int(c)*n + add
        add = m/10
        r = m%10
        result.append(str(r))
    if add > 0:
        result.append(str(add))

    return reverse_str(''.join(result))

def sum_str_digits(s):
    sum = 0
    for c in s:
        sum = sum + int(c)
    return sum

xret = "1"
for i in range(2, 101):
    xret = str_x_n(xret, i)
    print(i, len(xret), xret)


print(xret, sum_str_digits(xret))
