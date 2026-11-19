from functools import lru_cache

@lru_cache()
def f(n):
    if n == 28 or n < 1:
        return 0
    if n == 1:
        return 1
    res = f(n - 2)
    if n % 2 == 0:
        res += f(n//2)
    res += f(n-3)
    return res

print(f(98))