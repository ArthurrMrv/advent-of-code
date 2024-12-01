# --- DAY 10 --- #
# "We must believe that we are gifted for something, and that this thing, at whatever cost, must be attained." - Marie Curie

# Data Path: data/10.py || data/10_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(10, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/10_exemple.txt" if exemple else f"data/10.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
