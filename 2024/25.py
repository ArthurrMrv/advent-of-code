# --- DAY 25 --- #
# "Winning isn't everything, but wanting to win is." - Vince Lombardi

# Data Path: data/25.py || data/25_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(25, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/25_exemple.txt" if exemple else f"data/25.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
