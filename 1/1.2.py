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

top3 = 0
for i in sorted(elfs)[-3:]:
    top3 += i

print(top3)