
temp = input().split()
room_temp = int(temp[0])
cond_temp = int(temp[1])
mode = input()

def condition_mode(room_temp, cond_temp, mode):
    if mode == "fan":
        return room_temp
    elif mode == "freeze":
        if room_temp > cond_temp:
            return cond_temp
        else:
            return room_temp
    elif mode == "heat":
        if room_temp < cond_temp:
            return cond_temp
        else:
            return room_temp
    elif mode == "auto":
        return cond_temp
    
print(condition_mode(room_temp, cond_temp, mode))