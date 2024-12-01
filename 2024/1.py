# --- DAY 1 --- #
# "Believe you can and you're halfway there." - Theodore Roosevelt

# Data Path: data/1.py || data/1_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data(1, False)
    print(part1(data))
    print(part2(data))

def get_data(i, exemple=False):
    path = f"data/1_exemple.txt" if exemple else f"data/1.txt"
    with open(path, "r") as f:
        data = [i.strip() for i in f.readlines()]
    return data
    
def part1(data):
    data = data.split("\n")
    data = [data.split("   ") for data in data]
    l1, l2 = list(zip(*data))
    l1, l2 = [int(i) for i in l1], [int(i) for i in l2]
    l1 = np.array(l1)
    l2 = np.array(l2)
    
    l1.sort()
    l2.sort()
    
    return np.abs(l1-l2).sum()
    
def part2(data):
    data = data.split("\n")
    data = [data.split("   ") for data in data]
    l1, l2 = list(zip(*data))
    l1, l2 = [int(i) for i in l1], [int(i) for i in l2]
    
    keys = list(set(l1))
    
    l1_dict = {i:0 for i in keys}
    
    for i in tqdm(l2):
        if i in l1_dict:
            l1_dict[i] += 1
    
    return sum([k * l1_dict[k] for k in keys])
    
if __name__ == "__main__":
    main()
