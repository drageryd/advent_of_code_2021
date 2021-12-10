import sys

directions = {"forward": 1j, "down": 1, "up": -1}
actions = [x.split(" ") for x in sys.stdin.read().strip().split("\n")]
position = sum(int(n)*directions[d] for d,n in actions)
print(int(position.real * position.imag))

aim = 0
horizontal = 0
depth = 0
for d,n in actions:
    if d == "forward":
        horizontal += int(n)
        depth += int(n) * aim
    else:
        aim += directions[d] * int(n)
print(horizontal * depth)
