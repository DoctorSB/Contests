N, M, K = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    summa = 0
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            summa += matrix[i][j]
    print(summa)
