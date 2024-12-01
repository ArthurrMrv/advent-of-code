# --- DAY 14 --- #
# "If the wind will not serve, take to the oars." - Latin Proverb

# Data Path: data/14.py || data/14_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(14, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/14_exemple.txt" if exemple else f"data/14.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
