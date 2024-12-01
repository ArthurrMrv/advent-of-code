# --- DAY 7 --- #
# "Fall seven times and stand up eight." - Japanese Proverb

# Data Path: data/7.py || data/7_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(7, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/7_exemple.txt" if exemple else f"data/7.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
