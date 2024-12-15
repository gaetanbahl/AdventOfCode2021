from collections import defaultdict

with open("input.txt", 'r') as f:
    positions = [int(l.strip().split(": ")[1]) for l in f.readlines()]

combination_occ = defaultdict(int)
rolls = range(1,4)
combinations = [sum([i,j,k]) for i in rolls for j in rolls for k in rolls]
for c in combinations:
    combination_occ[c] += 1

memo = dict()

def flip_key(pos, score, t):
    return ((pos[1],pos[0]), (score[1],score[0]), ((t+1)%2))

def flip_win(wins):
    return (wins[1], wins[0])

def play(pos, score, depth):
    t = depth % 2

    if (pos, score, t) in memo:
        #print("memo hit")
        return memo[pos, score, t]

    flipped_key = flip_key(pos, score, t)
    if flipped_key in memo:
        #print("flip memo hit")
        return flip_win(memo[flipped_key])

    wins = [0,0]

    for c,v in combination_occ.items():
        p_pos = pos[t]
        p_score = score[t]

        p_pos += c
        p_pos = p_pos % 10
        p_score += p_pos +1

        if p_score >= 21:
            wins[t] += v
        else:
            new_pos = list(pos)
            new_score = list(score)
            new_pos[t] = p_pos
            new_score[t] = p_score

            w = play(tuple(new_pos), tuple(new_score), depth+1)
            wins[0] += v * w[0]
            wins[1] += v * w[1]

    memo[pos, score, t] = tuple(wins)

    return wins

res = play((positions[0]-1, positions[1]-1), (0,0), 0)
print(res)
print(max(res))
