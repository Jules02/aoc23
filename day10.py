connecting_rules = {
    "|": ("N", "S"),
    "|": ("S", "N"),
    "-": ("E", "W"),
    "-": ("W", "E"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("S", "W"),
    "F": ("S", "E"),
    ".": ("", "")
}


starting_coords = (..., ...)
starting_tile = ...

def way(tile1, tile2):
    if (connecting_rules[tile1][1], connecting_rules[tile2][0]) in [("N", "S"), ("S", "N"), ("E", "W"), ("W", "E")]:
        return True
    return False

'''
for (i, j) in adjacent(starting_coords):
    if way(starting_tile, grid((i, j))):
        for (k, l) in adjacent(starting_coords):
            if (k, l) != (i, j):
                explore((i, j), (k, l))

def explore(c1, c2):
    (i, j) = c1
    (last_i, last_j) = starting_coords
    (k, l) = c2
    (last_k, last_l) = starting_coords
    while (i, j) != (k, l) and b:
        b = False
        k += 1
        # Exploration vers la droite
        for (x, y) in adjacent((i, j)):
            if (x, y) != (last_i, last_j) and way(grid((i, j)), grid((x, y))):
                (last_i, last_j) = (i, j)
                (i, j) = (x, y)
                b = True
        # Exploration vers la gauche
        for (x, y) in adjacent((k, l)):
            if (x, y) != (last_k, last_l) and way(grid((k, l)), grid((x, y))):
                (last_k, last_l) = (k, l)
                (k, l) = (x, y)
                b = True
    print(k)

def adjacent(c):
    (x, y) = c
    l = []
    if x > 0:
        l.append((x-1, y))
    if x < len(grid) - 1:
        l.append((x+1, y))
    if y > 0:
        l.append((x, y-1))
    if y < len(grid[0]) - 1:
        l.append((x, y+1))
    return l'''
