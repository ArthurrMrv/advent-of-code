# --- DAY 15 --- #
# "If you hear a voice within you say “you cannot paint,” then by all means paint and that voice will be silenced." - Vincent Van Gogh

# Data Path: data/15.py || data/15_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(15, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/15_exemple.txt" if exemple else f"data/15.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
