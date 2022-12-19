import sys

data = sys.stdin.read().strip()

parsed = []

def right_order(x, y):
    if not type(x) == list:
        x = [x]

    if not type(y) == list:
        y = [y]

    for i in range(min(len(x), len(y))):
        if type(x[i]) == list or type(y[i]) == list:
            ret = right_order(x[i], y[i])
            if ret != None:
                return ret
        elif x[i] < y[i]:
            return True
        elif x[i] > y[i]:
            return False

    if len(x) < len(y):
        return True

    if len(x) > len(y):
        return False    

    return None

for pair in data.split("\n\n"):
    p = []
    for packet in pair.splitlines():
        p.append(eval(packet))

    parsed.append(p)

res = 0

for idx, pair in enumerate(parsed, start=1):
    if right_order(pair[0], pair[1]):
        res += idx

print(res)