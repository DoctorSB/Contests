start_string = input()

res_string = start_string

for _ in range(int(input())):
    s, e, c = input().split()
    s, e = int(s), int(e)
    res_string = res_string[:s - 1] + c + res_string[e:]

print(res_string)
