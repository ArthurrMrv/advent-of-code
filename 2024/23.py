# --- DAY 23 --- #
# "Every strike brings me closer to the next home run." - Babe Ruth

# Data Path: data/23.py || data/23_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(23)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/23_exemple.txt" if exemple else f"data/23.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
