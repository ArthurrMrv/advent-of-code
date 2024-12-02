# --- DAY 14 --- #
# "If the wind will not serve, take to the oars." - Latin Proverb

# Data Path: data/14.txt || data/14_exemple.txt

def main():
    data = get_data(14, True)
    print("-- Day 14 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/14_exemple.txt" if exemple else f"data/14.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
