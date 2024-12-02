# --- DAY 8 --- #
# "The most common way people give up their power is by thinking they don't have any." - Alice Walker

# Data Path: data/8.txt || data/8_exemple.txt

def main():
    data = get_data(8, True)
    print("-- Day 8 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/8_exemple.txt" if exemple else f"data/8.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
