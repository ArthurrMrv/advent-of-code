
def main():
    with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day9.txt", "r") as f:
        data = [[int(i) for i in l.split(" ")] for l in f.read().splitlines()]
        
    print("From part 1 : {}".format(part1(data)))
    print("From part 2 : {}".format(part2(data)))

def part1(data):
    
    def get_sequence(l):
        ans = []
        current = l[0]
        for e in l[1:]:
            ans.append(e-current)
            current = e
        return ans
    
    ans = 0
    for d in data:
        it = 0
        curr_ans = 0
        current_d = d
        layers = []
        while get_sequence(current_d).count(0) < (len(current_d)-1):
            current_d = get_sequence(current_d)
            it += 1
            layers.append(current_d[-1])
        layers.reverse()
        for l in layers:
            curr_ans += l
        curr_ans += d[-1]
        ans += curr_ans
    return ans
            
        
    
    
    
    

def part2(data):
    def get_sequence(l):
        ans = []
        current = l[0]
        for e in l[1:]:
            ans.append(e-current)
            current = e
        return ans
    
    ans = 0
    for d in data:
        it = 0
        curr_ans = 0
        current_d = d.copy()
        current_d.reverse()
        layers = []
        while get_sequence(current_d).count(0) < (len(current_d)-1):
            current_d = get_sequence(current_d)
            it += 1
            layers.append(current_d[-1])
        layers.reverse()
        for l in layers:
            curr_ans += l
        curr_ans += d[0]

        ans += curr_ans
    return ans


if __name__ == "__main__":
    main()