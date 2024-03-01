def shifrator(temp):
    surname, name, secname, day, mounth, year = temp
    fio_len = len(set(name + surname + secname))
    day_moun_sum = (sum(map(int, list(day))) + sum(map(int, list(mounth)))) * 64
    first_alpha = (ord(surname[0].lower()) - ord('a') + 1) * 256
    temp_ans = hex(fio_len + day_moun_sum + first_alpha).upper()
    ans = temp_ans[-3] + temp_ans[-2] + temp_ans[-1]
    return ans

result = []

for i in range(int(input())):
    temp = input().split(',')
    result.append(shifrator(temp))
    
print(*result, sep=' ')
# 2
# Volozh,Arcady,Yurievich,11,2,1964
# Segalovich,Ilya,Valentinovich,13,9,1964