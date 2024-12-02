# --- DAY 2 --- #
# "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough." - Oprah Winfrey

# Data Path: data/2.py || data/2_exemple.py

def main():
    data = get_data(2, False)
    print("-- Day 2 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def is_increasing(l):
    for i in range(len(l)-1):
        if  not(0 < l[i+1] - l[i] <= 3):
            return False
    return True

def is_decreasing(l):
    for i in range(len(l)-1):
        if not(0 < l[i] - l[i+1] <= 3):
            return False
    return True

def is_increasing_or_decreasing(l):
    if len(l) <= 1:
        return True
    
    if l[0] < l[1]:
        return is_increasing(l)
    elif l[0] > l[1]:
        return is_decreasing(l)
    else:
        return False
    
def is_increasing2(l, error=0):
    
    for i in range(len(l)-1):
        if  not(0 < l[i+1] - l[i] <= 3):
            if error:
                return False                
            if i and not(0 <= l[i+1] - l[i-1] <= 3):
                l[i+1] = l[i]
            elif not(i) and not(0 < l[i+2] - l[i+1] <= 3):
                l[i+1] = l[i]
            error += 1
    return True

def is_decreasing2(l, error=0):
    for i in range(len(l)-1):
        if not(0 < l[i] - l[i+1] <= 3):
            if error:
                return False
            
            if i and not(0 <= l[i-1] - l[i+1] <= 3):
                l[i+1] = l[i]
                
            elif not(i) and not(0 < l[i+1] - l[i+2] <= 3):
                l[i+1] = l[i]
            error += 1
    return True

def is_increasing_or_decreasing2(l):
    if len(l) <= 1:
        return True
    
    if len(l) < 4:
        return is_increasing2(l) or is_decreasing2(l)
    
    a, b, c, d = l[:4]
    
    if is_increasing([b, c, d]) and not(0 < b - a <= 3):
        return is_increasing(l[1:])
    elif is_decreasing([b, c, d]) and not(0 < a - b <= 3):
        return is_decreasing(l[1:])
    
    def indicate_start(a, x):
        if a < x:
            return 1
        if a > x:
            return 0
        return None
    
    start = list(map(lambda x: indicate_start(a, x), [b, c, d]))
    
    if start.count(1) >= 2:
        return is_increasing2(l)
    
    if start.count(0) >= 2:
        return is_decreasing2(l)
    
    return False
    
def get_data(i, exemple=False):
    path = f"data/2_exemple.txt" if exemple else f"data/2.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data

def part1(data):
    reports = [list(map(int, l.split(" "))) for l in data]
    is_increasing = sum(list(map(is_increasing_or_decreasing, reports)))
    return is_increasing
    
def part2(data):
    reports = [list(map(int, l.split(" "))) for l in data]
    is_increasing = sum(list(map(is_increasing_or_decreasing2, reports)))

    return is_increasing
    
if __name__ == "__main__":
    main()
    pass