points = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    points.append((x, y))

# Обтекание Джарвиса
x_min = min(points, key=lambda x: x[0])[0]
x_max = max(points, key=lambda x: x[0])[0]
y_min = min(points, key=lambda y: y[1])[1]
y_max = max(points, key=lambda y: y[1])[1]

# Вывод результатов в консоль
print(x_min, y_min, x_max, y_max)