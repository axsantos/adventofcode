import sys

data = sys.stdin.read().strip()

cycles = 0
x = 1
tosum = 20
res = 0

for instr in data.splitlines():
    instr = instr.split()
    op = instr[0]

    if op == "noop":
        cycles += 1
    
    if op == "addx":
        cycles += 2
    
    if cycles >= tosum:
        print(f"[cycle {cycles}] adding to res [{x * tosum}]")
        res += x * tosum
        tosum += 40
    
    # update only after
    if op == "addx":
        x += int(instr[1]) 

print(res)
