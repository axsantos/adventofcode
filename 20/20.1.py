import sys

data = sys.stdin.read().strip()

numbers = []

class Node:
    def __init__(self, val, prv=None, nxt=None):
        self.val = val
        self.prv = prv
        self.nxt = nxt


for line in data.splitlines():
    numbers.append(Node(int(line)))
 
 # Link the middle list
for a,b in zip(numbers,numbers[1:]):
    a.nxt = b
    b.prv = a

# make it circular
numbers[-1].nxt = numbers[0]
numbers[0].prv = numbers[-1]

def move(node):
    # remove from list
    node.prv.nxt = node.nxt
    node.nxt.prv = node.prv

    # move
    move = node.val % (len(numbers) - 1)
    a, b = node.prv, node.nxt
    for _ in range(move):
        a = a.nxt
        b = b.nxt

    # reconnect
    node.prv = a
    node.nxt = b
    a.nxt = node
    b.prv = node

for node in numbers:
    move(node)

for node in numbers:
    if node.val == 0:
        r = 0
        zero = node
        for _ in range(3):
            for _ in range(1000):
                zero = zero.nxt
            r += zero.val
        print(r)
