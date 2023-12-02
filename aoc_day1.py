s = 0;

with open('aoc_data.txt') as f:
    lines = f.readlines()

numbers = "123456789"

for w in lines:
    x = 0
    y = 0

    i = 0
    j = len(w) - 1
    while i <= (len(w) - 1):
        if w[i] in numbers:
            x = w[i]
            break
        i= i + 1
    while j >= i:
        if w[j] in numbers:
            y = w[j]
            break
        j = j - 1
    s += int(x)*10 + int(y)

print(s)