from collections import Counter

N = int(input())

memory = []

def recepts(number, al):
    rec = ''
    for i in range(1, al[0] + 1):
        rec += str(al[i])
    rec_dict = Counter(rec)
    memory.append(rec_dict)
    converter(rec_dict)

def converter(rec):
    for i in rec.keys():
        if i != '1' and i != '2':
            rec += memory[int(i) - 3]
    print(rec)

for i in range(N - 2):
    ing_list = list(map(int, input().split()))
    recepts(i + 2, ing_list)

for _ in range(int(input())):
    pass
