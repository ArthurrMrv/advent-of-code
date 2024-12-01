from tqdm import tqdm
import matplotlib.pyplot as plt

def main():
    with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day10.txt", "r") as f:
        data = f.read().splitlines()
        
    print("Part1: {}".format(len(part1(data))//2))
    print("Part2: {}".format(part2(data, part1(data))))

def can_go(data, x, y, visited = ()):
    connections : dict = {
        'S': {'N' : 1,
              'S' : 1,
              'E' : 1,
              'W' : 1},
        '|' : {'N' : 1,
               'S' : 1,
               'E' : 0,
               'W' : 0},
        '-' : {'N' : 0,
                'S' : 0,
                'E' : 1,
                'W' : 1},
        'L' : {'N' : 1,
                'S' : 0,
                'E' : 1,
                'W' : 0},
        '7' : {'N' : 0,
                'S' : 1,
                'E' : 0,
                'W' : 1},
        'F' : {'N' : 0,
                'S' : 1,
                'E' : 1,
                'W' : 0},
        'J' : {'N' : 1,
               'S' : 0,
                'E' : 0,
                'W' : 1},
        '.' : {'N' : 0,
                'S' : 0,
                'E' : 0,
                'W' : 0}
    }
    opposites : dict = {
        'N' : 'S',
        'S' : 'N',
        
        'E' : 'W',
        'W' : 'E',
    }
    
    to_corr : dict = {
        'N' : (0, -1),
        'S' : (0, 1),
        'E' : (1, 0),
        'W' : (-1, 0)
    }
    
    ans = []
    for d in ['N', 'S', 'E', 'W']:
        if connections[data[y][x]][d] and 0 <= y+to_corr[d][1] < len(data) and 0 <= x+to_corr[d][0] < len(data[0]) and (x+to_corr[d][0], y+to_corr[d][1]) not in visited and connections[data[y+to_corr[d][1]][x+to_corr[d][0]]][opposites[d]]:
            #print(f"'{data[y][x]}' Can go {d} from {x, y} to {x+to_corr[d][0], y+to_corr[d][1]}, ({data[y][x]} -> {data[y+to_corr[d][1]][x+to_corr[d][0]]})")
            ans.append((x+to_corr[d][0], y+to_corr[d][1]))
            
    return ans

def part1(data):
    MAX = len(data)*len(data[0])
    b = tqdm(MAX)
        
    def find_boucle(data, corr, path = [], visited = ()):
        
        current_p = {'visited' : (), "path" : path.copy(), "corr" : corr, 'continue' : 1}
        plan = {1 : [current_p]}
        
        while current_p != None:

            for k in plan.copy():
                for p in plan[k].copy():
                    if k < max(list(plan.keys())) and p["continue"] == 0 and p["path"][-1] != corr:
                        plan[k].remove(p)
                if len(plan[k]) == 0:
                    del plan[k]
            
            for possible_corr in can_go(data, current_p["corr"][0], current_p["corr"][1], current_p["visited"]):
                if len(current_p["path"])+1 not in plan:
                    plan[len(current_p["path"])+1] = []
                
                plan[len(current_p["path"])+1].append({
                    'visited' : current_p["visited"]+(current_p["corr"], ),
                    'path' : current_p["path"]+[possible_corr],
                    'corr' : possible_corr,
                    'continue' : 1 if data[possible_corr[1]][possible_corr[0]] != 'S' else 0
                })
            
            current_p["continue"] = 0
            
            current_p = None
            keys = list(plan.keys())
            keys.sort()
            for k in keys:
                
                if current_p != None:
                    break
                
                for p in plan[k].copy():
                    if p["continue"]:
                        current_p = p
                        break
            
            b.update(1)
        
        b.update(MAX-b.n)
        return plan[max(list(plan.keys()))][0]["path"]
        
    def loc_s(data):
        for y in range(len(data)):
            if 'S' in data[y]:
                return (data[y].index('S'), y)
    
    return find_boucle(data, loc_s(data), path=[loc_s(data)])

def part2(data, path):
    connections : dict = {
        'S': {'N' : 1,
              'S' : 1,
              'E' : 1,
              'W' : 1},
        '|' : {'N' : 1,
               'S' : 1,
               'E' : 0,
               'W' : 0},
        '-' : {'N' : 0,
                'S' : 0,
                'E' : 1,
                'W' : 1},
        'L' : {'N' : 1,
                'S' : 0,
                'E' : 1,
                'W' : 0},
        '7' : {'N' : 0,
                'S' : 1,
                'E' : 0,
                'W' : 1},
        'F' : {'N' : 0,
                'S' : 1,
                'E' : 1,
                'W' : 0},
        'J' : {'N' : 1,
               'S' : 0,
                'E' : 0,
                'W' : 1},
        '.' : {'N' : 0,
                'S' : 0,
                'E' : 0,
                'W' : 0}
    }
    
    PIPE_CELL = -1
    EMPTY_CELL = 0
    IN_PIPE_CELL = 1
    
    empty_board = [[IN_PIPE_CELL for j in range(len(data[0])*2)] for i in range(len(data)*2)]
    count_pipes = 0
    for corr in path:
        
        to_impl = connections[data[corr[1]][corr[0]]]
        
        if to_impl['N']:
            empty_board[corr[1]*2-1][corr[0]*2] = PIPE_CELL
            count_pipes += 1
        if to_impl['S']:
            empty_board[corr[1]*2+1][corr[0]*2] = PIPE_CELL
            count_pipes += 1
        if to_impl['E']:
            empty_board[corr[1]*2][corr[0]*2+1] = PIPE_CELL
            count_pipes += 1
        if to_impl['W']:
            empty_board[corr[1]*2-1][corr[0]*2-1] = PIPE_CELL
            count_pipes += 1
            
        empty_board[corr[1]*2][corr[0]*2] = PIPE_CELL
        count_pipes += 1
    
    
    to_visit = set([(x, y) for x in range(len(empty_board[0])) for y in range(0, len(empty_board), len(empty_board)-1)])
    
    for c in [(x, y) for x in range(0, len(empty_board[0]), len(empty_board[0])-1) for y in range(len(empty_board))]:
        to_visit.add(c)
    
    while len(to_visit) > 0:
        x, y = to_visit.pop()
        match empty_board[y][x]:
            case -1:
                pass
            case 0:
                for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                            if (0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board)) and empty_board[y+c[1]][x+c[0]] == IN_PIPE_CELL:
                                to_visit.add((x+c[0], y+c[1]))
            case 1:
                for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    if 0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board) and empty_board[y+c[1]][x+c[0]] == EMPTY_CELL:
                        empty_board[y][x] = EMPTY_CELL
                        for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                            if (0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board)):
                                to_visit.add((x+c[0], y+c[1]))
                        break
                    if not (0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board)):
                        empty_board[y][x] = EMPTY_CELL
                        for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                            if (0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board)):
                                to_visit.add((x+c[0], y+c[1]))
                        break

    fig, ax = plt.subplots()

    ax.imshow(empty_board)

    plt.show()
    
    return sum([sum([1 if empty_board[y][x] == IN_PIPE_CELL else 0 for x in range(0, len(empty_board[0]), 2)]) for y in range(0, len(empty_board), 2)])

