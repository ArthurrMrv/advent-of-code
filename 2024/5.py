# --- DAY 5 --- #
# "Definiteness of purpose is the starting point of all achievement." - W. Clement Stone

# Data Path: data/5.py || data/5_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(5, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/5_exemple.txt" if exemple else f"data/5.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
