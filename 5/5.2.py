#    [D]    
#[N] [C]    
#[Z] [M] [P]
# 1   2   3 

#    [C]             [L]         [T]
#    [V] [R] [M]     [T]         [B]
#    [F] [G] [H] [Q] [Q]         [H]
#    [W] [L] [P] [V] [M] [V]     [F]
#    [P] [C] [W] [S] [Z] [B] [S] [P]
#[G] [R] [M] [B] [F] [J] [S] [Z] [D]
#[J] [L] [P] [F] [C] [H] [F] [J] [C]
#[Z] [Q] [F] [L] [G] [W] [H] [F] [M]
# 1   2   3   4   5   6   7   8   9 

import pprint
import re
import sys

pp = pprint.PrettyPrinter(indent=4)

stacks_test = {
    "1" : ["Z", "N"],
    "2" : ["M", "C", "D"],
    "3" : ["P"]
}

stacks = {
    "1": ["Z", "J", "G"],
    "2": ["Q", "L", "R", "P", "W", "F", "V", "C"],
    "9": ["M", "C", "D", "P", "F", "H", "B", "T"],
    "8": ["F", "J", "Z", "S"],
    "7": ["H", "F", "S", "B", "V"],
    "6": ["W", "H", "J", "Z", "M", "Q", "T", "L"],
    "5": ["G", "C", "F", "S", "V", "Q"],
    "4": ["L", "F", "B", "W", "P", "H", "M"],
    "3": ["F", "P", "M", "C", "L", "G", "R"]
}

def move(order):
    #pp.pprint(stacks)
    nr, src, dst = re.search(r"move (\d+) from (\d+) to (\d+)", order).groups()
    #print(f"{order}: {nr} \t| {src} \t| {dst}")
    tmp = []
    for i in range(int(nr)):
        val = stacks.get(src).pop()
        tmp.append(val)
    
    for i in range(int(nr)):
        stacks.get(dst).append(tmp.pop())
    #pp.pprint(stacks)


data = sys.stdin.read().strip()

for line in data.splitlines():
    line = line.rstrip()
    move(line)

for i in range(1,10):
    print(stacks.get(str(i)).pop())