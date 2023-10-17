N, M = map(int, input().split())


def time_need(cookie_counts, K):
    hours_needed = 0
    for count in cookie_counts:
        hours_needed += -(-count // K)
    return hours_needed


cookie_counts = [int(input()) for _ in range(N)]


left = 0
right = max(cookie_counts)

while left < right:
    mid = (left + right) // 2
    if time_need(cookie_counts, mid) <= M:
        right = mid
    else:
        left = mid + 1


if sum(cookie_counts) == 0 or time_need(cookie_counts, left) > M:
    print(0)
else:
    print(left)
