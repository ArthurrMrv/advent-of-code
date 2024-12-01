## DAY 17

def main():
    data = get_data(True)
    print("Day 17", data)
    print("Part1: {}".format(part1(data)))
    print("Part2: {}".format(part2(data)))

def get_data(example=False):
    if example:
        with open("Data/day17_example.txt", "r") as f:
            data = f.read().splitlines()
    else:
        with open("Data/day17.txt", "r") as f:
            data = f.read().splitlines()
    return data

def part1(data):
    return
        
    
    
    

def part2(data):
    return


if __name__ == "__main__":
    main()
