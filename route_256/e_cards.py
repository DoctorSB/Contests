def read_input():
    m, n = map(int, input().split())
    return m, n


def read_items(m):
    items = list(map(int, input().split()[:m]))
    return items


def create_friends_dict(m, items):
    friends = {i + 1: set(range(1, items[i] + 1)) for i in range(m)}
    return friends


def find_unused_values(big_set, friends):
    for k, v in friends.items():
        value_found = False
        for value in big_set:
            if value not in v:
                value_found = True
                friends[k] = value
                big_set.remove(value)
                break
        if not value_found:
            return None
    return friends


def main():
    m, n = read_input()
    big_set = set(range(1, n + 1))
    items = read_items(m)
    friends = create_friends_dict(m, items)

    updated_friends = find_unused_values(big_set, friends)
    if updated_friends is None:
        print(-1)
    else:
        result = ' '.join(str(value) for value in updated_friends.values())
        print(result)


if __name__ == "__main__":
    main()
