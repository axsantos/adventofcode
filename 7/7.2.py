import sys
from pathlib import Path
data = sys.stdin.read().strip()

current_dir = Path("/")
dir_sizes = {}

for line in data.splitlines():
    if line.startswith("$ cd"):
        # update current dir
        #print(f"changing dir to [{line[5:]}]")
        current_dir = (current_dir / line[5:]).resolve()
        #print(f"in {current_dir}")

    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        continue
    else:
        # update current dir size
        line = line.split(" ")
        size = int(line[0])
        #print(f"[{line[1]}]: process sizes > {size}")
        if not dir_sizes.get(str(current_dir)):
            dir_sizes[str(current_dir)] = size
        else:
            dir_sizes[str(current_dir)] += size
        # udpate parents dir sizes
        for i in current_dir.parents:
            if not dir_sizes.get(str(i)):
                dir_sizes[str(i)] = size
            else:
                dir_sizes[str(i)] += size

print(dir_sizes)

unused = 70000000 - dir_sizes["/"]
required = 30000000 - unused

a = [v for v in dir_sizes.values() if v >= required]
print(min(a))