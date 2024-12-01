# --- DAY 19 --- #
# "Life shrinks or expands in proportion to one's courage." - Anais Nin

# Data Path: data/19.py || data/19_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(19, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/19_exemple.txt" if exemple else f"data/19.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
