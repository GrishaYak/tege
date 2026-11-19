def f(a, b, n, m):
    if a + b >= 207:
        return n % 2 == m % 2
    n += 1
    if n > m:
        return False
    h = [f(a+1,b,n, m),f(a*2,b,n, m),f(a,b+1,n,m),f(a,b*2,n,m)]
    if n % 2 == m % 2:
        return any(h)
    return all(h)

print(20, [b for b in range(2, 190) if f(17, b, 0, 3) and not f(17, b, 0, 1)])
print(21, [b for b in range(2, 190) if f(17, b, 0, 4) and not f(17, b, 0, 2)])
