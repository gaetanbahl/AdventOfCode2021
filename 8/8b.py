from collections import defaultdict

with open("input.txt", 'r') as f:
    lines = [l.strip().split("|") for l in f.readlines()]


s = 0
for l in lines:

    digits = [set(d) for d in l[0].split(" ")]

    gnn = [0 for i in range(10)]

    new_digits = []
    for d in digits:
        if len(d) == 2:
            gnn[1] = d
        elif len(d) == 3:
            gnn[7] = d
        elif len(d) == 4:
            gnn[4] = d
        elif len(d) == 7:
            gnn[8] = d
        else:
            new_digits.append(d)
    digits = new_digits

    new_digits = []
    for d in digits:
        if len(d) == 6:
            sub = list(gnn[8] - d)[0]
            if sub in gnn[1]:
                gnn[6] = d
            elif sub in gnn[4]:
                gnn[0] = d
            else:
                gnn[9] = d
        else:
            new_digits.append(d)

    digits = new_digits

    tr = gnn[8] - gnn[6]

    bl = gnn[8] - gnn[9] 

    gnn[5] = gnn[8] - tr - bl

    digits.remove(gnn[5])

    new_digits = []
    for d in digits:
        if len(d) == 5 and d!=gnn[5]:
            if list(bl)[0] in d and list(tr)[0] in d:
                gnn[2] = d
            else:
                gnn[3] = d

    right = [set(x) for x in l[1].strip().split(" ")]

    out = ""
    for n in right:
        out += str(gnn.index(n))
    s += int(out)

print(s)

    
