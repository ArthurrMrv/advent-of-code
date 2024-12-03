# --- DAY 3 --- #
# "Definiteness of purpose is the starting point of all achievement." - W. Clement Stone
import re

# Data Path: data/3.txt || data/3_exemple.txt

def main():
    data = get_data(3, False)
    print("-- Day 3 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    
    mults = list(re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data))
    return sum(list(map(lambda x: int(x[0]) * int(x[1]), mults)))
    
def part2(data):
    
    def filter_data(data):
        """Delete parts of the data that are not valid (between a "don't()" and a "do()")

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        
        if len(data) < 7:
            return data
        
        valid = 1
        
        if data[:7] == "don't()":
            valid = 0
            filter_data = ""
        else:
            filter_data = data[:7]
    
        for i in range(7, len(data)):
            if data[i-7:i] == "don't()":
                valid = 0
            elif "do()" in data[i-7:i]:
                valid = 1
                
            if valid:
                filter_data += data[i]
                
        return filter_data
    
    data = filter_data(data)
    mults = list(re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data))
    
    return sum(list(map(lambda x: int(x[0]) * int(x[1]), mults)))
    
def get_data(i, exemple=False):
    path = f"data/3_exemple.txt" if exemple else f"data/3.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return "".join(data)
    
if __name__ == "__main__":
    main()
