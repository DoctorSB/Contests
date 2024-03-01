baykalsk = list(map(int, input().split()))
smert_yascherov = list(map(int, input().split()))
pravoslavniy_kalendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = []
for i, j in zip(baykalsk, smert_yascherov):
	res.append(abs(j - i))
print(res[0] * 365 + pravoslavniy_kalendar[res[1] - 1] + res[2] + res[3],  res[4] * 360 + res[5] * 60 )