from itertools import product

alp = ['д', 'ж', 'з', 'о', 'у', 'ф', 'ч', 'ю', 'я']
print(alp)
k = 0
for t in product(alp, repeat=6):
    k += 1
    s=''.join(t)
    print(k, s)
    if k % 2 and 'у' not in s[0] + s[-1] and 'юю' in s:
        break