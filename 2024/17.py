# --- DAY 17 --- #
# "How wonderful it is that nobody need wait a single moment before starting to improve the world." - Anne Frank

# Data Path: data/17.py || data/17_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(17)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/17_exemple.txt" if exemple else f"data/17.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
