import sys
depths = [int(n) for n in sys.stdin.read().strip().split("\n")]
print(sum(1 for a,b in zip(depths[:-1],depths[1:]) if b>a))
windows = [sum(x) for x in zip(depths[:-2],depths[1:-1],depths[2:])]
print(sum(1 for a,b in zip(windows[:-1],windows[1:]) if b>a))
