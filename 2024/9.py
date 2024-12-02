# --- DAY 9 --- #
# "I have learned over the years that when one's mind is made up, this diminishes fear." - Rosa Parks

# Data Path: data/9.txt || data/9_exemple.txt

def main():
    data = get_data(9, True)
    print("-- Day 9 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/9_exemple.txt" if exemple else f"data/9.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
