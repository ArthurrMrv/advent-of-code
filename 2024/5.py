# --- DAY 5 --- #
# "Fall seven times and stand up eight." - Japanese Proverb

# Data Path: data/5.txt || data/5_exemple.txt
from queue import Queue

def main():
    data = get_data(5, False)
    print("-- Day 5 --")
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
    
def part1(data):
    instructions, execution = data
    ordering = get_ordering(instructions)
    execution = [e.split(",") for e in execution]
    
    sumo = 0
    for e in execution:
        if is_valid(e, ordering):
            sumo += int(e[len(e) // 2])
            
    return sumo
    
def part2(data):
    instructions, execution = data
    ordering = get_ordering(instructions)
    execution = [e.split(",") for e in execution]
    
    sumo = 0
    for e in execution:
        if not(is_valid(e, ordering)):
            e = reorder(e, ordering)
            sumo += int(e[len(e) // 2])
    return sumo
    
def get_data(i, exemple=False):
    path = f"data/5_exemple.txt" if exemple else f"data/5.txt"
    with open(path, "r") as f:
        data = [l.strip() for l in f.readlines()]
    separator = data.index("")
    return data[:separator], data[separator+1:]

def get_ordering(instructions):
    ordering : dict[int]= dict()
    for instruction in instructions:
        a, b = instruction.split("|")
        if b not in ordering:
            ordering[b] = set()
        ordering[b].add(a)
    return ordering

def is_valid(execution, ordering : dict):
    set_execution = set(execution)
    executed = set()
    for e in execution:
        if len(ordering.get(e, set()).intersection(set_execution) - executed):
            return False
        executed.add(e)
    return True

def reorder(execution, ordering : dict):
    set_execution = set(execution)
    executed = set()
    sorted_execution = []
    
    queue = Queue()
    for e in execution:
        queue.put(e)
        
    it = 1_000_000
    while it > 0 and queue.qsize():
        it -= 1
        e = queue.get()
        if len(ordering.get(e, set()).intersection(set_execution) - executed):
            queue.put(e)
        else:
            executed.add(e)
            sorted_execution.append(e)
    
    return sorted_execution

    
if __name__ == "__main__":
    main()
    a = set()
    b = set()
    a.intersection
    