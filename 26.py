f = open('26.txt')
n = int(f.readline())

a = [int(x) for x in f.readlines()]
a.sort(reverse=True)

k = 1
last = a[0]
for i in range(1, n):
    if last - a[i] < 8:
        continue
    k += 1
    print(last)
    last = a[i]

print(k, last)