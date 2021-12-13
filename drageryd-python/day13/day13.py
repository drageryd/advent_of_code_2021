import sys

data = sys.stdin.read().strip()
dots, folds = data.split("\n\n")
dots = set(tuple(int(d) for d in dot.split(",")) for dot in dots.split("\n"))
folds = [f.split(" ")[2].split("=") for f in folds.split("\n")]

p1 = True
for axis, value in folds:
    value = int(value)
    # Loop over copy of dots
    for x,y in list(dots):
        if axis == "x" and x > value:
            dots.remove((x,y))
            dots.add((x-2*(x-value),y))
        elif axis == "y" and y > value:
            dots.remove((x,y))
            dots.add((x,y-2*(y-value)))
    if p1:
        print(len(dots))
        p1 = False

for y in range(max(dots, key=lambda p: p[1])[1] + 1):
    for x in range(max(dots, key=lambda p: p[0])[0] + 1):
        print("#" if (x,y) in dots else ".", end="")
    print("")
