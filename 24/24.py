from collections import deque
from tqdm import trange

with open("input2.txt", 'r') as f:
    lines = deque([l.strip().split(" ") for l in f.readlines()])


def decode(instr):

    op = instr[0]

    out = instr[1]

    if op == "inp":
        state[out] = input_sn.popleft()
        return

    if instr[2] in state:
        b = state[instr[2]]
    else:
        b = int(instr[2])

    if op == "add":
        state[out] += b
    elif op == "mul":
        state[out] *= b
    elif op == "div":
        state[out] = state[out] // b
    elif op == "mod":
        state[out] = state[out] % b
    elif op == "eql":
        state[out] = int(state[out] == b)


#for i in trange(100000000000000,11111111111111,-1):
#s = str(i).zfill(14)
s = "33"
#if "0" in s:
#    continue
state = {"w":0, "x":0, "y":0, "z":0}
input_sn = deque([int(i) for i in list(s)])

for l in lines:
    decode(l)

if state["z"] == 0:
    print(s)
print(state)
