import pandas as pd

with open("/Users/arthurmorvan/Documents/Dev/advent_of_code/2023/Data/day7_example.txt", "r") as f:
    data = f.read().splitlines()
    
def sort_hands(all_hands, 
               jokers = False, 
               cards_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q','K', 'A']):
    
    def diff_cards(cards):
            return tuple({*cards})
    
    def sort_types(hands, jokers = jokers):
        
        hands_types = {
            'five' : [],
            'four' : [],
            'full' : [],
            'three' : [],
            'two' : [],
            'one' : [],
            'high' : []
        }
        
        for h in hands:
            if jokers:
                h2 = h.copy()[0]
                nb_J = h2.count("J")
                h2 = ''
                for i in range(len(h.copy()[0])):
    
                    if h.copy()[0][i] != "J":
                        h2 += h.copy()[0][i]
                    
                repetitions = [h2.count(diff_cards(h2)[i]) for i in range(len(diff_cards(h2)))]

                if [repetitions.count(i)+nb_J for i in range(6)].count(5):
                    hands_types['five'].append(h)
                elif [repetitions.count(i)+nb_J for i in range(6)].count(4):
                    hands_types['four'].append(h)
                elif [repetitions.count(i) + repetitions.count(j) + nb_J for i in range(6) for j in range(6)].count(5):
                    hands_types['full'].append(h)
                elif [repetitions.count(i)+nb_J for i in range(6)].count(3):
                    hands_types['three'].append(h)
                elif [repetitions.count(i)+nb_J for i in range(6)].count(2) == 2:
                    hands_types['two'].append(h)
                elif [repetitions.count(i)+nb_J for i in range(6)].count(2):
                    hands_types['one'].append(h)
                else:
                    hands_types['high'].append(h)

            else:
                repetitions = [h[0].count(diff_cards(h[0])[i]) for i in range(len(diff_cards(h[0])))]

                if repetitions.count(5):
                    hands_types['five'].append(h)
                elif repetitions.count(4):
                    hands_types['four'].append(h)
                elif repetitions.count(3) and repetitions.count(2):
                    hands_types['full'].append(h)
                elif repetitions.count(3):
                    hands_types['three'].append(h)
                elif repetitions.count(2) == 2:
                    hands_types['two'].append(h)
                elif repetitions.count(2):
                    hands_types['one'].append(h)
                else:
                    hands_types['high'].append(h)
        
        return hands_types
    
    def sort_hands(hand1, hand2, cards_order):
        for i in range(len(hand1[0])):
            if cards_order.index(hand1[0][i]) > cards_order.index(hand2[0][i]):
                #print(f"{hand1[0]} > {hand2[0]}")
                return [hand2, hand1]
            elif cards_order.index(hand1[0][i]) < cards_order.index(hand2[0][i]):
                #print(f"{hand1[0]} < {hand2[0]}")
                return [hand1, hand2]
        return [hand1, hand2]
    
    def sort_kind(hands):

        cursor = 0
        while cursor < len(hands)-1:
            #print(cursor, sort_hands(hands[cursor], hands[cursor+1]))
            if sort_hands(hands[cursor], hands[cursor+1], cards_order) != [hands[cursor], hands[cursor+1]]:
                hands[cursor], hands[cursor+1] = sort_hands(hands[cursor], hands[cursor+1], cards_order)
                cursor = max(0, cursor-1)
            else:
                cursor += 1
                
        return hands
    
    devide = sort_types(all_hands)
        
    keys = ['high', 'one', 'two', 'three', 'full', 'four', 'five']

    ans = []
    for k in keys:
        ans+= sort_kind(devide[k])
    
    return ans


def part1(hands):
    sorted_rands = sort_hands(hands)
    
    #print([h[0] for h in sorted_rands])
    print(sum([(i+1)*int(sorted_rands[i][1]) for i in range(len(hands))]))
    pass

def part2(hands):
    sorted_rands = sort_hands(hands, jokers = True, cards_order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'A', 'Q','K'])
    print(sorted_rands)
    print(sum([(i+1)*int(sorted_rands[i][1]) for i in range(len(hands))]))


if __name__ == "__main__":
    hands = [i.split(" ") for i in data]
    part1(hands.copy())
    part2(hands.copy())
