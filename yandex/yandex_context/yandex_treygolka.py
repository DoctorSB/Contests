d = int(input())
X = input().split()
X = [int(i) for i in X]
a = [0, 0]
b = [d, 0]
c = [0, d]

f = (a[0] - X[0]) * (b[1] - a[1]) - (b[0] - a[0]) * (a[1] - X[1])
s = (b[0] - X[0]) * (c[1] - b[1]) - (c[0] - b[0]) * (b[1] - X[1])
t = (c[0] - X[0]) * (a[1] - c[1]) - (a[0] - c[0]) * (c[1] - X[1])

if (f > 0 and s > 0 and t > 0) or (f < 0 and s < 0 and t < 0):
    print(0)
elif (f == 0 or s == 0 or t == 0):
    print(0)
else:
    minimal = min(f, s, t)
    if minimal == t:
        print(1)
    elif minimal == s:
        print(2)
    elif minimal == f:
        print(3)
