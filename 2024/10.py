# --- DAY 10 --- #
# "We must believe that we are gifted for something, and that this thing, at whatever cost, must be attained." - Marie Curie

# Data Path: data/10.txt || data/10_exemple.txt

def main():
    data = get_data(10, True)
    print("-- Day 10 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/10_exemple.txt" if exemple else f"data/10.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
