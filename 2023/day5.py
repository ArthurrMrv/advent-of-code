with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day5_example.txt", "r") as f:
    data = f.read().splitlines()

#seeds: 79 14 55 13

#seed-to-soil map:
# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4

def part1():
    dico_maps = {
        "seed-to-soil": dict(),
        "soil-to-fertilizer": dict(),
        "fertilizer-to-water": dict(),
        "water-to-light": dict(),
        "light-to-temperature": dict(),
        "temperature-to-humidity": dict(),
        "humidity-to-location": dict()
    }
    # for d in dico_maps:
    #     dico_maps[d] = {'to':dict(),
    #                     'from':dict()}
    seeds = [int(i) for i in data[0].split(": ")[1].split(" ")]
    
    for i in range(2, len(data)):
        if 'seeds:' in data[i] or data[i] == "":
            continue
        if 'map' in data[i]:
            current_map = data[i].split(" ")[0]
        else:
            a, b, c = tuple([int(i) for i in data[i].split(" ")])

            begin = [a+i for i in range(c)]
            arival = [b+i for i in range(c)]
            
            for k in range(len(begin)):
                dico_maps[current_map][begin[k]] = arival[k]
    
    for s in seeds:
        current = s
        for d in dico_maps:
            if current not in dico_maps[d]:
                dico_maps[d][current] = current
            else:
                current = dico_maps[d][current]
    
    mini = None          
    for s in seeds:
        current = s
        for d in dico_maps:
            current = dico_maps[d][current]
        if mini is None or current < mini:
            mini = current
        
    return dico_maps["seed-to-soil"]

def part2():
    pass


if __name__ == "__main__":
    print(part1())

    part2()