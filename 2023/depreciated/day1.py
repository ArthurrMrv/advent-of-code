with open("day1.txt") as f:
    data = f.read().splitlines()

dict_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six" : 6, "seven": 7, "eight": 8, "nine": 9}

sum = 0
for i in range(len(data)):
    
    idx_low = 0
    idx_up = len(data[i]) - 1
    down_value = None
    up_value = None
    for idx_low in range(0, len(data[i])):
        if down_value is not None:
            break
        for j in range(0, idx_low):
                if data[i][j:idx_low] in dict_num:
                    down_value = dict_num[data[i][j:idx_low]]
                    break
        if data[i][idx_low] in '0123456789':
            break
    if down_value is None:
        down_value = int(data[i][idx_low])
        
    for idx_up in range(len(data[i]) - 1, -1, -1):
        if up_value is not None:
            break
        for j in range(len(data[i]), idx_up, -1):
            if data[i][idx_up:j] in dict_num:
                up_value = dict_num[data[i][idx_up:j]]
                break
        if data[i][idx_up] in '0123456789':
            break
    if up_value is None:
        up_value = int(data[i][idx_up])
    
    sum += int(f"{down_value}{up_value}")

print(sum)