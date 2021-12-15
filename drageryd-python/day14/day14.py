import sys
import cProfile
import pstats
import numpy


data = sys.stdin.read().strip()
dataa = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

template, rules = data.split("\n\n")
#print(template)
#print(rules)

"""
for step in range(1):
    next_template = ""
    for a,b in zip(template[:-1], template[1:]):
        # Append a regardless
        next_template += a
        # If there is a polymer rule
        # Add the element after a
        if a + b in rules:
            next_template += rules[a + b]
        # b is a in next loop
    # Finally add last b
    next_template += b
    template = next_template
    print(template)

    # Count most common
    #counts = sorted([(c, template.count(c)) for c in set(template)], key=lambda x: x[1])
    #print(counts[-1][1] - counts[0][1])
    """

#print("[('N', 'C'), ('C', 'N'), ('N', 'B'), ('B', 'C'), ('C', 'H'), ('H', 'B')]")

def solve(template, rules, depth):
    queue = [(a + b, depth) for a,b in zip(template[:-1], template[1:])]
    rules = dict(r.split(" -> ") for r in rules.split("\n"))

    # Every known location will be for example ("AB", 3)
    # which means that the value holds the result if AB is expanded 3 times
    known = {}
    def expand(pair, depth):
        # If depth at bottom the value is simply the first
        # character in the pair
        if depth == 0:
            #print("Calculating {} at depth 0".format(pair))
            return {pair[0]: 1}
        # Return value direcly if it is already known
        if (pair, depth) in known:
            #print("Returning {} at depth {} = {}".format(pair, depth, len(known[(pair,depth)])))
            return known[(pair, depth)]
        # Character to insert
        character = rules[pair]
        head = expand(pair[0] + character, depth - 1)
        tail = expand(character + pair[1], depth - 1)
        # Now that this has been calculated it can be added to known
        known[(pair, depth)] = {c:head.get(c,0)+tail.get(c,0) for c in set(head.keys()).union(tail.keys())}
        return known[(pair, depth)]

    # Process all of queue
    total_count = {}
    for p,d in queue:
        character_count = expand(p,d)
        for character, count in character_count.items():
            total_count[character] = total_count.get(character, 0) + count
    # Lastly count the last character once more
    total_count[template[-1]] += 1
    ordered = sorted(total_count.items(), key=lambda x: x[1])
    #print(ordered[0], ordered[-1])
    return ordered[-1][1] - ordered[0][1]

with cProfile.Profile() as pr:
    print(solve(template, rules, 10))
    print(solve(template, rules, 40))

stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()
