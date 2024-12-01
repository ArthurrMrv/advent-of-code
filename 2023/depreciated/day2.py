with open("day2.txt") as f:
    data = f.read().splitlines()
    
# for i in range(len(data)):
#     data[i] = data[i].replace(';', ',')
# with open("day2.txt", 'w') as f:
#     for d in data:
#         f.write(d + '\n')

ids = 0
def is_valid(manche):
    for manche in manches:
        dict_partie = {'red': 0, 'blue':0, 'green':0}
        showed = manche.split(',')
        for j in showed:
            number, color = j.split(" ")[1], j.split(" ")[2]
            #print(f".{number}.{color}.")
            dict_partie[color] += int(number)
        
        if dict_partie['red'] > 12 or  dict_partie["green"] > 13 or dict_partie["blue"] > 14:
            return False
            
    return True

def get_min(manches):
    dict_mini = {'red': None, 'blue': None, 'green':None}
    
    
    for manche in manches:
        dict_partie = {'red': 0, 'blue':0, 'green':0}
        showed = manche.split(',')
        for j in showed:
            number, color = j.split(" ")[1], j.split(" ")[2]
            
            dict_partie[color] += int(number)
        
        for k in dict_partie:
            if dict_mini[k] is None or dict_mini[k] < dict_partie[k]:
                dict_mini[k] = dict_partie[k]
    
    to_mult = []
    for k in dict_mini:
        if dict_mini[k] != None:
            to_mult.append(dict_mini[k])
    
    ans = 1
    for i in to_mult:
        ans *= i
    #print(ans)
    return ans

# for i in data:
#     game, content = i.split(':')[0], i.split(':')[1]
#     manches = content.split(';')
#     if is_valid(manches):
    
#         ids += int(game.split(' ')[1])
rep = 0
for i in data:
    game, content = i.split(':')[0], i.split(':')[1]
    manches = content.split(';')
    #print(f"{i} : {get_min(manches)}")
    rep += get_min(manches)
     
print(rep)