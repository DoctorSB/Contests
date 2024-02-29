from collections import defaultdict

N = int(input())

memory = []

def recepts(number, al):
    rec = ''
    for i in range(1, al[0] + 1):
        rec += str(al[i])
    rec_dict = defaultdict(int)
    for i in rec:
        rec_dict[i] += 1
    memory.append(rec_dict)
    converter(rec_dict)

def converter(rec):
    print(rec)
    for i in rec.keys():
        if i != '1' and i != '2':
            print(memory[int(i) - 3])
            rec += memory[int(i) - 3]
    print(rec)

for i in range(N - 2):
    ing_list = list(map(int, input().split()))
    recepts(i + 2, ing_list)

for _ in range(int(input())):
    pass