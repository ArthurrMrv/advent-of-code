with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/day4.txt", 'r') as f:
    data = f.read().splitlines()
    
def car_num(line):
    line = line.split(':')[1]
    winner, cars = tuple(line.split('|'))
    w = set()
    c = set()
    for i in winner.split(' '):
        if len(i):
            w.add(int(i))
    for i in cars.split(' '):
        if len(i):
            c.add(int(i))
    return len(c.intersection(w))

def part1():
    sum = 0    
    for i in data:
        sum += pow(2, car_num(i)-1) if car_num(i) > 0 else 0
    print(sum)

def part2():
    
    deck = dict([i, 1] for i in range(1, len(data)+1))
    ans = 0
    

    for i in range(1, len(data)+1):
            num = car_num(data[i-1])
            for j in range(i+1,i+1+num):
                deck[j] += 1*deck[i]

    print(sum(deck.values()))
    
part1()
part2()