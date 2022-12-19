import sys 

data = sys.stdin.read().strip()

def all_unique(val):
    return len(val) == len(set(val))

for line in data.splitlines():
    for i in range(len(line)):
        window = line[i:i+14]
        #print(f"[{i}] check [{window}]: {all_unique(window)} {len(window)} {len(set(window))} ")
        
        if all_unique(window):
            print(i+14)
            len(line)
            break

