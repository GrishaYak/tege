
with open('24.txt') as f:
    line = f.readline().strip()

l, k, ky = 0, 0, 0
line = line.replace('2025', '*')
mx = 0

for r in range(len(line)):
    if line[r] == '*':
        k += 1
    if line[r] == 'Y': 
        ky += 1
    while ky > 80:
        if line[l] == '*': k -= 1
        if line[l] == 'Y': ky -= 1
        l += 1
    if ky == 80 and k >= 90:
        mx = max(mx, r - l + 1 + 3 * k)
print(mx)
    