# --- DAY 15 --- #
# "Go confidently in the direction of your dreams.  Live the life you have imagined." - Henry David Thoreau

# Data Path: data/15.txt || data/15_exemple.txt

def main():
    data = get_data(15, True)
    print("-- Day 15 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/15_exemple.txt" if exemple else f"data/15.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
