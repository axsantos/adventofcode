import sys
import re
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

sensors = set()
beacons = set()
dists = {}

data = sys.stdin.read().strip()

for line in data.splitlines():
    
    sensor_str = line.split(":")[0].split("=")
    sensor = Point(int(sensor_str[1].split(",")[0]), int(sensor_str[2]))
   
    beacon_str = line.split(":")[1].split("=")
    beacon = Point(int(beacon_str[1].split(",")[0]), int(beacon_str[2]))

    sensors.add(sensor)
    beacons.add(beacon)
    dists[sensor] = sensor.distance(beacon)

cnt = 0
y = 10
y = 2000000

max_dist = max(dists.values())
min_x = min([point.x for point in dists.keys()])
max_x = max([point.x for point in dists.keys()])

for x in range(min_x - max_dist - 1, max_x + max_dist + 2):
    cur = Point(x, y)
    for s in sensors:
        dist = cur.distance(s)
        if dist <= dists[s] and cur not in beacons:
            cnt += 1
            break

print(cnt) 