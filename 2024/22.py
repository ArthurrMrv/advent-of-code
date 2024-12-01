# --- DAY 22 --- #
# "Every strike brings me closer to the next home run." - Babe Ruth

# Data Path: data/22.py || data/22_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(22, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/22_exemple.txt" if exemple else f"data/22.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
