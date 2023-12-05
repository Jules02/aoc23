str_colors = ["blue", "red", "green"]
digits = "0123456789"
R = 12; G = 13; B = 14
s = 0

with open('aoc_day2_data.txt') as f:
    lines = f.readlines()

for w in lines:
    correctness = True
    w_col_set = {"blue": 0, "red": 0, "green": 0}
    q = 0
    str_id = ""
    while w[5+q] in digits:
        str_id = str_id + w[5+q]
        q += 1
    id = int(str_id)
    i = 7 + q
    while i <= len(w) - 1:
        j = 0
        str_n = ""
        while w[i+j] in digits:
            str_n = str_n + w[i+j]
            j += 1
        n = int(str_n)
        i = i + 1 + j
        r = 0
        b = True
        while (r <= len(str_colors) - 1) and b:
            m = str_colors[r]
            k = 0
            b2 = True
            while (k <= len(m) - 1) and (i + k <= len(w) - 1) and b2:
                if w[i + k] != m[k]:
                    b2 = False
                k += 1
            if k == len(m) and b2:
                w_col_set[m] += int(n)
                if i + k >= len(w) - 1:
                    correctness = correctness and (w_col_set["red"] <= R and w_col_set["green"] <= G and w_col_set["blue"] <= B)
                    w_col_set = {"blue": 0, "red": 0, "green": 0}
                elif w[i + k] == ";":
                    correctness = correctness and (w_col_set["red"] <= R and w_col_set["green"] <= G and w_col_set["blue"] <= B)
                    w_col_set = {"blue": 0, "red": 0, "green": 0}
                i += k + 2
                b = False
            r += 1

    if correctness:
        s += id
print(s)

