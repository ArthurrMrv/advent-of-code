## DAY 12

def main():
    data = get_data()
    print(part1(data))
    print(part2(data))

def get_data(example=False):
    if example:
        with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day12_example.txt", "r") as f:
            data = f.read().splitlines()
    else:
        with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day12.txt", "r") as f:
            data = f.read().splitlines()
    return data

def part1(data):
    return

def part2(data):
    return


if __name__ == "__main__":
    main()
