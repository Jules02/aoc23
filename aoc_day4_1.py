digits = "0123456789"

s = 0

with open('aoc_day4_data.txt') as f:
    lines = f.readlines()

for line in lines:
    matches = 0
    winning_numbers = []
    i = 0
    while line[i] != ":":
        i += 1
    i += 2
    while line[i] != "|":
        winning_numbers.append(line[i:i+2])
        i += 3
    i += 2
    while i <= len(line) - 1:
        if line[i:i+2] in winning_numbers:
            matches += 1
        i += 3
    if matches != 0:
        s += 2**(matches-1)

print(s)