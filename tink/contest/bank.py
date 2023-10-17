def rob_money(a, n):
    m = len(a)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1
    print(dp)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - a[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)
    res = []

    i, j = m, n
    print(i, j)
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            res.append(a[i - 1])
            j -= a[i - 1]
        i -= 1

    return res


n, m = map(int, input().split())

a = list(map(int, input().split()))

res = rob_money(a, n)

print(len(res))
print(*res)
