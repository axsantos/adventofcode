import sys
from dataclasses import dataclass
from collections import deque 

@dataclass
class Point:
    x: int
    y: int

    def add(self, dx: int, dy: int) -> "Point":
        return Point(self.x + dx, self.y + dy)
    
    def sum(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def distance(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def in_board(self, weight: int, height: int) -> bool:
        if self.x >= weight or self.y >= height or self.x < 0 or self.y < 0:
            return False
        else:
            return True

    def neighbours(self) -> list:
        neighs = []
        for dir in [Point(0, 1), Point(1, 0), Point(-1, 0), Point(0, -1)]:
            neighs.append(self.sum(dir))

        return neighs

    def __hash__(self) -> int:
        return hash((self.x, self.y))

data = sys.stdin.read().strip()

grid = [list(line) for line in data.splitlines()]

weight = len(grid[0])
height = len(grid)

source = None
target = None

board = {}
for y in range(height):
    for x in range(weight):
        
        board[Point(x, y)] = ord(grid[y][x])

        if grid[y][x] == "S":
            source = Point(x, y)
            board[source] = ord("a")

        elif grid[y][x] == "E":
            target = Point(x, y)
            board[target] = ord("z")

print(board)
print(source)
print(target)

def search(start):
    queue = deque()
    seen = set()

    queue.append((start, 0))

    while queue: 
        p, depth = queue.popleft()

        if p in seen:
            print(f"[{p}][{depth}] been here {n}")
            continue
        elif p == target:
            return depth

        seen.add(p)

        for n in p.neighbours():
            if not n.in_board(weight, height):
                print(f"[{p}][{depth}] out of board {n}")
                continue

            if board.get(n) - 1 <= board.get(p):
                queue.append((n, depth + 1))

    return 1e9

print(search(source))




