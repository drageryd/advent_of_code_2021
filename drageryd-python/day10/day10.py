import  sys

# Parse input
data = sys.stdin.read().strip()
lines = [list(x) for x in data.split("\n")]

# Matching brackets and score system
matching = {"[": "]", "(": ")", "{": "}", "<": ">"}
scores = {")": (3,1), "]": (57,2), "}": (1197,3), ">": (25137,4)}

# Recursively parse every line
def parse(line):
    # Pop opening bracket
    opening = line.pop(0)
    # Loop as long as the next character is an opening bracket
    # If some recursive call returned incomplete, break
    ret = ""
    while not ret and line and line[0] in matching:
        ret = parse(line)
    # If there is no more characters, the line is incomplete
    if not line:
        return opening + ret
    # Else check if the closing bracket is invalid
    closing = line.pop(0)
    if closing != matching[opening]:
        line.clear()
        return closing
    # Reaching end if valid
    return ""

# Parse input once and collect invalid and incomplete lines
invalid = []
incomplete = []
for line in lines:
    # Some lines have a valid start
    # Parse them until whole line is consumed
    while line:
        res = parse(line)
    # res is empty if ok
    if not res:
        continue
    # Either invalid or incomplete
    # If the last read char is closing it is invalid
    if res[-1] in scores:
        invalid.append(res[-1])
    else:
        incomplete.append(res)

# Part 1 - Invalid lines
print("Part 1: {}".format(sum(scores[i][0] for i in invalid)))

# Part 2 - Incomplete lines
def calculate_score(incomplete):
    score = 0
    while incomplete:
        score *= 5
        score += scores[matching[incomplete.pop()]][1]
    return score

incomplete_scores = [calculate_score(list(i)) for i in incomplete]
incomplete_scores.sort()
print("Part 2: {}".format(incomplete_scores[(len(incomplete_scores) - 1) // 2]))
