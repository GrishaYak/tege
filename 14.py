def cnt0(n):
    if n == 0:
        return 1
    res = 0
    while n:
        res += n % 39 == 0
        n //= 39
    return res 

num = 39 ** 483 + 39 ** 235

mx = 0
for x in range(1, 9431):
    cur = cnt0(num-x)
    if cur > mx:
        mx = cur
        print(mx, x)
print(mx)