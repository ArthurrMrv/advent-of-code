# --- DAY 5 --- #
# "Fall seven times and stand up eight." - Japanese Proverb

# Data Path: data/5.txt || data/5_exemple.txt

def main():
    data = get_data(5, True)
    print("-- Day 5 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/5_exemple.txt" if exemple else f"data/5.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
