# --- DAY 24 --- #
# "First, have a definite, clear practical ideal; a goal, an objective. Second, have the necessary means to achieve your ends; wisdom, money, materials, and methods. Third, adjust all your means to that end." - Aristotle

# Data Path: data/24.py || data/24_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(24, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/24_exemple.txt" if exemple else f"data/24.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
