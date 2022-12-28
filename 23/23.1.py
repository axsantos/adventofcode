import sys
from collections import defaultdict, deque

from dataclasses import dataclass

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
    
    def neighbours_all(self) -> list:
        neighs = []
        for dir in [Point(0, 1), Point(1, 0), Point(-1, 0), Point(0, -1),
                    Point(1, 1), Point(1, -1), Point(-1, -1), Point(-1, 1)]:
            neighs.append(self.sum(dir))

        return neighs

    def __hash__(self) -> int:
        return hash((self.x, self.y))

def print_grid(grid):
    max_x = max([point.x for point in grid.keys()])
    min_x = min([point.x for point in grid.keys()])
    max_y = max([point.y for point in grid.keys()])
    min_y = min([point.y for point in grid.keys()])

    for y in range(min_y, max_y + 1):
        row = ''.join(str(grid.get(Point(x, y), '.')) for x in range(min_x, max_x + 1))
        print(row)

def count_blanks(grid):
    max_x = max([point.x for point in grid.keys()])
    min_x = min([point.x for point in grid.keys()])
    max_y = max([point.y for point in grid.keys()])
    min_y = min([point.y for point in grid.keys()])

    blanks = 0
    for y in range(min_y, max_y + 1):
       for x in range(min_x, max_x + 1):
                p = Point(x, y)
                if board.get(p) != '#':
                    blanks += 1
    
    return blanks

rules = [
    # If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step
    [[(0,-1), (-1,-1), (1,-1)], (0,-1)],    
    # If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step
    [[(0,1), (-1,1), (1,1)], (0,1)],
    #If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step
    [[(-1,0), (-1,-1), (-1,1)], (-1,0)],
    #If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.
    [[(1,0), (1,-1), (1,1)], (1,0)]
]

def proposal():
    prop = defaultdict(list)
    for p, v in board.items():
        if v == "#":
            skip = True
            # check if any elves neighbouring
            for n in p.neighbours_all():
                if board.get(n) == '#':
                    skip = False

            if skip:
                continue

            for rule in rules:
                go = True
                for dx, dy in rule[0]:
                    val = board.get(p.add(dx, dy))
                    if val == "#":
                        go = False
                    
                if go:
                    dx, dy = rule[1]
                    prop[p.add(dx, dy)].append(p)
                    break
                    
    for new_loc, elves in prop.items():
        if len(elves) == 1:
            board[elves[0]] = "."
            board[new_loc] = "#"
 
    return prop

data = sys.stdin.read().strip()

board = {}

for y, line in enumerate(data.splitlines()):
    for x, val in enumerate(line):
        board[Point(x, y)] = val

# Simulate the Elves' process
# find the smallest rectangle that contains the Elves after 10 rounds.
# How many empty ground tiles does that rectangle contain?

for i in range(1,11):
    proposal()
    # rules change after each round: first becomes last
    rules = rules[1:] + rules[:1]
    print(f"====== End of round {i} =======")
    print_grid(board)

# clean any columns/rows with only dots
cleanup = {p:'#' for p in board if board[p] == '#'}
print(f"====== Cleanup =======")
print_grid(cleanup)
print(count_blanks(cleanup))