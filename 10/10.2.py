import sys

data = sys.stdin.read().strip()

cycles = 0
x = 1
vals = []

for instr in data.splitlines():
    instr = instr.split()
    op = instr[0]

    if op == "noop":
        vals.append(x)
        cycles += 1
    
    if op == "addx":
        vals.append(x)
        vals.append(x)
        cycles += 2
        x += int(instr[1])

    
for i in range(len(vals)):
    pos = i % 40
    sprite = [pos - 1, pos, pos + 1]
    if vals[i] in sprite: 
        print("#", end="")
    else:
        print(".", end="")

    if pos == 39:
        print("")
