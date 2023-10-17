n = int(input())

joe_hand = list(map(int, input().split()))
win_hand = list(map(int, input().split()))

left = 0
right = 0

for i in range(n):
    if joe_hand[i] == win_hand[i]:
        left += 1
    else:
        break

for i in range(n - 1, -1, -1):
    if joe_hand[i] == win_hand[i]:
        right += 1
    else:
        break

if (win_hand[left:n - right]) == sorted((joe_hand[left:n - right])):
    print('YES')
else:
    print('NO')
