import sys

data = sys.stdin.read().strip()

grid = []

for line in data.splitlines():
    grid.append([int(col) for col in line])

height = len(grid)
width = len(grid[0])

visible = 0
max_score = 0


def calc_score(val, side):
    score = 0
    for neigh in side:
        score += 1
        if neigh >= val:
            break
            
    return score


max_score = 0

for x in range(width):
    for y in range(height):

        # must search in every direction
        row = grid[y]
        col = [row[x] for row in grid]
        val = grid[y][x]

        left = row[:x]
        right = row[x+1:]
        up = col[:y]
        down = col[y+1:]

        left.reverse()
        up.reverse()
        score_left = calc_score(val, left)
        score_right = calc_score(val, right)
        score_up = calc_score(val, up)
        score_down = calc_score(val, down)

        score_tree = calc_score(val, left) * calc_score(val, right) * \
            calc_score(val, up) * calc_score(val, down)

        if score_tree > max_score:
            print(f"[{x}][{y}]new max score: {score_tree}")
            max_score = score_tree


print(max_score)
