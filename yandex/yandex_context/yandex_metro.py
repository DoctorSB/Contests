data = input().split()
data = [int(i) for i in data]
if data[1] > data[2]:
    data[1], data[2] = data[2], data[1]
up = abs(data[2] - data[1]) - 1
down = abs(data[0] - data[2]) + data[1] - 1
if up < down:
    print(up)
else:
    print(down)
