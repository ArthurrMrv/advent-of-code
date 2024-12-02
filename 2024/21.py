# --- DAY 21 --- #
# "What's money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do." - Bob Dylan

# Data Path: data/21.txt || data/21_exemple.txt

def main():
    data = get_data(21, True)
    print("-- Day 21 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/21_exemple.txt" if exemple else f"data/21.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
