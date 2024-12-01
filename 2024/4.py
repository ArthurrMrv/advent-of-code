# --- DAY 4 --- #
# "Definiteness of purpose is the starting point of all achievement." - W. Clement Stone

# Data Path: data/4.py || data/4_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(4)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/4_exemple.txt" if exemple else f"data/4.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
