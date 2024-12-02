# --- DAY 22 --- #
# "Every strike brings me closer to the next home run." - Babe Ruth

# Data Path: data/22.txt || data/22_exemple.txt

def main():
    data = get_data(22, True)
    print("-- Day 22 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/22_exemple.txt" if exemple else f"data/22.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
