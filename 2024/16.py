# --- DAY 16 --- #
# "Go confidently in the direction of your dreams.  Live the life you have imagined." - Henry David Thoreau

# Data Path: data/16.py || data/16_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(16)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/16_exemple.txt" if exemple else f"data/16.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
