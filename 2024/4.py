# --- DAY 4 --- #
# "In order to succeed, your desire for success should be greater than your fear of failure." - Bill Cosby

# Data Path: data/4.txt || data/4_exemple.txt
import numpy as np

def main():
    data = get_data(4, False)
    print("-- Day 4 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data, word = "XMAS"):
    occurences = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == word[0]:
                occurences += look_for(data, word, (i, j))
    return occurences
    
def part2(data, word = "MAS"):
    occurences = np.zeros((len(data), len(data[0])))
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == word[0]:
                idx_occurences = look_for_occurences(data, word, (i, j))
                for idx in idx_occurences:
                    occurences[idx[0]][idx[1]] += 1

    return np.count_nonzero(occurences == 2)
    
def look_for(data, word, coordinates,
              directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, -1), (-1, 0)],):
   
    occurences = 0
    
    for d in directions:
        dx, dy = d
        x, y = coordinates
        idx = 1
        while 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]):
            x += dx
            y += dy
            if data[x][y] == word[idx]:
                idx += 1
                if idx == len(word):
                    occurences += 1
                    break
            else:
                break
            
    return occurences 

 
def look_for_occurences(data, word, coordinates,
              directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]):
    
    occurences_idx = []
    
    for d in directions:
        dx, dy = d
        x, y = coordinates
        idx = 1
        while 0 <= x + dx < len(data) and 0 <= y + dy < len(data[0]):
            x += dx
            y += dy
            if data[x][y] == word[idx]:
                idx += 1
                if idx == len(word):
                    occurences_idx.append((x-dx, y-dy))
                    break
            else:
                break
            
    return occurences_idx

    
    
    
def get_data(i, exemple=False):
    path = f"data/4_exemple.txt" if exemple else f"data/4.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    return data
    
if __name__ == "__main__":
    main()
