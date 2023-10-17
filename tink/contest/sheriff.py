alpha_list = list(input())

alpha_dict = {
    's': 0,
    'h': 0,
    'e': 0,
    'r': 0,
    'i': 0,
    'f': 0,
}

for i in alpha_list:
    if i in alpha_dict:
        alpha_dict[i] += 1

print(min(alpha_dict['s'], alpha_dict['h'], alpha_dict['e'],
      alpha_dict['r'], alpha_dict['i'], alpha_dict['f'] // 2))
