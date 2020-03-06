from math import *

n = int(input('Enter number: '))
p = [2, 3]
cnt = 2
a = 5
while cnt < n:
    b = 0
    for i in range(2, a):
        if i <= sqrt(a):
            if a % i == 0:
                print("a neprost", a)
                b = 1
            else:
                pass
    if b != 1:
        print("a prost", a)
        p += [a]
    cnt += 1
    a += 2
print(p)
