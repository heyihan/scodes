# https://projecteuler.net/problem=26

def digits_to_str(arr):
    ret = ''
    for n in arr:
        ret = ret + str(n)
    return ret

def find_x(arr, n):
    i = 0
    while i < len(arr) and arr[i] != n:
        i += 1
    return i

def cycle_len(d):
    qlist = []
    rlist = []
    r = 1

    while r>0 and r not in rlist:
        rlist.append(r)
        q = r*10/d
        r = r*10%d
        qlist.append(q)

    idx = find_x(rlist, r)
    ret = len(rlist) - idx
    
    if ret == 0:
        print("1/" + str(d) + " 0." + digits_to_str(qlist))
    else:
        print("1/" + str(d) + " 0." + digits_to_str(qlist) + "(" +digits_to_str(qlist[idx:])+") cycle " + str(ret))

    return ret


max_cycle = 0
max_d = 0
for d in range(2, 1000):
    cycle = cycle_len(d)
    if cycle > max_cycle:
        max_cycle = cycle
        max_d = d
print(max_d, " cycle ", max_cycle)
