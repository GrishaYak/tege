from functools import lru_cache

def div(n):
    res = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            res |= {i, n//i}  
    return res

@lru_cache()
def isp(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def getm(n):
    p = sorted([d for d in div(n) if isp(d)])
    if len(p) >= 2:
        return p[-1] - p[0]
    return 0

k = 0
for x in range(8_117_600_757, 8_120_000_000):
    if k == 5:
        break
    m = getm(x)
    if m >= 1111 and str(m).count('1') >= 4 and isp(m):
        print(x, m)
        k += 1
        
# 8117601578 1117817
# 8117603854 11117
# 8117607130 811760711
# 8117608904 1014701111
# 8117611292 111119