import string
import sys

def get_prio(val):
    abc = list(string.ascii_letters)
    return abc.index(val) + 1

def get_compartments(rucksack):
    half = len(rucksack) // 2

    return rucksack[:half], rucksack[-half:]

def find_common_element(a, b):
    return set(a).intersection(b).pop()

data = sys.stdin.read().strip()

total = 0
for line in data.splitlines():
    a, b = get_compartments(line)
    total = total + get_prio(find_common_element(a, b))

print(total)




