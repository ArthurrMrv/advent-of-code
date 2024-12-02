# --- DAY 23 --- #
# "Winning isn't everything, but wanting to win is." - Vince Lombardi

# Data Path: data/23.txt || data/23_exemple.txt

def main():
    data = get_data(23, True)
    print("-- Day 23 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/23_exemple.txt" if exemple else f"data/23.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
