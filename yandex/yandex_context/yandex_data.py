from collections import Counter
massa = input().split(", ")
c = Counter(massa)
for i in c:
    print(i, c)
