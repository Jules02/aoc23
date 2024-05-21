from math import gcd
from functools import reduce

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

def lcm_list(lst):
    return reduce(lcm, lst)


with open("day8_data.txt") as f:
    lines = f.readlines()

path = lines[0][:-1]

positions = []
nodes = {}
for i in range(2, len(lines)):
    if lines[i][2] == 'A':
        positions.append(str(lines[i][0:3]))
    nodes[str(lines[i][0:3])] = (str(lines[i][7:10]), str(lines[i][12:15]))

steps = []
for k in range(len(positions)):
    i = 0
    steps.append(0)
    while positions[k][2] != 'Z':
        steps[k] += 1

        j = i % len(path)
        direction = path[j]
   
        (left, right) = (nodes[positions[k]][0], nodes[positions[k]][1])
        if direction == 'L':
            positions[k] = left
        else:
            positions[k] = right
    
        i += 1

print(steps)
print(lcm_list(steps))


