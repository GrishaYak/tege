from turtle import *

tracer(0)

k = 5
for i in range(8):
    fd(20*k)
    rt(90)
    fd(37*k)
    rt(90)
up()
fd(13*k)
rt(90)
fd(15*k)
lt(90)
down()
for i in range(8):
    fd(210*k)
    rt(90)
    fd(354*k)
    rt(90)
    
up()
color('blue')
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*k, y*k)
        dot(3)
update()

n1 = 21 * 38
n2 = 211 * 355
intersection = 8 * 23
union = n1 + n2 - intersection
print(union)
while(True):
    pass