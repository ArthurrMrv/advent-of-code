# --- DAY 7 --- #
# "You become what you believe." - Oprah Winfrey

# Data Path: data/7.txt || data/7_exemple.txt

def main():
    data = get_data(7, True)
    print("-- Day 7 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/7_exemple.txt" if exemple else f"data/7.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
