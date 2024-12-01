# --- DAY 17 --- #
# "Go confidently in the direction of your dreams.  Live the life you have imagined." - Henry David Thoreau

# Data Path: data/17.py || data/17_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(17, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/17_exemple.txt" if exemple else f"data/17.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
