import numpy as np
import random

random.seed(32)
options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
groups = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
all = [{'rank': option, 'suit': group} for option in options for group in groups]
random.shuffle(all)
handout = {f'{i+1}': [] for i in range(4)}
for _ in range(5):
    for p in handout:
        a = all.pop()
        handout[p].append(a)
for p, h in handout.items():
    print(f"{p}'s hand: {h}") 
