from functools import cmp_to_key

cards_strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
strength_order = {key: i for i, key in enumerate(cards_strength)}

def compare_strength(item1, item2):
    j = 0
    while j < len(item1) and item1[j] == item2[j]:
        if j == len(item1):
            return 0
        j += 1
    if strength_order[item1[j]] < strength_order[item2[j]]:
        return -1
    else:
        return 1

s = 0

fives = {}
fours = {}
fulls = {}
threes = {}
two_pairs = {}
one_pairs = {}
high_cards = {}


with open('aoc_day7_data.txt') as f:
    lines = f.readlines()

for w in lines:
    hand = w[:5]
    bid = int(w[6:9])



    d = {}
    i = 0
    n = 0
    m = 0
    l = ""
    while i < 5:
        if w[i] == l or i == 0:
            m += 1
        else:
            n = max(n, m+1)
            m = 0
            l = w[i]
        try:
            d[w[i]] += 1
        except KeyError:
            d[w[i]] = 1
        i += 1

    if len(d) == 1:
        fives[hand] = bid
    elif max(d.values()) == 4:
        fours[hand] = bid
    elif len(d) == 2:
        fulls[hand] = bid
    elif max(d.values()) == 3:
        threes[hand] = bid
    elif len(d) == 3:
        two_pairs[hand] = bid
    elif len(d) == 4:
        one_pairs[hand] = bid
    else:
        high_cards[hand] = bid


fives = {key:fives[key] for key in sorted(fives.keys(), key=cmp_to_key(compare_strength))}
fours = {key:fours[key] for key in sorted(fours.keys(), key=cmp_to_key(compare_strength))}
fulls = {key:fulls[key] for key in sorted(fulls.keys(), key=cmp_to_key(compare_strength))}
threes = {key:threes[key] for key in sorted(threes.keys(), key=cmp_to_key(compare_strength))}
two_pairs = {key:two_pairs[key] for key in sorted(two_pairs.keys(), key=cmp_to_key(compare_strength))}
one_pairs = {key:one_pairs[key] for key in sorted(one_pairs.keys(), key=cmp_to_key(compare_strength))}
high_cards = {key:high_cards[key] for key in sorted(high_cards.keys(), key=cmp_to_key(compare_strength))}

res = {**fives, **fours, **fulls, **threes, **two_pairs, **one_pairs, **high_cards}
print(res)

r = 1
for bid in reversed(res.values()):
    print(r, bid)
    s += r * bid
    r += 1
print(s)