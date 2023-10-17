n, s = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
max_p = 0
for i in prices:
    if i >= max_p and s >= i:
        max_p = i

print(max_p)