# def part2(data, path):
#     PIPE_CELL = -1
#     EMPTY_CELL = 0
#     IN_PIPE_CELL = 1
#     empty_board = [[IN_PIPE_CELL for j in range(len(data[0]))] for i in range(len(data))]
#     for corr in path:
#         empty_board[corr[1]][corr[0]] = PIPE_CELL
        
#     fig, ax = plt.subplots()

#     ax.imshow(empty_board)

#     plt.show()
    
#     to_visit = set([(x, y) for x in range(len(empty_board[0])) for y in range(0, len(empty_board), len(empty_board)-1)])
#     for c in [(x, y) for x in range(0, len(empty_board[0]), len(empty_board[0])-1) for y in range(len(empty_board))]:
#         to_visit.add(c)
    
#     while len(to_visit) > 0:
#         x, y = to_visit.pop()
#         match empty_board[y][x]:
#             case -1:
#                 pass
#             case 0:
#                 for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
#                             if (0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board)) and empty_board[y+c[1]][x+c[0]] == IN_PIPE_CELL:
#                                 to_visit.add((x+c[0], y+c[1]))
#             case 1:
#                 for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
#                     if 0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board) and empty_board[y+c[1]][x+c[0]] == EMPTY_CELL:
#                         empty_board[y][x] = EMPTY_CELL
#                         for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
#                             if (0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board)):
#                                 to_visit.add((x+c[0], y+c[1]))
#                         break
#                     if not (0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board)):
#                         empty_board[y][x] = EMPTY_CELL
#                         for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
#                             if (0 <= x+c[0] < len(empty_board[0]) and 0 <= y+c[1] < len(empty_board)):
#                                 to_visit.add((x+c[0], y+c[1]))
#                         break
    
#     fig, ax = plt.subplots()

#     ax.imshow(empty_board)

#     plt.show()

                    
#     return sum([sum([1 if empty_board[y][x] == IN_PIPE_CELL else 0 for x in range(len(empty_board[0]))]) for y in range(len(empty_board))])


if __name__ == "__main__":
    main()