# --- DAY 21 --- #
# "The best revenge is massive success." - Frank Sinatra

# Data Path: data/21.py || data/21_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(21)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/21_exemple.txt" if exemple else f"data/21.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
