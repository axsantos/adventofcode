import sys
from collections import defaultdict, deque
import math

data = sys.stdin.read().strip()

monkeys = {}
result = {}

def calculate(id):
    if type(monkeys[id]) == int or type(monkeys[id]) == bool:
        return monkeys[id]
    
    a, op, b = monkeys[id]
    
    a = calculate(a)
    b = calculate(b)

    if id == "root":
        return eval(f"{a} {op} {b}")

    return eval(f"{a} {op} {b}")

for line in data.splitlines():
    monkey = line.split(": ")
    if len(monkey[1].split(" ")) == 1:
        monkeys[monkey[0]] = int(monkey[1])
    else:
        a, op, b = monkey[1].split(" ")
        monkeys[monkey[0]] = (a, op, b)
        if monkey[0] == "root":
            monkeys['root'] = (a, "==", b)

a, _, b = monkeys["root"]

#start = 3375719472760
start = 0
offset = 20

def simulate(start, offset):
    prv_a = 0
    diff = 0

    for i in range(int(start), int(start) + offset):
        monkeys["humn"] = i
        result = {}
        for k in monkeys.keys():
            result[k] = calculate(k)
        
        a, _, b = monkeys["root"]
        if i % (offset / 2) == 0:
            if prv_a:
                diff = prv_a - result[a]
            
            prv_a = result[a]
    
            if diff:
                estimated = i + (result[a] - result[b]) * ((offset / 2) / diff)
                print(f"a = {result[a]} (diff = {diff}) || b = {result[b]} (diff = {result[a] - result[b]}) || estimated {estimated}")
        
        if(result['root']):
            return True, result["humn"]

    return False, estimated

estimated = 0
for i in range(10):
    print(f"Try #{i}")
    finished, estimated = simulate(estimated, 20)
    if finished:
        print(estimated)
        break
