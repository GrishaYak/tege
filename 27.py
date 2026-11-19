from math import dist
f = open('27.txt')
a = [line.replace(',', '.').strip().split() for line in f.readlines()]
a = [[float(el[0]), float(el[1]), el[2]]for el in a]
f.close()
print(a[0])
print(len(a))

cl = [[],[],[]]
cl[0] = [el for el in a if el[1] > 22]
cl[1] = [el for el in a if el[1] < 22 and el[0] < 22]
cl[2] = [el for el in a if el[0] > 22]
print(len(cl[0]), len(cl[1]), len(cl[2]))

def b1(arr1, arr2):
    a1 = [el[:2] for el in arr1 if el[-1][0] == 'J']
    a2 = [el[:2] for el in arr2 if el[-1][0] == 'J']
    res = 1e9
    for el1 in a1:
        for el2 in a2:
            cur = dist(el1, el2)
            if cur < res:
                res = cur
    return res

def b2(arr1, arr2):
    a1 = [el[:2] for el in arr1 if el[-1][0] == 'J']
    a2 = [el[:2] for el in arr2 if el[-1][0] == 'J']
    res = 0
    for el1 in a1:
        for el2 in a2:
            cur = dist(el1, el2)
            if cur > res:
                res = cur
    return res

print(int(b1(cl[0], cl[1]) * 10_000))
print(int(b2(cl[0], cl[2]) * 10_000))