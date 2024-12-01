# --- DAY 6 --- #
# "Fall seven times and stand up eight." - Japanese Proverb

# Data Path: data/6.py || data/6_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(6)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/6_exemple.txt" if exemple else f"data/6.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
