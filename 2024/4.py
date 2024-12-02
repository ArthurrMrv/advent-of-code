# --- DAY 4 --- #
# "In order to succeed, your desire for success should be greater than your fear of failure." - Bill Cosby

# Data Path: data/4.txt || data/4_exemple.txt

def main():
    data = get_data(4, True)
    print("-- Day 4 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/4_exemple.txt" if exemple else f"data/4.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
