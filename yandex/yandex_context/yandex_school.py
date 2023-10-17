students = int(input())
house = input().split()
house = [int(i) for i in house]
srsumm = 0
for i in range(min(house), max(house)):
    summ = 0
    for j in range(students):
        srsumm = summ + j
print(srsumm)
