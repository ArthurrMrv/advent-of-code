# --- DAY 24 --- #
# "Winning isn't everything, but wanting to win is." - Vince Lombardi

# Data Path: data/24.py || data/24_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(24)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/24_exemple.txt" if exemple else f"data/24.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
