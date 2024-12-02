# --- DAY 3 --- #
# "Definiteness of purpose is the starting point of all achievement." - W. Clement Stone

# Data Path: data/3.txt || data/3_exemple.txt

def main():
    data = get_data(3, True)
    print("-- Day 3 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/3_exemple.txt" if exemple else f"data/3.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
