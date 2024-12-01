# --- DAY 9 --- #
# "The most common way people give up their power is by thinking they don't have any." - Alice Walker

# Data Path: data/9.py || data/9_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(9)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/9_exemple.txt" if exemple else f"data/9.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
