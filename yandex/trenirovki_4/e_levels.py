res = []
count = int(input())
num_list = list(map(int, input().split()))
summ = sum(num_list)

for i in num_list:
    res.append(abs(summ - i * count))

print(*res)
