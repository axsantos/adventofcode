import sys
import copy
from dataclasses import dataclass

data = sys.stdin.read().strip()

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

board = {}

def print_grid(grid):
    max_x = max([point.x for point in grid.keys()])
    min_x = min([point.x for point in grid.keys()])
    max_y = max([point.y for point in grid.keys()])
    min_y = min([point.y for point in grid.keys()])

    for y in range(min_y, max_y + 1):
        row = ''.join(str(grid.get(Point(x, y), ' ')) for x in range(min_x, max_x + 1))
        print(row)

def sand_simulation(board, abyss = 1000000):
    board = copy.deepcopy(board)
    sand = source

    while True:
 
        if sand.y > abyss:
            return board
        
        if board.get(sand.add(0, 1), '.') not in ["#", "o"]:
            sand = sand.add(0, 1)
            continue
        elif board.get(sand.add(-1, 1), '.') not in ["#", "o"]:
            sand = sand.add(-1, 1)
            continue
        elif board.get(sand.add(1, 1), '.') not in ["#", "o"]:
            sand = sand.add(1, 1)
            continue
        else:
            board[sand] = "o"
            sand = source

for rock_path in data.splitlines():
    prv = None
    for rock in rock_path.split('-> '):
        if not prv:
            prv = Point(int(rock.split(',')[0]), int(rock.split(',')[1]))
            continue
        else:           
            cur = Point(int(rock.split(',')[0]), int(rock.split(',')[1]))
            for x in range(min(prv.x, cur.x), max(prv.x, cur.x) + 1):
                for y in range(min(prv.y, cur.y), max(prv.y, cur.y)+ 1):
                    board[Point(x, y)] = "#"
            prv = cur

source = Point(500, 0)
board[source] = "+"

abyss = max([point.y for point in board.keys()]) + 100

res_board = sand_simulation(board, abyss)

print(sum(1 for v in res_board.values() if v == "o"))