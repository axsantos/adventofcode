import sys

data = sys.stdin.read().strip()

print(data)

grid = []

for line in data.splitlines():
    grid.append([int(col) for col in line])

print(grid)
height = len(grid)
width = len(grid[0])

visible = 0
for x in range(width):
    for y in range(height):
        # print(f"[{x}][{y}]")
        if x == 0 or y == 0 or x == (len(grid) - 1) or y == (len(grid[0]) - 1):
            print(f"[{x}][{y}] is visible")
            visible += 1
        else:
            # must search in every direction
            row = grid[y]
            col = [row[x] for row in grid]
            val = grid[y][x]

            left = row[:x]
            right = row[x+1:]
            up = col[:y]
            down = col[y+1:]

            if max(left) < val or max(right) < val or max(up) < val or max(down) < val:
                print(f"[{x}][{y}] is visible")
                visible += 1
            else:
                print(f"[{x}][{y}] is not visible")

print(visible)
