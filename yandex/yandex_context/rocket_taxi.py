from collections import defaultdict

def calculate_movement_time(log_entries):
    log_entries.sort()
    rocket_status = defaultdict(lambda: {'start_time': None, 'total_time': 0})
    
    for entry in log_entries:
        day, hour, minute, rocket_id, status = entry
        time_in_minutes = day * 24 * 60 + hour * 60 + minute
        
        if status == 'A':
            rocket_status[rocket_id]['start_time'] = time_in_minutes
        elif status == 'B':
            rocket_status[rocket_id]['total_time'] += time_in_minutes - rocket_status[rocket_id]['start_time']
            rocket_status[rocket_id]['start_time'] = time_in_minutes
        elif status == 'C':
            print(rocket_status[rocket_id]['total_time'], status)
            if rocket_status[rocket_id]['start_time'] is not None:
                rocket_status[rocket_id]['total_time'] += time_in_minutes - rocket_status[rocket_id]['start_time'] 
                rocket_status[rocket_id]['start_time'] = None
        elif status == 'S':
            if rocket_status[rocket_id]['start_time'] is not None:
                rocket_status[rocket_id]['total_time'] += time_in_minutes - rocket_status[rocket_id]['start_time']
                rocket_status[rocket_id]['start_time'] = None

    
    result = [rocket_status[rocket_id]['total_time'] for rocket_id in sorted(rocket_status)]
    return result


# Пример использования
log_entries = [
    (14, 21, 30, '3632', 'A'),
    (14, 21, 40, '212372', 'B'),
    (14, 23, 52, '3632', 'B'),
    (50, 7, 25, '3632', 'A'),
    (14, 23, 52, '212372', 'S'),
    (15, 0, 5, '3632', 'C'),
    (14, 21, 30, '212372', 'A'),
    (50, 7, 26, '3632', 'C'),
]

result = calculate_movement_time(log_entries)
print(" ".join(map(str, result)))


