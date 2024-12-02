# --- DAY 11 --- #
# "We must balance conspicuous consumption with conscious capitalism." - Kevin Kruse

# Data Path: data/11.txt || data/11_exemple.txt

def main():
    data = get_data(11, True)
    print("-- Day 11 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/11_exemple.txt" if exemple else f"data/11.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
