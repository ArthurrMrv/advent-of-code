# --- DAY 19 --- #
# "Teach thy tongue to say, “I do not know,” and thous shalt progress." - Maimonides

# Data Path: data/19.txt || data/19_exemple.txt

def main():
    data = get_data(19, True)
    print("-- Day 19 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    return None
    
def part2(data):
    return None
    
def get_data(i, exemple=False):
    path = f"data/19_exemple.txt" if exemple else f"data/19.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
