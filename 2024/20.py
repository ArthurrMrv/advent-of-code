# --- DAY 20 --- #
# "The best revenge is massive success." - Frank Sinatra

# Data Path: data/20.txt || data/20_exemple.txt

def main():
    data = get_data(20, True)
    print("-- Day 20 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/20_exemple.txt" if exemple else f"data/20.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
