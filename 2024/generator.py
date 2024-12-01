import sys
from tqdm import tqdm
import os
import json
import random

random.seed(42)

def main():
    
    quotes : list = get_quotes()
    random.shuffle(quotes)
    
    mini, maxi = get_mini_maxi()
    if check_already_exist(mini, maxi):
        return
    
    generate_data(mini, maxi)
    generate_py(mini, maxi, quotes)
    
    pass

def check_already_exist(mini, maxi):
    for i in range(mini, maxi+1):
        if os.path.exists(f"day_{i}.py"):
            print(f"File data/{i}.py already exist")
            return True
        if os.path.exists(f"data/{i}.txt"):
            print(f"File data/{i}.txt already exist")
            return True
        if os.path.exists(f"data/{i}_exemple.txt"):
            print(f"File data/{i}_exemple.txt already exist")
            return True
    return False

def get_quotes():
    quotes = json.loads(open("quotes.json", "r").read())
    return quotes["quotes"]

def get_mini_maxi():
    if len(sys.argv) != 3:
        mini = int(input("Enter the minimum value: "))
        maxi = int(input("Enter the maximum value: "))
    else:
        mini = int(sys.argv[1])
        maxi = int(sys.argv[2])
    return mini, maxi

def generate_data(mini, maxi):
    for i in tqdm(range(mini, maxi+1)):
        os.system(f"touch data/{i}.txt")
        os.system(f"touch data/{i}_exemple.txt")
    
def generate_py(mini, maxi, quotes):
    for i in tqdm(range(mini, maxi+1)):
        
        template = PyTemplate(i, quotes[(i-mini)%len(quotes)])
        
        with open(f"{i}.py", "w") as f:
            f.write(str(template))
            
class PyTemplate:
    
    def __init__(self, i, quote):
        self.i = i
        self.quote = quote
        self.template = self.make_template()
        pass
    
    def __str__(self):
        return self.template
    
    def make_template(self):
        PY_TEMPLATE = f"""# --- DAY {self.i} --- #
# \"{self.quote['quote']}\" - {self.quote['author']}

# Data Path: data/{self.i}.py || data/{self.i}_exemple.py

import os 
from tqdm import tqdm
import numpy as np

def main():
    data = get_data({self.i})
    print(part1(data))

def get_data(i, exemple=False):
    path = f"data/{self.i}_exemple.txt" if exemple else f"data/{self.i}.txt"
    with open(path, "r") as f:
        data = f.read()
    return data
    
def part1(data):
    return None
    
def part2(data):
    return None
    
if __name__ == "__main__":
    main()
"""
        
        return PY_TEMPLATE

if __name__ == "__main__":
    main()