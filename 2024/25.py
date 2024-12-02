# --- DAY 25 --- #
# "It's not the years in your life that count. It's the life in your years." - Abraham Lincoln

# Data Path: data/25.txt || data/25_exemple.txt

def main():
    data = get_data(25, True)
    print("-- Day 25 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/25_exemple.txt" if exemple else f"data/25.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
