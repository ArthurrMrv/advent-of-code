# --- DAY 3 --- #
# "Definiteness of purpose is the starting point of all achievement." - W. Clement Stone

# Data Path: data/3.py || data/3_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(3, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/3_exemple.txt" if exemple else f"data/3.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
