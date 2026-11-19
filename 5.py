def to2(n):
    return bin(n)[2:]

def r(n):
    d = to2(n)
    if n % 7 == 0:
        d += '01'
    else:
        d += to2(n // 7)
    return int(d, 2)

for n in range(1, 1300, 2):
    R = r(n)
    if R<=1300:
        print(n, R)