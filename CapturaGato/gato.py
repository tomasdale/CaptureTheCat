# encoding: utf-8

import importlib
import sys
import random
import math

cat    = eval(sys.argv[1])
blocks = eval(sys.argv[2])
exits  = eval(sys.argv[3])

def valid_movements(cat, blocked) :
    valids = []
    candidates = movements(cat)
    for cand in candidates :
        if not (cand[0] < 0 or cand[0] > 10 or
            cand[1] < 0 or cand[1] > 10 or
            tuple(cand[:2]) in blocked) :
            valids.append( cand )
    return valids


def movements(cat) :
    candidates = None
    if cat[0] % 2 == 0 :
        candidates = [
            (cat[0] - 1, cat[1] - 1, "NW"),
            (cat[0] - 1, cat[1],     "NE"),
            (cat[0], cat[1] - 1,     "W"),
            (cat[0], cat[1] + 1,     "E"),
            (cat[0] + 1, cat[1] - 1, "SW"),
            (cat[0] + 1, cat[1],     "SE")
        ]
    else :
        candidates = [
            (cat[0] - 1, cat[1],     "NW"),
            (cat[0] - 1, cat[1] + 1, "NE"),
            (cat[0], cat[1] - 1,     "W"),
            (cat[0], cat[1] + 1,     "E"),
            (cat[0] + 1, cat[1],     "SW"),
            (cat[0] + 1, cat[1]+1,   "SE")
        ]
    return candidates

## The score is gonna be the distance to the two closest exits.
def compute_score(cat, exits, blocks) :
    distance1 = 10000
    distance2 = 10000
    for ex in exits :
        if not ex in blocks :
            distance = math.sqrt( (ex[0] - cat[0]) ** 2 + (ex[1] - cat[1])**2    )
            if distance < distance1 :
                distance1 = distance
            elif distance < distance2 :
                distance2 = distance
    score = distance1 * distance2
    return score

def wheel(scores) :
    scores  = [5*scores[i] for i in range(len(scores))]
    
    minimum = min(scores)
    scores  = [scores[i] - minimum  for i in range(len(scores))]

    maximum = max(scores)
    scores  = [maximum + 1 - scores[i]  for i in range(len(scores))]

    soma    = sum(scores)
    scores  = [scores[i]*100/soma for i in range(len(scores))]

    guess   = random.randint(0,99)
    acc     = 0

    chosen  = 0
    try :
        while True :        
            acc += scores[chosen]
            if guess <= acc :
                break
            chosen += 1
    except :
        sys.exit()
    return chosen

candidates = valid_movements(cat, blocks)

if len(candidates) == 0 :
    sys.exit()

scores     = []

for cand in candidates :
    scores.append(compute_score(cand, exits, blocks))

chosen = wheel(scores)
print(candidates[chosen][2])
