# https://projecteuler.net/problem=22

def str_score(s):
    sum = 0
    for c in s:
        sum = sum + (ord(c)-ord('A')+1) 
    return sum

f = open("data/project_022.dat", "r")
txt = f.read()
txt = txt.strip()
lst = txt.split(",")

names = [s.strip("\"") for s in lst]
names.sort()

i = 1
sum = 0
for name in names:
    score = str_score(name)
    sum = sum + score*i
    print(i, name, score, sum)
    i = i + 1



