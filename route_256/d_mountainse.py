def read_input():
    num_input = int(input())
    inputs = []
    for _ in range(num_input):
        num_mounts, y, x = map(int, input().split())
        matrix = []
        for _ in range(num_mounts):
            if num_mounts > 1 and _ > 0:
                input()  # Skipping empty line
            sub_matrix = [list(input().rstrip()) for _ in range(y)]
            matrix.append(sub_matrix)
        inputs.append((matrix, x, y))
    return inputs


def update_view(view, num_mounts):
    it = num_mounts - 1
    while it != -1:
        for j in range(len(view[it])):
            for n in range(len(view[it][j])):
                if view[it][j][n] != '.':
                    view[-1][j][n] = view[it][j][n]
        it -= 1


def print_result(result):
    for sub_matrix in result:
        for row in sub_matrix:
            print(''.join(row))
        print()


def main():
    inputs = read_input()
    results = []
    for matrix, x, y in inputs:
        view = matrix.copy()
        update_view(view, len(matrix))
        results.append(view[-1])

    print_result(results)


if __name__ == '__main__':
    main()
