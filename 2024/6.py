# --- DAY 6 --- #
# "Whatever the mind of man can conceive and believe, it can achieve." - Napoleon Hill

# Data Path: data/6.txt || data/6_exemple.txt

def main():
    data = get_data(6, True)
    print("-- Day 6 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/6_exemple.txt" if exemple else f"data/6.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
