import  sys

data = sys.stdin.read().strip()
sdata = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

lines = data.split("\n")
#heightmap = {x+y*1j:int(v) for y,row in enumerate(data.split("\n")) for x,v in enumerate(row)}

m = {
    "[": "]",
    "(": ")",
    "{": "}",
    "<": ">",
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def parse(line):
    #print(line, len(line))
    if len(line) < 2:
        #print("invalid")
        if line and line[0] in scores:
            return 0, scores[line[0]], ""
        else:
            #print("incomplete")
            return 0, 0, line[0]
    # Get opening
    o = line[0]
    #print(o)
    # Peek at next 
    if line[1] == m[o]:
        # Bracket closing
        #print(line[1])
        #print("valid")
        return 2, 0, ""
    else:
        y = 1
        x, s, l = parse(line[y:])
        while x != 0:
            y += x
            #print(y)
            if y >= len(line):
                #print("incomplete2", o + l)
                return y + 1, 0, o + l
            #print(y)
            if line[y] == m[o]:
                #print(line[y])
                #print("valid")
                return y + 1, 0, l
            elif line[y] in m:
                x, s, l = parse(line[y:])
            elif line[y] in scores:
                #print("Expected {}, but found {} instead".format(m[o], line[y]))
                return 0, scores[line[y]], line[y:]
            else:
                #print("invalid")
                return 0, 0, o + l
        #print(s)
        #if not l:
        #    print(l)
        return 0, s, o + l

#parse("[]")
#parse("([])")
#parse("{()()()}")
#parse("<([{}])>")
#parse("[<>({}){}[([])<>]]")
#parse("(((((((((())))))))))")

#print(parse("(]"))
#print(parse("{()()()>"))
#print(parse("(((()))}"))
#print(parse("<([]){()}[{}])"))

#print(parse("{[([{[[[{({<<[<>[]]<()[]>>(<[]<>>({}))><{[{}()]{<>{}}}<<{}{}>{{}[]}>>}<<{{<>()}<()()>}<[(){}]<[]{"))

# Part 1
"""
score = 0
for line in lines:
    o, s, l = parse(line)
    score += s
print(score)
"""


#print(parse("[({(<(())[]>[[{[]{<()<>>"))

def p2(line):
    o, s, l = parse(line)
    if s:
        return ""
    #print(o, s, l)
    #print(o, s, l)
    while o and o < len(line):
        line = line[o:]
        #print(line)
        o, s, l = parse(line)
    return l
#print(parse("(((({<>}<{<{<>}{[]{[]{}"))
#print(parse("{<[[]]>}<{[{[{[]{()[[[]"))
#print(parse("<{([{{}}[<[[[<>{}]]]>[]]"))

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

# Part 2
score = []
for line in lines:
    inc = p2(line)
    if inc:
        #print("".join(inc))
        inc = list(inc)
        s = 0
        while inc:
            c = inc.pop()
            #print(c, s)
            s *= 5
            s += scores.get(m.get(c, 0), 0)
        #print(s)
        score.append(s)

score = sorted(score)

print(score[(len(score) - 1) // 2])
