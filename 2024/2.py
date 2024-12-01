# --- DAY 2 --- #
# "The battles that count aren't the ones for gold medals. The struggles within yourself-the invisible battles inside all of us-that's where it's at." - Jesse Owens

# Data Path: data/2.py || data/2_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(2)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/2_exemple.txt" if exemple else f"data/2.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
