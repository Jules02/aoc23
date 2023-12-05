digits = "0123456789"

card_matches = {}
card_copies = {}

with open('aoc_day4_data.txt') as f:
    lines = f.readlines()

for line in lines:
    matches = 0

    winning_numbers = []

    i = 5
    while line[i] != ":":
        i += 1
    str_card_id = line[5:i]
    card_id = int(str_card_id)
    print(card_id)

    i += 2
    while line[i] != "|":
        winning_numbers.append(line[i:i+2])
        i += 3
    i += 2
    while i <= len(line) - 1:
        if line[i:i+2] in winning_numbers:
            matches += 1
        i += 3
    card_matches[card_id] = matches
    card_copies[card_id] = 1

for i in range(1, len(card_matches)+1):
    m = card_matches[i]
    for k in range(1, m+1):
        card_copies[i+k] += card_copies[i]

s = sum(card_copies.values())

print(s)