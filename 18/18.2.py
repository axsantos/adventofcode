import sys
from collections import deque

data = sys.stdin.read().strip()

cubes = set()

min_cubes = (1000, 1000, 1000)
max_cubes = (-1000, -1000, -1000)

min_x = min_y = min_z = -10000

for line in data.splitlines():
    x, y, z = map(int, line.split(","))
    max_x, max_y, max_z = max_cubes
    min_x, min_y, min_z = min_cubes
    max_cubes = (max(max_x, x), max(max_y, y), max(max_z, z))
    min_cubes = (min(min_x, x), min(min_y, y), min(min_z, z))
    cubes.add((int(x),int(y),int(z)))

def is_internal(node):
    # we are going to do a dfs
    seen = set()
    q = deque([node])

    while q:
        n = q.popleft()
        x, y, z = n

        if n in seen:
            continue

        cond_x = min_x <= x < max_x
        cond_y = min_y <= y < max_y
        cond_z = min_z <= z < max_z

        if not (cond_x and cond_y and cond_z):
            return False

        seen.add((x, y, z))

        for dx, dy, dz in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
            nx, ny, nz = x + dx, y + dy, z + dz
            if (nx, ny, nz) in cubes:
                continue

            q.append((nx, ny, nz))

    return True

cnt = 0
# lets count sides then
for x, y, z in cubes:
    for dx, dy, dz in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) not in cubes:
            if not is_internal((nx, ny, nz)):
                cnt += 1

print(cnt)