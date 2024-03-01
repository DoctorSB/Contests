def distance(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5

list_point = list(map(float, input().split()))

print(distance((list_point[0], list_point[1]), (list_point[2], list_point[3])))