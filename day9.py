with open("day9_data.txt", 'r') as f:
   lines = f.readlines()

s = 0

for line in lines:
    initial_seq = line.split(' ')
    initial_seq = [int(e) for e in initial_seq]

    sequences = [initial_seq]

    seq = initial_seq
    while not(all(diff == 0 for diff in seq)):
        last_seq = list(seq)
        seq = []
        for i in range(len(last_seq)-1):
            seq.append(last_seq[i+1] - last_seq[i])
        sequences.append(seq)

    #for i in range(len(sequences)-1, 0, -1):
    #    print(i)
    #    sequences[i-1].append(sequences[i-1][-1] + sequences[i][-1])

    print(sequences)
    for i in range(len(sequences)-1, 0, -1):
        print(i)
        y = sequences[i-1][0] - sequences[i][0]
        sequences[i-1] = [y] + sequences[i-1]

    print(sequences)
    print(sequences[0][0])
    s += sequences[0][0]
print(s)

