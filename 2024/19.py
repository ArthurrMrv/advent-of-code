# --- DAY 19 --- #
# "I didn't fail the test. I just found 100 ways to do it wrong." - Benjamin Franklin

# Data Path: data/19.py || data/19_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(19)
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/19_exemple.txt" if exemple else f"data/19.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
