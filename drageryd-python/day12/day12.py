import sys

data = sys.stdin.read().strip()
# Produce cave pairs (e.g A-b also is b-A)
data = [t for d in data.split("\n") for t in (tuple(d.split("-")),tuple(reversed(d.split("-"))))]
# Produce cave map (e.g start leads to A and b)
cave = {}
for k,v in data:
    cave[k] = cave.get(k, ()) + (v,)

def bfs(p2 = False):
    # BFS through all paths
    # queue holds current path
    queue = [(("start",),False)]
    completed = []
    i = 0
    while queue:
        path, twice = queue.pop(0)
        current_cave = path[-1]
        connected_caves = cave[current_cave]
        for c in connected_caves:
            new_twice = twice
            # small caves may not be visited twice
            if c.islower() and c in path:
                if p2:
                    if c == "start" or twice:
                        # In part 2 a small cave can be visited twice
                        continue
                    else:
                        new_twice = True
                else:
                    continue
            # otherwise the path can be explored
            new_path = path + (c,)
            if c == "end":
                completed.append(new_path)
            else:
                queue.append((new_path, new_twice))
    return len(completed)

print(bfs())
print(bfs(True))
