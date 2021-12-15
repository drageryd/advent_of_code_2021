import sys

data = sys.stdin.read().strip()
test = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

def generate_map(data):
    return {x+y*1j: int(r)
            for y,row in enumerate(data.split("\n"))
            for x,r in enumerate(row)}

def solve(risk_map):
    queue = [(0,0)]
    visited = set((0,0))
    end = max(k.real for k in risk_map) + max(k.imag for k in risk_map) * 1j
    adjacent = [1, -1, 1j, -1j]
    c = 0
    while queue:
        position, risk = queue.pop(0)
        #print(position, risk)
        if position == end:
            return risk
        for a in adjacent:
            if position + a not in risk_map:
                continue
            if position + a not in visited:
                # Insert new position in queue
                i = 0
                for p, r in queue:
                    if r > risk + risk_map[position + a]:
                        break
                    i += 1
                queue.insert(i, (position + a, risk + risk_map[position + a]))
                visited.add(position + a)
        #print(len(queue))


#print(solve(generate_map(test)))
print(solve(generate_map(data)))

# Assemble data for part 2
def generate_extended_map(data):
    sx = len(data.split("\n")[0])
    sy = len(data.split("\n"))

    risk_map = {}
    for dy in range(5):
        for dx in range(5):
            map_part = {sx*dx+x+(sy*dy+y)*1j: (int(r) + dx + dy) if (int(r) + dx + dy) <= 9 else (int(r) + dx + dy) - 9
                        for y,row in enumerate(data.split("\n"))
                        for x,r in enumerate(row)}
            risk_map.update(map_part)
    return risk_map

#print(solve(generate_extended_map(test)))
print(solve(generate_extended_map(data)))
