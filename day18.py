import numpy as np


with open("data.txt") as f:
    puzzle = f.readlines()


gl_terrain = [ [0 for _ in range(900)] for _ in range(900)]
gl_terrain = np.array(gl_terrain)
gl_interieur = [ [0 for _ in range(900)] for _ in range(900)]
gl_interieur = np.array(gl_interieur)

s = 0
for l in puzzle:
    if l[0] == "L":
        s += int(l[2])
print(s)

(i, j) = (0, 0) # starting point

for l in puzzle:
    direction = l[0]
    length = int(l[2])

    if direction == "R":
        for _ in range(length):
            gl_terrain[i][j] = 1
            j += 1
    if direction == "L":
        for _ in range(length):
            gl_terrain[i][j] = 1
            j -= 1
    if direction == "D":
        for _ in range(length):
            gl_terrain[i][j] = 1
            i += 1
    if direction == "U":
        for _ in range(length):
            gl_terrain[i][j] = 1
            i -= 1

for i in range(len(gl_terrain)):
    b = False   # indique si l'on se trouve à l'intérieur du contour
    for j in range(len(gl_terrain[i])-1):
        if b and (gl_terrain[i][j] == 1 and gl_terrain[i][j+1] == 0):
            # on sort du contour
            gl_interieur[i][j] = 1
            b = False
        elif not(b) and (gl_terrain[i][j] == 1 and gl_terrain[i][j+1] == 0):
            # on entre dans le contour
            gl_interieur[i][j] = 1
            b = True
        elif gl_terrain[i][j] == 1:
            gl_interieur[i][j] = 1
        elif b:
            # on est à l'intérieur du contour
            gl_interieur[i][j] = 1
        else:
            gl_interieur[i][j] = 0

print(np.sum(gl_terrain))
print(np.sum(gl_interieur))

print(gl_terrain[0])
print(gl_interieur)
