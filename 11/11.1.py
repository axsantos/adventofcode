import sys
from dataclasses import dataclass
@dataclass
class Monkey:
    items: list
    op: str
    test: int
    if_true: int
    if_false: int
    inspected: int

monkeys = []

data = sys.stdin.read().strip()

for block in data.split("\n\n"):
    lines = block.splitlines()
    
    # line 1: items
    items = lines[1].split("Starting items: ")[1].split(",")
    # line 2: op 
    op_str = lines[2].split("= ")[1]
    op = eval(f"lambda old: {op_str}")
    # line 3: test (only op is divisable, so store only int) 
    test = lines[3].split("by ")[1]
    # line 4: if true
    if_true = lines[4].split("monkey ")[1]
    # line 5: if false
    if_false = lines[5].split("monkey ")[1]
    monkeys.append(Monkey(items, op, int(test), int(if_true), int(if_false), 0))

for round in range(1, 21):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = int(monkey.items.pop(0))
            item = monkey.op(item)
            item = item // 3
            
            if item % monkey.test == 0:
                next_monkey = monkey.if_true
            else:
                next_monkey = monkey.if_false
            
            monkeys[next_monkey].items.append(item)
            monkey.inspected += 1

#for monkey in monkeys:
#    print(monkey.items)
#    print(monkey.inspected)

inspected = sorted([monkey.inspected for monkey in monkeys], reverse = True)
print(inspected[0] * inspected[1])

