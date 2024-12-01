# --- DAY 12 --- #
# "We must believe that we are gifted for something, and that this thing, at whatever cost, must be attained." - Marie Curie

# Data Path: data/12.py || data/12_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(12, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/12_exemple.txt" if exemple else f"data/12.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
