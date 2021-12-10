import sys

raw = sys.stdin.read()
#raw = "16,1,2,0,4,2,7,1,2,14"
positions = [int(x) for x in raw.strip().split(",")]

minp = min(positions)
maxp = max(positions)

minfuel = -1
minpos = -1
for align in range(minp, maxp + 1):
    fuel = sum(abs(align - p) for p in positions)
    if minfuel == -1 or minfuel > fuel:
        minfuel = fuel
        minpos = align
print("Part 1:", minfuel)

def trisum(x):
    return sum(i+1 for i in range(x))

minfuel = -1
minpos = -1
for align in range(minp, maxp + 1):
    fuel = sum(trisum(abs(align - p)) for p in positions)
    if minfuel == -1 or minfuel > fuel:
        minfuel = fuel
        minpos = align
        print(minfuel, minpos)
print("Part 2:", minfuel)
