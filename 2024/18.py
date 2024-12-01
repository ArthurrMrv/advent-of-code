# --- DAY 18 --- #
# "Life shrinks or expands in proportion to one's courage." - Anais Nin

# Data Path: data/18.py || data/18_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(18)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/18_exemple.txt" if exemple else f"data/18.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
