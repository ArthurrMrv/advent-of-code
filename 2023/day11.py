## DAY 11
import numpy as np 
from tqdm import tqdm

def main():
    data = get_data()
    print("Part 1: {}".format(part1(data)))
    print("Part 2: {}".format(part2(data)))

def get_data(example=False):
    if example:
        with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day11_example.txt", "r") as f:
            data = f.read().splitlines()
    else:
        with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day11.txt", "r") as f:
            data = f.read().splitlines()
    return data

def part1(data):
    galaxy_list = list()
    shaped_map = []
    for r in data:
        shaped_map.append(list([0 if i == '.' else 1 for i in r]))
    
    shaped_map = np.matrix(shaped_map)
    
    for j in range(2):
        if j:
            shaped_map = shaped_map.transpose()
        i = 0
        while i < shaped_map.shape[0]:
            if np.count_nonzero(shaped_map[i]) == 0:
                shaped_map = np.insert(shaped_map, i, 0, axis=0)
                i += 1
            
            i += 1

    shaped_map = shaped_map.transpose()
    for y in range(shaped_map.shape[0]):
        for x in range(shaped_map.shape[1]):
            if shaped_map[y, x] == 1:
                galaxy_list.append((x, y))
    
    count = 0
    while len(galaxy_list) > 0:
        current_galaxy = galaxy_list.pop()
        for g in galaxy_list:
            count += abs(current_galaxy[0] - g[0]) + abs(current_galaxy[1] - g[1])
        
    return count

def part2(data, EXPANSION_LEVEL = 1_000_000):

    galaxy_list = list()
    shaped_map = []
    for r in data:
        shaped_map.append(list([0 if i == '.' else 1 for i in r]))
    
    shaped_map = np.matrix(shaped_map)
    
    for y in range(shaped_map.shape[0]):
        for x in range(shaped_map.shape[1]):
            if shaped_map[y, x] == 1:
                galaxy_list.append((x, y))
    bar = tqdm(total=len(galaxy_list), desc="Calculating distances")
    
    count = 0
    
    while len(galaxy_list) > 0:
        current_galaxy = galaxy_list.pop()
        
        for g in galaxy_list:
            petit_bonhomme_coor = current_galaxy
            
            x_diff, y_diff = g[0] - current_galaxy[0], g[1] - current_galaxy[1]
            
            for diff in [y_diff, x_diff]:
                #print(f"current_galaxy: {current_galaxy}, g: {g}, petit_bonhomme_coor: {petit_bonhomme_coor}, diff: {diff} over ({y_diff}, {x_diff})")
                for i in range(abs(diff)):
                    petit_bonhomme_coor = (petit_bonhomme_coor[0], int(petit_bonhomme_coor[1] + (diff/abs(diff)))) if diff != 0 else petit_bonhomme_coor

                    if np.count_nonzero(shaped_map[petit_bonhomme_coor[1]]) == 0:
                        count += EXPANSION_LEVEL
                    else:
                        count += 1
                
                petit_bonhomme_coor = (petit_bonhomme_coor[1], petit_bonhomme_coor[0])
                shaped_map = shaped_map.transpose()
            
        bar.update(1)
        
    bar.close()

            
        
    return count


if __name__ == "__main__":
    main()
