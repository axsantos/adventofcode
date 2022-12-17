import sys
from dataclasses import dataclass

directions = {
    "U":  (0, 1),
    "D":  (0, -1),
    "L":  (-1, 0),
    "R":  (1, 0)
}


def update(head, tail):
    print(f"[{head}] > [{tail}] distance ({head.distance(tail)})")
    # if move diag
    if head.distance(tail) > 2:
        if head.x > tail.x and head.y > tail.y:
            tail = tail.add(1, 1)
        if head.x < tail.x and head.y > tail.y:
            tail = tail.add(-1, 1)  
        if head.x > tail.x and head.y < tail.y:
            tail = tail.add(1, -1)
        if head.x < tail.x and head.y < tail.y:
            tail = tail.add(-1, -1)
    # if horizontally or vertically
    if head.distance(tail) > 1:
        if head.x == tail.x and head.y > tail.y:
            tail = tail.add(0, 1)
        if head.x == tail.x and head.y < tail.y:
            tail = tail.add(0, -1)
        if head.y == tail.y and head.x > tail.x:
            tail = tail.add(1, 0)
        if head.y == tail.y and head.x < tail.x:
            tail = tail.add(-1, 0)

    return tail

@dataclass
class Point:
    x: int
    y: int

    def add(self, dx: int, dy: int) -> "Point":
        return Point(self.x + dx, self.y + dy)

    def distance(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


head = Point(0, 0)
tail = Point(0, 0)

seen = set()
data = sys.stdin.read().strip()

for instr in data.splitlines():
    direction, steps = instr.split(" ")

    #print(f"Instruction: {direction}, {steps}")

    for _ in range(int(steps)):
        dx, dy = directions[direction]
        #print(f"dir {direction} > {dx}, {dy}")

        head = head.add(dx, dy)
        #print(f"Head > {head}, Tail: > {tail}")
        tail = update(head, tail)
        seen.add(tail)

print(f"Part 1: {len(seen)}")