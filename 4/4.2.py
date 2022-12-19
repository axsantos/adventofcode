import sys

data = sys.stdin.read().strip()

def build_list(val):
    x = val.split("-")
    return list(range(int(x[0]), int(x[1])+1))

def check_if_subset(a, b):
    return set(a) <= set(b)

def check_intersect(a, b):
    return set(a).intersection(b)


total = 0
for line in data.splitlines():
    pairs = line.split(",")
    a = build_list(pairs[0])
    b = build_list(pairs[1])
    #print(f"Testing: {a} | {b}")
    if(check_intersect(a, b)):
    #   print(f"found one: {a} | {b}")
        total += 1

print(total)