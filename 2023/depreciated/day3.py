
with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/day3.txt", 'r') as f:
    data = f.read().splitlines()
    
def get_digits(coords):
    ans = []
    for (x, y) in coords:
        ans.append(data[y][x])
    return int(''.join(ans))

def get_engine_parts():
    engine_parts = set()
    visited = set()

    for y in range(len(data)):
        for x in range(len(data[y])):
            
            if data[y][x].isdigit() and (x, y) not in visited:
                cursor = 1
                current_num = tuple()
                current_num += ((x, y), )
                
                while 0 < x+cursor < len(data[y]) and data[y][x + cursor].isdigit() and (x+cursor, y) not in visited:
                    current_num += ((x + cursor, y), )
                    visited.add((x + cursor, y))
                    cursor += 1
                
                for (i, j) in current_num:
                    for (k, l) in ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)):
                        if 0 < i + k < len(data[y]) and 0 < j + l < len(data) and (not(data[j + l][i + k].isdigit()) and data[j + l][i + k] != '.'):
                            engine_parts.add(current_num)
                            break
            visited.add((x, y))
    return engine_parts

def part1():
    engine_parts = set()
    visited = set()
    
    engine_parts = get_engine_parts()
            
    return sum([get_digits(num) for num in engine_parts])

def part2():
    gears = set()
    dico_engines = dict()
    engine_parts = get_engine_parts()
    for e in engine_parts:
        for corr in e:
            
            dico_engines[corr] = e

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '*':
                visited = set()
                gear = tuple()
                for (i, j) in ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)):
                    if 0 <= x + i < len(data[y]) and 0 <= y + j < len(data) and data[y+j][x+i].isdigit() and (x+i, y+j) not in visited:
                        for corr in dico_engines[(x+i, y+j)]:
                            visited.add(corr)
                        gear += (dico_engines[(x+i, y+j)], )
                        
                if len(gear) == 2:
                    gears.add(gear)

    return sum([get_digits(g[0])*get_digits(g[1]) for g in gears])

print(part2())