---

### 2. **core.py**

```python
import random

directions = ['N', 'E', 'S', 'W']
silence = '-'

adjacency = {
    'N': {'E', 'W'},
    'E': {'N', 'S'},
    'S': {'E', 'W'},
    'W': {'N', 'S'},
    '-': set(directions)
}

def is_move_allowed(a, b):
    if a == '-' or b == '-':
        return True
    return b not in adjacency[a]

def infinite_sequence():
    current = random.choice(directions + [silence])
    yield current
    while True:
        candidates = [d for d in directions + [silence] if is_move_allowed(current, d)]
        current = random.choice(candidates)
        yield current

class BubbleCore:
    def __init__(self):
        self.seq_gen = infinite_sequence()

    def next_step(self):
        return next(self.seq_gen)
