import sys

notes = sys.stdin.read().strip()
anotes = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
anotes = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

notes = [tuple(tuple(y.split(" ")) for y in x.split(" | ")) for x in notes.split("\n")]
unique = set([2, 3, 4, 7])

print(sum(sum(1 for x in o if len(x) in unique) for p,o in notes))

# So we are not really interested in what segement maps to what signal
# More like which sequence maps to what digit, so that should be possible
# So starting from 1, 7, 4 and 8 we can create other digits

def solve(pattern, output):
    unknown = set(frozenset(p) for p in pattern)
    dp = {}
    # Get 1, 4, 7 and 8
    for p in list(unknown):
        if len(p) == 2:
            dp[1] = p
            unknown.remove(p)
        elif len(p) == 3:
            dp[7] = p
            unknown.remove(p)
        elif len(p) == 4:
            dp[4] = p
            unknown.remove(p)
        elif len(p) == 7:
            dp[8] = p
            unknown.remove(p)
    #print(1, "".join(dp[1]))
    #print(4, "".join(dp[4]))
    #print(7, "".join(dp[7]))
    #print(8, "".join(dp[8]))
    # 9
    nine_mask = set().union(dp[4], dp[7])
    dp[9] = [x for x in unknown if not nine_mask.difference(x)].pop()
    unknown.remove(dp[9])
    #print(9, "".join(dp[9]))
    # 6
    six_mask = set().union(frozenset(dp[9]).difference(dp[7]),
                           frozenset(dp[8]).difference(dp[9]))
    dp[6] = [x for x in unknown if not six_mask.difference(x)].pop()
    unknown.remove(dp[6])
    #print(6, "".join(dp[6]))
    # 0
    zero_mask = set().union(dp[7], frozenset(dp[8]).difference(dp[9]))
    dp[0] = [x for x in unknown if not zero_mask.difference(x)].pop()
    unknown.remove(dp[0])
    #print(0, "".join(dp[0]))
    # 5
    dp[5] = [x for x in unknown if not frozenset(x).difference(dp[6])].pop()
    unknown.remove(dp[5])
    # 3
    dp[3] = [x for x in unknown if not frozenset(x).difference(dp[9])].pop()
    unknown.remove(dp[3])
    # 2
    dp[2] = unknown.pop()

    result = 0
    for c in output:
        c = frozenset(c)
        for d, p in dp.items():
            if c == p:
                result = 10 * result + d
                break
    return result
print(sum(solve(p, o) for p, o  in notes))
