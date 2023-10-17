def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


def main():
    n = int(input())
    times = [time_to_seconds(input()) for _ in range(n)]

    days_count = 1
    for i in range(1, n):
        if times[i] <= times[i - 1]:
            days_count += 1

    print(days_count)


if __name__ == "__main__":
    main()
