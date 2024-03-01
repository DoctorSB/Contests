N, M = map(int, input().split())
num_list = [int(i) for i in input().split()]
for _ in range(M):
    L, R = map(int, input().split())
    t_list = num_list[L:R + 1]
    mmax = max(t_list)
    mmin = min(t_list)
    if mmin != mmax:
        print(mmax)
    else:
        print('NOT FOUND')