from core import directions, silence
import random

binary_layer = ['0', '1', silence]

def binary_is_move_allowed(a, b):
    if a == '-' or b == '-':
        return True
    return a != b  # simple example: avoid repeating same binary digit

def infinite_binary_sequence():
    current = random.choice(binary_layer)
    yield current
    while True:
        candidates = [d for d in binary_layer if binary_is_move_allowed(current, d)]
        current = random.choice(candidates)
        yield current

class Layer:
    def __init__(self, mode='direction'):
        if mode == 'direction':
            from core import infinite_sequence
            self.gen = infinite_sequence()
        elif mode == 'binary':
            self.gen = infinite_binary_sequence()
        else:
            raise ValueError("Unsupported mode")

    def next_element(self):
        return next(self.gen)
