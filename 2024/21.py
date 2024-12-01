# --- DAY 21 --- #
# "What's money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do." - Bob Dylan

# Data Path: data/21.py || data/21_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(21, True)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/21_exemple.txt" if exemple else f"data/21.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
