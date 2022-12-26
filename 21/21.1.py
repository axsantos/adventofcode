import sys
from collections import defaultdict, deque


data = sys.stdin.read().strip()

monkeys = {}
result = {}

def calculate(id):
    if type(monkeys[id]) == int:
        return monkeys[id]
    
    a, op, b = monkeys[id]
    
    a = calculate(a)
    b = calculate(b)

    return int(eval(f"{a} {op} {b}"))

for line in data.splitlines():
    monkey = line.split(": ")
    if len(monkey[1].split(" ")) == 1:
        monkeys[monkey[0]] = int(monkey[1])
    else:
        a, op, b = monkey[1].split(" ")
        monkeys[monkey[0]] = (a, op, b)

for k in monkeys.keys():
    result[k] = calculate(k)

print(result['root'])
