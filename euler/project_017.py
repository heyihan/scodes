# https://projecteuler.net/problem=17

numberStr = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
        }

def number_2_en(n, meta):
    if n == 0:
        return []

    q = n / 1000
    if q > 0:
        ret = number_2_en(q, meta)
        ret.append("thousand")
        r = n % 1000
        if r > 0 and r < 100:
            ret.append("and")
        ret = ret + number_2_en(n % 1000, meta)
        return ret

    ret = []
    q = n / 100
    if q > 0:
        ret = [meta[q], "hundred"]
    r = n % 100
    if r > 0:
        if q > 0:
            ret.append("and")
        if r in meta:
            ret.append(meta[r])
        else:
            last1 = r%10
            last2 = r - r%10
            ret.append(meta[last2])
            ret.append(meta[last1])

    return ret

len_sum = 0
for i in range(1, 1002):
    arr = number_2_en(i, numberStr)
    l = len(''.join(arr))
    len_sum = len_sum + l
    print(i, arr, l, len_sum)

