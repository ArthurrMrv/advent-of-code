# --- DAY 4 --- #
# "In order to succeed, your desire for success should be greater than your fear of failure." - Bill Cosby

# Data Path: data/4.py || data/4_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(4, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/4_exemple.txt" if exemple else f"data/4.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
