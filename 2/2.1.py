import sys 

data = sys.stdin.read().strip()

translator = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",
    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors",
}

val = {
    "rock" : 1,
    "paper" : 2,
    "scissors" : 3,
}

def strat_calc(theirs, strat):
    if strat == "X":
        #lose
        if theirs == "rock":
            return "scissors"
        elif theirs == "paper":
            return "rock"
        elif theirs == "scissors":
            return "paper"
    elif strat == "Y":
        # draw
        return theirs
    elif strat == "Z":
        # win
        if theirs == "rock":
            return "paper"
        elif theirs == "paper":
            return "scissors"
        elif theirs == "scissors":
            return "rock"

def result_calc(a, b):
    if a == b:
        return 3
    elif a == "rock":
        if b == "scissors":
            return 6
        else:
            return 0
    elif a == "paper":
        if b == "rock":
            return 6
        else:
            return 0
    elif a == "scissors":
        if b == "paper":
            return 6
        else:
            return 0


total = 0
for line in data.splitlines():
    play = line.split(" ")

    theirs = translator.get(play[0])
    ours = translator.get(play[1])

    total = total + result_calc(ours, theirs) + val.get(ours)

print(total)
