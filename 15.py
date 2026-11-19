def in_p(x):
    return 2508 <= x <= 2570

def check(x):
    return x % A == 0 or in_p(x) <= (x % 214 != 0 or x + A <= 5286)

for A in range(1, 6000):
    if all(check(x) for x in range(1, 10_000)):
        print(A)