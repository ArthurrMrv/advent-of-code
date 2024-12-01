# --- DAY 8 --- #
# "Whatever the mind of man can conceive and believe, it can achieve." - Napoleon Hill

# Data Path: data/8.py || data/8_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(8, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/8_exemple.txt" if exemple else f"data/8.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
