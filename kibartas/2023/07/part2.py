from functools import cmp_to_key
from collections import Counter

input = [x.split() for x in open('input.txt', 'r').read().strip().split('\n')]

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def is_two_pair(hand):
    counters = Counter(hand)
    return list(counters.values()).count(2) == 2

def is_one_pair(hand):
    counters = Counter(hand)
    return list(counters.values()).count(2) == 1

def hand_key(hand):
    hand = ''.join(sorted(hand))
    counts = Counter(hand)
    joker_count = counts['J']
    del counts['J']
    lst_counts = sorted(list(counts.values()), reverse=True)
    # 5 of a kind
    if hand == hand[0] * len(hand): 
        return 7
    elif joker_count != 0 and 5 - joker_count in lst_counts:
        return 7
    # 4 of a kind
    elif hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4:
        return 6
    elif joker_count != 0 and 4 - joker_count in lst_counts:
        return 6
    # Full house
    elif hand.count(hand[0]) == 3 and hand.count(hand[3]) == 2:
        return 5
    elif hand.count(hand[0]) == 2 and hand.count(hand[2]) == 3:
        return 5
    elif joker_count != 0 and lst_counts[0] + lst_counts[1] + joker_count == 5:
        return 5
    # 3 of a kind
    elif hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
        return 4
    elif joker_count != 0 and lst_counts[0] + joker_count == 3:
        return 4
    # 2 pair
    elif is_two_pair(hand):
        return 3
    elif joker_count != 0 and lst_counts[0] + lst_counts[1] + joker_count == 4:
        print(hand)
        return 3
    # 1 pair
    elif is_one_pair(hand):
        return 2
    elif joker_count != 0 and lst_counts[0] + joker_count == 2:
        return 2
    else:
        return 1

def hand_cmp(x, y):
    key_1, key_2 = hand_key(x[0]), hand_key(y[0])
    if key_1 == key_2:
        for el, o_el in zip(x[0], y[0]):
            if cards.index(el) < cards.index(o_el):
                return 1
            elif cards.index(el) > cards.index(o_el):
                return -1
        return 0
    elif key_1 > key_2:
        return 1
    else:
        return -1


sr_hands = sorted(input, key=cmp_to_key(hand_cmp))
prod_sum = 0
for i, hand in enumerate(sr_hands):
    prod_sum += int(hand[1]) * (i+1)


result = prod_sum
print("Result: {}".format(result))
