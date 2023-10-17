t_max = 30
t_min = 15

num_cases = int(input())
result = []

for _ in range(num_cases):
    num_conditions = int(input())
    max_value = t_max
    min_value = t_min
    for _ in range(num_conditions):
        condition, value = input().split()
        value = int(value)
        if condition == '>=':
            min_value = max(min_value, value)
        elif condition == '<=':
            max_value = min(max_value, value)
        else:
            min_value = max(min_value, value + 1)
            max_value = min(max_value, value - 1)
        if min_value > max_value:
            result.append(-1)
        else:
            result.append(max_value)
    result.append('\n')
print(*result, sep='\n')
