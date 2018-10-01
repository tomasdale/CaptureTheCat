import sys
import random

cat    = eval(sys.argv[1])
blocks = eval(sys.argv[2])
exits  = eval(sys.argv[3])

def generate_random(used) :
    candidate = (random.randint(0, 10), random.randint(0, 10))
    while candidate in used :
        candidate = (random.randint(0, 10), random.randint(0, 10))    
    return candidate

print(generate_random(blocks + [tuple(cat)]))
