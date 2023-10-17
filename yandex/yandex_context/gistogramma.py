def read_file(file):
    with open(file, "r") as fl:
        list_of_alpha = fl.read()
        return sorted(list_of_alpha)


answer = {}
for i in read_file("input.txt"):
    if i != "\n" and i != " ":
        answer[i] = answer.get(i, 0) + 1


def horiz_hist(answer):
    max_height = max(answer.values())
    for i in range(max_height):
        for j in answer:
            if answer[j] >= max_height - i:
                print("#", end="")
            else:
                print(" ", end="")
        print()


horiz_hist(answer)
print("".join(answer.keys()))
