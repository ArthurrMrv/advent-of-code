# --- DAY 13 --- #
# "Start where you are. Use what you have.  Do what you can." - Arthur Ashe

# Data Path: data/13.py || data/13_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(13)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/13_exemple.txt" if exemple else f"data/13.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
