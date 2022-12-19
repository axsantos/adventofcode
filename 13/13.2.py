import sys
from functools import cmp_to_key

data = sys.stdin.read().strip()

def right_order(x, y):
    if not type(x) == list:
        x = [x]

    if not type(y) == list:
        y = [y]

    for i in range(min(len(x), len(y))):
        if type(x[i]) == list or type(y[i]) == list:
            ret = right_order(x[i], y[i])
            if ret != 0:
                return ret
        elif x[i] < y[i]:
            return -1
        elif x[i] > y[i]:
            return 1

    if len(x) < len(y):
        return -1

    if len(x) > len(y):
        return 1    

    return 0

packets = []
for pair in data.split("\n\n"):
    for packet in pair.splitlines():
        packets.append(eval(packet))

packets.append([[2]])
packets.append([[6]])

packets = sorted(packets, key=cmp_to_key(right_order))

for idx, packet in enumerate(packets, start=1):
    if packet == [[2]]:
        print(f"[2] {idx}")
        sig = idx
    if packet == [[6]]:
        print(f"[6] {idx}")
        sig *= idx

print(sig)