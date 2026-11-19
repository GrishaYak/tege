from itertools import product

def f():
    return w and ((x<=y) == (y<=z))

for x, y, z, w in product((0, 1), repeat=4):
    if f():
        print(x, z, w, y)