import sys

data = sys.stdin.read().strip()

cubes = set()

for line in data.splitlines():
    x, y, z = line.split(",")
    cubes.add((int(x),int(y),int(z)))

cnt = 0
# lets count sides then
for x, y, z in cubes:
    for dx, dy, dz in [(0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0)]:
        if (x + dx, y + dy, z + dz) not in cubes:
            cnt += 1

print(cnt)