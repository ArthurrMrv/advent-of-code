# --- DAY 17 --- #
# "Life shrinks or expands in proportion to one's courage." - Anais Nin

# Data Path: data/17.txt || data/17_exemple.txt

def main():
    data = get_data(17, True)
    print("-- Day 17 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/17_exemple.txt" if exemple else f"data/17.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
