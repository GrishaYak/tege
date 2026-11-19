from math import ceil
l = 117

k = 256_473
V = 48 * (1<<20)

for i in range(20):
    if ceil(i * l / 8) * k <= V:
        print(1<<i, (ceil(i * l / 8) * k) / (2**20))