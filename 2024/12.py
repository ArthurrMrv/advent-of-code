# --- DAY 12 --- #
# "Start where you are. Use what you have.  Do what you can." - Arthur Ashe

# Data Path: data/12.txt || data/12_exemple.txt

def main():
    data = get_data(12, True)
    print("-- Day 12 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/12_exemple.txt" if exemple else f"data/12.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
