def can_transform(s1, s2):
    if len(s1) != len(s2):
        return False
    alpha_dict_index = {}
    for i in range(len(s1)):
        if s1[i] not in alpha_dict_index:
            alpha_dict_index[s1[i]] = [i]
        else:
            alpha_dict_index[s1[i]].append(i)
    print(alpha_dict_index)
    res_dict = {}
    for i in alpha_dict_index.keys():
        for j in list(s2):

            res_dict[j] = alpha_dict_index[i]
    print(res_dict)


def main():
    t = int(input())
    tests = []
    res = []
    for _ in range(t):
        s1 = input()
        s2 = input()
        tests.append((s1, s2))
    print(tests)
    for s1, s2 in tests:
        if can_transform(s1, s2):
            res.append("YES")
        else:
            res.append("NO")
        print('\n')
    print(res)


if __name__ == "__main__":
    main()
