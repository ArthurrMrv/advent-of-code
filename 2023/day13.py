## DAY 13
import numpy as np

def main():
    data = get_data(False)
    
    print("Part1: {}".format(part1(data)))
    print("Part2: {}".format(part2(data)))

def get_data(example=False):
    if example:
        with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day13_example.txt", "r") as f:
            data = f.read().splitlines()
    else:
        with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day13.txt", "r") as f:
            data = f.read().splitlines()
    return data

def part1(data):
    shaped_map = [[]]
    for r in data:
        if len(r) == 0:
            shaped_map.append([])
        else:
            shaped_map[-1].append(list([0 if i == '.' else 1 for i in r]))
    
    for i in range(len(shaped_map)):
        shaped_map[i] = np.matrix(shaped_map[i])
        
    def get_lin_break(m):
        
        for j in range(2):
            
            for i in range(m.shape[0]-1):
                
                if np.all(m[i] == m[i+1]):
                    jocker = True
                    cursor = 1
                    while i-cursor >= 0 and cursor+1+i < m.shape[0]:
                        #print(i, cursor, m[i-cursor], m[i+1+cursor])
                        
                        if np.all(m[i-cursor] == m[i+1+cursor]) :
                            cursor += 1
                        else:
                            break  
                    
                    if not(i-cursor >= 0 and cursor+1+i < m.shape[0]):
                        return i+1 if j == 1 else (i+1) * 100
                    
            m = m.transpose()

    count = 0
    for m in shaped_map:
        count += get_lin_break(m)
    return count

def part2(data):
    shaped_map = [[]]
    for r in data:
        if len(r) == 0:
            shaped_map.append([])
        else:
            shaped_map[-1].append(list([0 if i == '.' else 1 for i in r]))
    
    for i in range(len(shaped_map)):
        shaped_map[i] = np.matrix(shaped_map[i])
        
    def get_lin_break(m):
        
        for j in range(2):
            
            for i in range(m.shape[0]-1):
                #print("i: {}".format(i))
                if np.all(m[i] == m[i+1]) or np.count_nonzero(m[i]-m[i+1]) == 1:
                    
                    cursor = 1
                    
                    if np.all(m[i] == m[i+1]):
                        jocker = True
                        #print('->',i-cursor, cursor+1+i, m[i-cursor], m[i+1+cursor], jocker and np.count_nonzero(m[i-cursor]-m[i+1+cursor]) <= 1)
                    else:
                        jocker = False
                        
                    while i-cursor >= 0 and cursor+1+i < m.shape[0]:
                        #print(i-cursor, cursor+1+i, m[i-cursor], m[i+1+cursor], jocker and np.count_nonzero(m[i-cursor]-m[i+1+cursor]) <= 1)
                        if jocker and np.count_nonzero(m[i-cursor]-m[i+1+cursor]) == 1:
                            jocker = False
                            cursor += 1
                        elif np.all(m[i-cursor] == m[i+1+cursor]) :
                            cursor += 1
                        else:
                            break  
                    
                    if not(i-cursor >= 0 and cursor+1+i < m.shape[0]):
                        return i+1 if j == 1 else (i+1) * 100
                    
            m = m.transpose()

    count = 0
    for m in shaped_map:
        #print(m, get_lin_break(m))
        count += get_lin_break(m)
    return count


if __name__ == "__main__":
    main()
