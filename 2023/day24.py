## DAY 24

def main():
    data = get_data()
    print("Part1: {}".format(part1(data)))
    print("Part2: {}".format(part2(data)))

def get_data(example=False):
    if example:
        with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day24_example.txt", "r") as f:
            data = f.read().splitlines()
    else:
        with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day24.txt", "r") as f:
            data = f.read().splitlines()
    return data

def part1(data):
    return

def part2(data):
    return


if __name__ == "__main__":
    main()
