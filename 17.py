
a = []
with open('17.txt') as f:
    a = [int(x.strip()) for x in f.readlines()]

k = len([x for x in a if x % 100 == 0])

res = 0
mx = -100_001
for i in range(len(a) - 1):
    pair = a[i:i + 2]
    if (pair[0] < 0 or pair[1] < 0) and sum(pair) < k:
        res += 1
        mx = max(mx, sum(pair))
print(res, mx)