import sys

data = sys.stdin.read().strip()

elfs = []
calories = 0
id = 1

for line in data.splitlines():
    if line:
        calories += int(line)
    else:
        id += 1
        elfs.append(calories)
        calories = 0

print(sorted(elfs, reverse=True)[0])