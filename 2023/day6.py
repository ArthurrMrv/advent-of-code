with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day6.txt", "r") as f:
    data = f.read().splitlines()
    
class Race:
    all_races = {}
    id_cursor = 0
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance
        self.id = self.id_cursor
        
        self.add_race(self.id, self)
        
    def get_time(self):
        return self.time
    
    def get_distance(self):
        return self.distance
    
    def get_id(self):
        return self.id
        
    @classmethod
    def add_race(cls,id, race):
        cls.all_races[id] = race
        cls.id_cursor += 1
    
    def __str__(self):
        return "(id: {}) Distance: {} - Time: {}".format(self.id, self.distance, self.time)
        pass
    
    @staticmethod
    def distance(speed, time):
        return speed * time
    
    @staticmethod
    def all_distances(time):
        return [Race.distance(i, time-i) for i in range(time+1)]
    
    @staticmethod
    def all_distancesAbove(time, record):
        return list(filter(lambda x: x > record, Race.all_distances(time)))
    
def part1():
    count = 1
    for i in range(Race.id_cursor):
        count *= len(Race.all_distancesAbove(Race.all_races[i].get_time(), Race.all_races[i].get_distance()))
    print(count)
    pass

def part2():
    real_race = {"time": '', "distance": ''}
    for i in range(Race.id_cursor):
        real_race["time"] += str(Race.all_races[i].get_time())
        real_race["distance"] += str(Race.all_races[i].get_distance())
    count = len(Race.all_distancesAbove(int(real_race["time"]), int(real_race["distance"])))
    print(count)
    pass


if __name__ == "__main__":
    time = []
    for i in data[0].split(":")[1].split(" "):
        if len(i):
            time.append(int(i))
    distance = []
    for i in data[1].split(":")[1].split(" "):
        if len(i):
            distance.append(int(i))
    for i in range(len(time)):
        j = Race(time[i], distance[i])
        
    part1()
    part2()