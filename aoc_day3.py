digits = "0123456789"
symbols = "#*+=/&%@$-"

s = 0

with open('aoc_day3_data.txt') as f:
    lines = f.readlines()

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
            b = False
            # on check les voisins du haut
            if q > 0:
                for r in range(j):
                    if lines[q-1][i+r] in symbols:
                        print("test")
                        b = True
            # ceux du bas
            if q < len(lines) - 1:
                for r in range(j):
                    if lines[q+1][i+r] in symbols:
                        b = True
            # ceux à gauche
            if i > 0:
                # et aussi dans les angles
                if q > 0:
                    if lines[q-1][i-1] in symbols:
                        b = True
                if q < len(lines) - 1:
                    if lines[q+1][i-1] in symbols:
                        b = True
                if line[i - 1] in symbols:
                    b = True
            # ceux à droite
            if i + j <= len(line) - 1:
                if q > 0:
                    if lines[q-1][i+j] in symbols:
                        b = True
                if q < len(lines) - 1:
                    if lines[q+1][i+j] in symbols:
                        b = True
                if line[i+j] in symbols:
                    b = True
            if b:
                print("n: " + str(n))
                s += n
        i = i + 1 + j

print(s)
