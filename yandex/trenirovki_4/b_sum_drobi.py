from math import gcd

d1, z1, d2, z2 = map(int, input().split())

ans = d1 * z2 + d2 * z1, z1 * z2

mmin = gcd(*ans)

print(int(ans[0]/mmin), int(ans[1]/mmin))
