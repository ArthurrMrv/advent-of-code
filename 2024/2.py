# --- DAY 2 --- #
# "Believe you can and you're halfway there." - Theodore Roosevelt

# Data Path: data/2.py || data/2_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(2, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/2_exemple.txt" if exemple else f"data/2.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
