# --- DAY 16 --- #
# "How wonderful it is that nobody need wait a single moment before starting to improve the world." - Anne Frank

# Data Path: data/16.txt || data/16_exemple.txt

def main():
    data = get_data(16, True)
    print("-- Day 16 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/16_exemple.txt" if exemple else f"data/16.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
