# --- DAY 20 --- #
# "Teach thy tongue to say, “I do not know,” and thous shalt progress." - Maimonides

# Data Path: data/20.py || data/20_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(20)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/20_exemple.txt" if exemple else f"data/20.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
