# --- DAY 18 --- #
# "I didn't fail the test. I just found 100 ways to do it wrong." - Benjamin Franklin

# Data Path: data/18.txt || data/18_exemple.txt

def main():
    data = get_data(18, True)
    print("-- Day 18 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/18_exemple.txt" if exemple else f"data/18.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
