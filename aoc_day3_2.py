digits = "0123456789"

s = 0

with open('aoc_day3_data.txt') as f:
    lines = f.readlines()

gears = {}

for q in range(len(lines)):
    line = lines[q]
    i = 0
    while i <= len(line) - 1:
        j = 0
        str_n = ""
        n = 0
        while (i+j <= len(line) - 1) and (line[i+j] in digits):
            str_n = str_n + line[i+j]
            j += 1
        if str_n != "":
            n = int(str_n)
        if n != 0:
            # on check les voisins
            # on check les voisins du haut
            if q > 0:
                for r in range(j):
                    if lines[q-1][i+r] == "*":
                        try:
                            s += n * gears[(q-1, i+r)]
                        except KeyError:
                            gears[(q-1, i+r)] = n
            # ceux du bas
            if q < len(lines) - 1:
                for r in range(j):
                    if lines[q+1][i+r] == "*":
                        try:
                            s += n * gears[(q+1, i+r)]
                        except KeyError:
                            gears[(q+1, i+r)] = n
            # ceux à gauche
            if i > 0:
                # et aussi dans les angles
                if q > 0:
                    if lines[q-1][i-1] == "*":
                        try:
                            s += n * gears[(q-1, i-1)]
                        except KeyError:
                            gears[(q-1, i-1)] = n
                if q < len(lines) - 1:
                    if lines[q+1][i-1] == "*":
                        try:
                            s += n * gears[(q+1, i-1)]
                        except KeyError:
                            gears[(q+1, i-1)] = n
                if line[i - 1] == "*":
                    try:
                        s += n * gears[(q, i-1)]
                    except KeyError:
                        gears[(q, i-1)] = n
            # ceux à droite
            if i + j <= len(line) - 1:
                if q > 0:
                    if lines[q-1][i+j] == "*":
                        try:
                            s += n * gears[(q-1, i+j)]
                        except KeyError:
                            gears[(q-1, i+j)] = n
                if q < len(lines) - 1:
                    if lines[q+1][i+j] == "*":
                        try:
                            s += n * gears[(q+1, i+j)]
                        except KeyError:
                            gears[(q+1, i+j)] = n
                if line[i+j] == "*":
                    try:
                        s += n * gears[(q, i+j)]
                    except KeyError:
                        gears[(q, i+j)] = n
        i = i + 1 + j

print(s)
