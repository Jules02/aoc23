letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
with open('aoc_day5_data.txt') as f:
    lines = f.readlines()

seeds = []
i = 7
while i <= len(lines[0]) - 1:
    str_n = ""
    j = 0
    while (i + j <= len(lines[0]) - 1) and (lines[0][i + j] != " "):
        str_n = str_n + lines[0][i + j]
        j += 1
    seeds.append(int(str_n))
    i = i + j + 1

r = 2
maps = []
map_corr = {}
while r <= len(lines) - 1:
    line = lines[r]
    if line[0] == "\n":
        maps.append(map_corr)
        map_corr = {}
    elif line[0] in letters:
        pass
    else:
        j = 0
        str_dest = ""
        while line[j] in digits:
            str_dest = str_dest + line[j]
            j += 1
        dest = int(str_dest)
        j+=1
        str_src = ""
        while line[j] in digits:
            str_src = str_src + line[j]
            j += 1
        src = int(str_src)
        j += 1
        range_length = int(line[j:])
        for i in range(range_length):
            map_corr[src+i] = dest+i
    r += 1

maps.append(map_corr)

loc_numbers = []

# for seed in seeds:
#     c = seed
#     for map_corr in maps:
#         try:
#             c = map_corr[c]
#         except KeyError:
#             # on laisse c inchangé
#             pass
#     loc_numbers.append(c)
#
# print(min(loc_numbers))
