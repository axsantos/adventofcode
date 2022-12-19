import string
import sys 

def get_prio(val):
    abc = list(string.ascii_letters)
    return abc.index(val) + 1

def get_compartments(rucksack):
    half = len(rucksack) // 2

    return rucksack[:half], rucksack[-half:]

def find_common_element(a, b):
    return set(a).intersection(b)

def find_common_element_list(val):
    ab = find_common_element(val[0], val[1])
    return find_common_element(list(ab), val[2]).pop()        

data = sys.stdin.read().strip()

total = 0
group_size = 0
group = []
    
for line in data.splitlines():
    
    group.append(line)
    group_size = group_size + 1
    
    if group_size == 3:
        total = total + get_prio(find_common_element_list(group))
        group_size = 0
        group = []

print(total)

