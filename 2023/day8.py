from tqdm import tqdm

def main():
    with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day8.txt", "r") as f:
        data = f.read().splitlines()
        path = data[0]
        map_tunel = dict()
        for d in data[2:]:
            key, l, r = d.split("=")[0].strip(), d.split("=")[1].strip().split(",")[0].strip()[1:], d.split("=")[1].strip().split(",")[1].strip()[:-1]
            map_tunel[key] = {"L": l, 
                              "R": r}
    print("Part1: Found in {} steps".format(part1(path, map_tunel)))
    print("Part2: Found in {} steps".format(part2(path, map_tunel)))
    


def part1(path, map_tunel):
    current = "AAA"
    it = 0
    while it < 1_000_000 and current != "ZZZ":
        if current in map_tunel:
            if path[it%len(path)] == "L":
                current = map_tunel[current]["L"]
            elif path[it%len(path)] == "R":
                current = map_tunel[current]["R"]
        it += 1
    return it

def part2(path, map_tunel):
    current_points = []
    ending_points = set()
    for k in map_tunel.keys():
        if k[-1] == 'A':
            current_points.append(k)
        elif k[-1] == 'Z':
            ending_points.add(k)
    
    def decomp(n):
        ans = ()
        it = 2
        while n / it != 1:
            if n / it == int(n / it):
                ans += (it, )
                n /= it
            else:
                it += 1
        return ans + (it, )
    
    for i, current in enumerate(current_points):
        it = 0
        while it < 1_000_000_000_000_000 and current[-1] != "Z":
            if current in map_tunel:
                if path[it%len(path)] == "L":
                    current = map_tunel[current]["L"]
                elif path[it%len(path)] == "R":
                    current = map_tunel[current]["R"]
            it += 1
        current_points[i] = it
    
    for i, current in enumerate(current_points):
        current_points[i] = decomp(current)

    ans = []
    for nb in current_points:
        for fact in nb:
            while ans.count(fact) < nb.count(fact):
                ans.append(fact)
    i = 1
    for c in ans:
        i *= c
    return i

if __name__ == "__main__":
    main()