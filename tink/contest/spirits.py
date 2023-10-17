n, m = map(int, input().split())

bands = [i for i in range(1, n + 1)]

spirits = [1 for _ in range(n)]

num_band = max(bands)

res = []

for _ in range(m):
    task = list(map(int, input().split()))
    if task[0] == 1:
        if bands[task[1] - 1] != bands[task[2] - 1]:
            num_band += 1
            f, s = bands[task[1] - 1], bands[task[2] - 1]
            for i in range(n):
                if bands[i] == f or bands[i] == s:
                    bands[i] = num_band
                    spirits[i] += 1
    elif task[0] == 2:
        if bands[task[1] - 1] == bands[task[2] - 1]:
            res.append('YES')
        else:
            res.append('NO')
    elif task[0] == 3:
        res.append(spirits[task[1] - 1])

print(*res, sep='\n')
