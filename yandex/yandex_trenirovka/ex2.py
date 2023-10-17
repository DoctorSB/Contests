def makeStringBeautiful(string, k): 
    stroka_list = list(string)
    n = len(stroka_list)
    for i in range(n/2):
        if stroka_list[i] == stroka_list[n]:
        

k = int(input())
stroka = input()

print(makeStringBeautiful(stroka, k))