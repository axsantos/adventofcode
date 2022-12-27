import sys

data = sys.stdin.read().strip()

nums = []

def convert_to_decimal(val):
    m = {
        '2' : 2,
        '1' : 1,
        '0' : 0,
        '-' : -1,
        '=' : -2
    }

    a = [1]
    while(len(a) < len(val)):
        a.append(5 * a[-1])

    a.reverse()

    cnt = 0
    for a, b in zip(a, val):
        cnt += m[b] * a
    
    return cnt

def convert_to_snafu(val):
    b5 = []
    while val:
        b5.append(val % 5)
        val //= 5
    
    b5 = [0] + b5[::-1]
    
    while any(n >= 3 for n in b5):
        for i in range(len(b5)):
            if b5[i] >= 3:
                b5[i-1] += 1
                b5[i] -= 5
    
    return "".join(["0","1","2","=","-"][n] for n in b5).lstrip("0")

for line in data.splitlines():
    nums.append(convert_to_decimal(line))

print(convert_to_snafu(sum(nums)))